
import requests
import time
import json
import smtplib
import socket
from email.mime.text import MIMEText

# TODO add some docstring
# TODO automatically start
# TODO exceptions clearfy
# TODO document

with open('local.ini', 'r') as fid:
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
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fid.write('{0}\t{1}\n'.format(now, info))


def netlog():
    try:
        r = requests.post(login_url, data = data)
        rjs = json.loads(r.text.replace("'", '"'))
        if rjs['success']:
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    old_ip =  get_ip_by_prefix(pars["ip_prefix"])
    writelog('start ip {0}'.format(old_ip))
    old_ip = ''

    while True:
        isconnect = check_connection()

        if not isconnect:
             writelog('re-login...')
             if  netlog():
                writelog('done')
                time.sleep(2)
                now_ip = get_ip_by_prefix(pars["ip_prefix"])
                if now_ip != old_ip:
                    send_ip_by_email(now_ip)
                    old_ip = now_ip
                    writelog('send ip {0}'.format(old_ip))
             else:
                writelog('error')

        time.sleep(sleep)