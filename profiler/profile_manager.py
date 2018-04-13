from flask import request
import datetime
application = None


class ProfileManager():

    def __init__(self, app, mode):
        global application
        self.app = app
        application = app
        if mode.lower() == 'debug':
            import add_headers

    def start(self, key):
        start_time = datetime.datetime.now()
        ctx = None
        try:
            ctx = request.context
        except:
            ctx = {}

        ctx[key] = {'start': start_time}
        request.context = ctx

    def stop(self, key):
        stop_time = datetime.datetime.now()
        try:
            ctx = request.context
            if ctx and key in ctx:
                data = ctx.get(key, {})
                start_time = data.get('start')
                if start_time:
                    diff = stop_time - start_time
                    millis = diff.total_seconds()*1000
                    ctx[key] = millis
        except:
            pass