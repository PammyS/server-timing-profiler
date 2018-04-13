from flask import Flask, jsonify
import time
from profiler.profile_manager import ProfileManager

app = Flask(__name__)

profiler = ProfileManager(app, 'debug')


@app.route("/test", methods=["GET"])
def hello():
    print 'test start sleep'

    profiler.start('App 1')
    time.sleep(1)
    profiler.stop('App 1')

    profiler.start('App 2')
    time.sleep(2)
    profiler.stop('App 2')

    profiler.start('App 3')
    time.sleep(3)
    profiler.stop('App 3')

    profiler.start('App 4')
    time.sleep(4)
    profiler.stop('App 4')

    print 'test stop sleep'
    return jsonify({'success':True})

app.run(host="0.0.0.0",port=8080,debug=True)