# HTTP Server-Timing for Python Flask
  * Installation
  ```
    pip install server-timing-profiler
   ```
This is a library including middleware for using
[HTTP Server-Timing](https://www.w3.org/TR/server-timing) with Python. This header
allows a server to send timing information from the backend, such as database
access time, file reads, etc. The timing information can be then be inspected
in the standard browser developer tools:

![Server Timing Example](https://github.com/PammyS/server-timing-profiler/blob/master/example/ScreenShot.png)

## Features

  * Middleware for injecting the server timing into the request `Context`
    and writing the `Server-Timing` header.

  * Concurrency-safe structures for easily recording timings of multiple
    concurrency tasks.

  * Parse `Server-Timing` headers as a client.

  * Note: No browser properly supports sending the Server-Timing header as
    an [HTTP Trailer](https://tools.ietf.org/html/rfc7230#section-4.4) so
	the Middleware only supports a normal header currently.

## Browser Support

Browser support is required to **view** server timings easily. Because server
timings are sent as an HTTP header, there is no negative impact to sending
the header to unsupported browsers.

  * **Chrome 65 or higher** is required to properly display server timings
    in the devtools.

## Usage

Example usage is shown below. A fully runnable example is available in
the `example/` directory.

```python
from flask import Flask, jsonify
import time

# Import ProfileManager
from profiler.profile_manager import ProfileManager

app = Flask(__name__)
'''
Bind you app object with ProfileManager and pass app object along with 'debug' mode to enable the
result in reposne headers. If PROD or DEV is set you will not get stats in reponse to make sure
even if you miss to comment this code in prod, it will not affect your application
'''
profiler = ProfileManager(app, 'debug')


@app.route("/test", methods=["GET"])
def hello():
    print 'test start sleep'

    '''
    To profile any code snippet or call to external services , 
    call the start with a unique key and after the code snippet call stop function. 
    Also make sure to add call stop function [profiler.stop('<key>')]  with the same
    key you started with, otherwise status will not be reflect.
    '''
    
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
```
Note: Recommended not to enable this in production environment
