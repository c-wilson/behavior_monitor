from django.db import models
from django.utils import timezone

STATUS_COLORS = {'Running': '#98FF98',
                 'Stopped': 'white',
                 'Paused': 'red'}

class Rig(models.Model):
    name = models.CharField('Rig', max_length=10)
    status = models.CharField('Status', max_length=10, blank=True, default='')
    non_responses = models.IntegerField('Number non-responses', blank=True, default=0)
    correct = models.IntegerField('Trials correct', blank=True, default=0)
    n_trials = models.IntegerField('Num Trials', blank=True, default=0)
    last_heartbeat = models.DateTimeField('Last heartbeat', blank=True, default=timezone.now)
    vnc_ip = models.URLField()
    miss_alerted = models.IntegerField('miss alert sent', default=0)
    pause1 = models.BooleanField('paused', default=False)
    pause_alerted = models.BooleanField('pause alert sent', default=False)

    def time_since_last(self):
        t = timezone.now() - self.last_heartbeat
        return "{0:0.0f}".format(t.total_seconds())

    def performance(self):
        try:
            p = self.correct / self.n_trials
        except ZeroDivisionError:
            p = 0.

        return "{0:0.2f}".format(p)

    def status_color(self):

        if int(self.time_since_last()) > 200 and not self.status == 'Stopped':
            return 'red'
        elif (float(self.performance()) < .4 or self.non_responses > 25) and not self.status == 'Stopped':
            return 'yellow'
        else:
            return STATUS_COLORS[self.status]

    def __str__(self):
        return 'Rig {0}'.format(self.name)


    def alert_poll(self, api):
        # api.update_status('rig {} polled'.format(self.name))
        if int(self.time_since_last()) > 200 and not self.status == 'Stopped' and not self.pause_alerted:
            api.update_status('rig {} paused!)'.format(self.name))
            self.pause_alerted = True
            self.save()
        elif self.non_responses > 25 and self.miss_alerted < 1:
            api.update_status('rig {}: 25 misses.'.format(self.name))
            self.miss_alerted = 1
            self.save()
        elif self.non_responses > 50 and self.miss_alerted < 2:
            api.update_status('rig {}: 50 misses!'.format(self.name))
            self.miss_alerted = 2
            self.save()
        elif self.non_responses > 100 and self.miss_alerted < 3:
            api.update_status('rig {}: 100 misses!'.format(self.name))
            self.miss_alerted = 3
            self.save()
        elif self.miss_alerted and self.non_responses < 25:
            self.miss_alerted = 0
            self.save()
        elif self.pause_alerted and int(self.time_since_last()) < 200:
            self.pause_alerted = False
            self.save()


    def reset(self):
        self.correct = 0
        self.non_responses = 0
        self.n_trials = 0
        self.status = ''
        self.miss_alerted = 0
        self.pause1 = False
        self.pause_alerted = False
        self.save()

