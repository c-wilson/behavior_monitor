import tweepy
from .models import Rig
from threading import Timer
from django.utils import timezone


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class BehaviorBot(object):
    _access_token = r'726055453181009920-pqOwxtOzCcbND7rTIZLHkZBGp7iNW38'
    _access_token_secret = r'xnFlLWmJdxveq6NCrGJVnXjTng4QnWwXIwlQwf90knJIn'
    _consumer_key = r'JJ0jyxpPhaKLhtax6ZvrRQsVs'
    _consumer_secret = r'H2VmXWARYEi4aIEZoMjCqRO2E6KyBUobZpZfJxSLrtrNF4vDbY'
    def __init__(self):

        try:
            self._auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
            self._auth.set_access_token(self._access_token, self._access_token_secret)
            self.twitter = tweepy.API(self._auth)
            # _ = self.twitter.update_status('BBot started {}.'.format(timezone.now()))
        except:
            return None
        return

    def update_status(self, string):
        _ = self.twitter.update_status('{0}\n{1}'.format(string, timezone.now())) #timezone.now()
        return

    def process_post(self, post):
        pass


class Alerter(object):
    def __init__(self):
        self.bbot = BehaviorBot()
        self.timer = RepeatedTimer(30, self.check_updates)

    def check_updates(self):
        for rig in Rig.objects.all():
            rig.alert_poll(self.bbot)
