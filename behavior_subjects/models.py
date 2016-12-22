from django.db import models
from django.utils import timezone
from .utils import mouse_path
import tables as tb
from django.db import transaction
import os.path

SEX_CHOICES = (('M', 'male'),
               ('F', 'female'))


class Mouse(models.Model):
    active = models.BooleanField('Active', default=True)
    mouse_number = models.IntegerField('Mouse Number', unique=True)
    surgery_date = models.DateField('Surgery Date', blank=True, default=timezone.now)
    dob = models.DateField('Date of birth', blank=True, default=timezone.now)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, default='')
    date_added = models.DateField('Date added to database', default=timezone.now)
    genotype = models.CharField('Genotype', default='Wild Type', blank=True, max_length=100)

    def __str__(self):
        return 'mouse {0}'.format(self.mouse_number)

    def age(self):
        return timezone.now() - self.dob

    def last_session_date(self):
        # TODO: last session date.
        if self.session_set:
            return self.session_set.latest('run_dtg').run_dtg
        else:
            return ''

    def rig(self):
        if self.session_set:
            return self.session_set.latest('run_dtg').rig
        else:
            return ''

    def last_session_performance(self):
        if self.session_set:
            return self.session_set.latest('run_dtg').performance
        else:
            return ''

    def odorsets(self):
        return self.session_set.values_list('odors').distinct()


class Session(models.Model):
    mouse = models.ForeignKey(Mouse)
    session_num = models.CharField('Session number', max_length=5)
    run_dtg = models.DateTimeField('Run DTG', unique=True)
    added_dtg = models.DateTimeField('Date added')
    file = models.FileField(upload_to=mouse_path)
    performance = models.DecimalField('Session performance', max_digits=3, decimal_places=2, default=0.0)
    valid_trials = models.IntegerField('Number trials completed', default=0)
    trials_correct = models.IntegerField('Trials correct', default=0)
    protocol_name = models.CharField('Protocol Name', max_length=32, default='', blank=True)
    rig = models.CharField('Rig', max_length=10, default='', blank=True)
    lickgraceperiod = models.IntegerField('Lick Grace Period', blank=True, default=0)
    odorset_name = models.CharField('Odorset name', max_length=32, blank=True, default='')
    notes = models.TextField('Session Notes', default='', blank=True)
    bad = models.BooleanField('Bad Session', default=False, blank=True)
    exh_inh_delay = models.IntegerField('Exh-inh delay', default=-1, blank=True)
    first_lick_rt_calc = models.BooleanField('First inh rt calculated?', default=False)
    odors = models.TextField('Odors used', default='', max_length=128)

    @transaction.atomic  # do all processing, commit to database if everything is successful.
    def process(self):
        with tb.open_file(self.file.path) as f:
            assert isinstance(f, tb.File)
            tr_table = f.root.Trials.read()
            ncorrects = 0
            nvalids = 0
            ntrials = 0
            attrs = f.root._v_attrs.__dict__
            self.protocol_name = attrs.get('protocol_name', 'none_specified')
            self.rig = attrs.get('rig', tr_table[0]['rig'])
            self.odorset_name = attrs.get('odor_set_name', 'none_specified')
            self.lickgraceperiod = attrs.get('lickgraceperiod', tr_table['lickgraceperiod'].max())
            odors = set()
            for tr in tr_table:
                result = tr['result']
                try:
                    odor = tr['odor']
                except ValueError:
                    if 'olfas:olfa_0:odor' in tr.dtype.names:
                        odor = tr['olfas:olfa_0:odor']
                    else:
                        odor = ''
                odors.add(bytes.decode(odor))  # strips "b" from string representation.
                valid = result > 0 and result < 5
                correct = result > 0 and result < 3
                nvalids += valid  # boolean adds to integer just fine.
                ncorrects += correct
                ntrials += 1
                try:
                    laser_d = tr['pulseOnsetDelay_1']
                    laser_i = int(b'0'+tr['LaserIntensity_1'][:-2])
                    laser_np = tr['trainlength_1']
                    laser_d_act = (tr['laserontime'] - tr['inh_onset'])
                except ValueError:
                    laser_d, laser_i, laser_np, laser_d_act = 0, 0, 0, 0

                try:
                    conc = tr['odorconc']
                except ValueError:
                    conc = 0.

                trial = Trial(
                    session=self,
                    trial_num=tr['trialNumber'],
                    result=result,
                    valid=valid,
                    correct=correct,
                    odor=odor,
                    odorconc=conc,
                    laser_delay=laser_d,
                    laser_intensity=laser_i,
                    laser_npulses=laser_np,
                    laser_delay_actual=laser_d_act
                )

                trial.save()
        odorlist = list(odors)
        odorlist.sort()
        self.odors = str(odorlist)
        self.performance = ncorrects / nvalids
        self.trials_correct = ncorrects
        self.valid_trials = nvalids
        self.save()

    def odorset(self):
        return self.trial_set.values('odor').distinct()

    def lasers(self):
        ls = self.trial_set.values_list('laser_intensity', flat=True)
        return any(ls)

    def __str__(self):
        return "m: {0} s: {1}".format(self.mouse.mouse_number, self.run_dtg)

    # @transaction.atomic()
    def calc_inh_delay(self):
        basedir = '/experiment/raw_data/behavior/'
        import behavior_tools2 as bt
        sp = os.path.join(basedir, self.file.name)
        sess = bt.BehaviorSession(sp)
        a = bt.sniff.find_pre_inh_events(sess)
        self.exh_inh_delay = -int(a[1][a[1] < 500].mean())
        # raise Exception('hello')
        self.save()
        return


class Trial(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    trial_num = models.IntegerField('Trial Number')
    result = models.IntegerField('Result')
    valid = models.BooleanField('Valid')
    correct = models.BooleanField('Correct')
    odor = models.CharField('Odor', max_length=32)
    odorconc = models.FloatField('Odor concentration')
    laser_delay = models.IntegerField('Laser delay (ms)')
    laser_intensity = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='Laser intensity (mW)')
    laser_npulses = models.IntegerField('Number laser pulses')
    laser_delay_actual = models.IntegerField('Laser delay calculated', null=True, default=0)
    first_lick_rt = models.IntegerField('First lick reaction time', default=-1)
    first_lick_correct = models.BooleanField('First lick correct?', default=False)

    def __str__(self):
        return "Trial {}".format(self.trial_num)



