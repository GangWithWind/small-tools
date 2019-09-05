
import requests
import time
import json
import smtplib
import socket
from email.mime.text import MIMEText

with open('pars.ini', 'r') as fid:
    pars = json.load(fid)

data = {"opr": "pwdLogin",
        "userName": pars['net_name'],
        "pwd": pars["net_pwd"],
        "rememberPwd": "1",
        }

login_url = "http://1.1.1.3/ac_portal/login.php"
check_url = "http://www.baidu.com"
sleep = pars.get('sleep', 10)


def send_ip_by_email(ip_address):
    msg = MIMEText('ip_address change to: {0}'.format(ip_address),
                   'plain', 'utf-8')
    sender = pars['email_name']
    password = pars['email_pwd']
    smtp_server = pars['email_host']
    msg['From'] = sender
    msg['To'] = sender
    msg['Subject'] = 'ip address'
    server = smtplib.SMTP(smtp_server, 25)
    server.login(sender, password)
    server.sendmail(sender, msg['To'], msg.as_string())
    server.quit()


def get_ip_by_prefix(prefix):
    localIP = ''
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if ip.startswith(prefix):
            localIP = ip
    return localIP


def check_connection():
    try:
        q = requests.get(check_url)
        if ("1.1.1" not in q.url):
            # will redirect to 1.1.1.3 if not connect to internet
            return True
        else:
            return False
    except:
        return False


def writelog(info):
    with open('netlogin.log', 'a') as fid:
        # TODO: 地址写入ini文件
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fid.write('{0}\t{1}\n'.format(now, info))


if __name__ == "__main__":
    old_ip = ''
    writelog('start: ip = {0}'.format(old_ip))

    while True:
        isconnect = check_connection()

        if not isconnect:
            writelog('re-login...')
            r = requests.post(login_url, data = data)
            rjs = json.loads(r.text.replace("'", '"'))
            if not rjs['success']:
                writelog('error')
                time.sleep(sleep)
            else:
                writelog('done')
                sleep(2)
                now_ip = get_ip_by_prefix(pars["ip_prefix"])
                if now_ip != old_ip:
                    send_ip_by_email(now_ip)
                    old_ip = now_ip
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