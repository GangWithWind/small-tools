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

