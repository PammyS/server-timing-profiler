from flask import request

from profile_manager import application


@application.after_request
def after_request(response):
    try:
        request_context = request.context
        if request_context:
            timing_list = []
            for key, val in request_context.iteritems():
                key = key.replace(' ', '-')
                timing = key + ';dur=' + str(val) + ';desc="' + key + '"'
                timing_list.append(timing)
            timings = ', '.join(timing_list)
            response.headers.set('Server-Timing', timings)
    except:
        pass
    return response