import requests
import time
import json

#

data = {"opr": "pwdLogin",
"userName": "zhaogang",
"pwd": "123456",
"rememberPwd": "1"
}

login_url = "http://1.1.1.3/ac_portal/login.php"
check_url = "http://www.baidu.com"
sleep = 10


def check_connection():
    try:
        q =  requests.get(check_url)
        if ("1.1.1" not in q.url ): #will redirect to 1.1.1.3 if not connect to internet
            return True
        else:
            return False
    except:
        return False

def writelog(info):
    with open('/home/gzhao/GitHub/mytools/netlogin/netlogin.log', 'a') as fid:
        # TODO: 地址写入ini文件
        now = time.strftime('%Y-%m-%d %H:%M:%s', time.localtime(time.time()))
        fid.write('%s\t%s\n'%(now,info))
        # TODO: 日期的秒数显示太长

if __name__ == "__main__":
    writelog('start')
    while True:
        isconnect = check_connection()

        if not isconnect:
            writelog('re-login...')
            r = requests.post(login_url, data = data)
            rjs = json.loads(r.text.replace("'",'"'))
            if not rjs['success']:
                writelog('error')
                break
            writelog('done')
        time.sleep(sleep)

# TODO FIXIT
""" File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connection.py", line 159, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/util/connection.py", line 80, in create_connection
    raise err
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/util/connection.py", line 70, in create_connection
    sock.connect(sa)
OSError: [Errno 101] Network is unreachable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connectionpool.py", line 354, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/home/gzhao/anaconda3/lib/python3.7/http/client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/home/gzhao/anaconda3/lib/python3.7/http/client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/home/gzhao/anaconda3/lib/python3.7/http/client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/home/gzhao/anaconda3/lib/python3.7/http/client.py", line 1016, in _send_output
    self.send(msg)
  File "/home/gzhao/anaconda3/lib/python3.7/http/client.py", line 956, in send
    self.connect()
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connection.py", line 181, in connect
    conn = self._new_conn()
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connection.py", line 168, in _new_conn
    self, "Failed to establish a new connection: %s" % e)
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7fa38ef43c50>: Failed to establish a new connection: [Errno 101] Network is unreachable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/connectionpool.py", line 638, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/urllib3/util/retry.py", line 399, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='1.1.1.3', port=80): Max retries exceeded with url: /ac_portal/login.php (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fa38ef43c50>: Failed to establish a new connection: [Errno 101] Network is unreachable'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gzhao/GitHub/mytools/netlogin/netlogin.py", line 39, in <module>
    writelog('re-login...')
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/api.py", line 116, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/home/gzhao/anaconda3/lib/python3.7/site-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='1.1.1.3', port=80): Max retries exceeded with url: /ac_portal/login.php (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fa38ef43c50>: Failed to establish a new connection: [Errno 101] Network is unreachable'))
"""