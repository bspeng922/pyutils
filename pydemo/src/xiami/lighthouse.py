import json
import requests

login_url = 'https://www.light-house.cc/auth/login'
checkin_url = 'https://www.light-house.cc/user/checkin'
conf_url = 'https://www.light-house.cc/user/getpcconf'
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
headers = {'User-Agent': user_agent}
folder = "D:\\"


def login(email, passwd):
    post_data = {'email': email,
                 'passwd': passwd}
    resp = requests.post(login_url, data=post_data, headers=headers)
    return resp.cookies


def save_configure(cookies, path):
    # get ss configure file and save to file
    conf_resp = requests.get(conf_url, cookies=cookies, headers=headers)
    with open(path, 'wb') as f:
        f.write(conf_resp.content)


def checkin(cookies):
    # check in after login successfully
    resp = requests.post(checkin_url, cookies=cookies, headers=headers)
    content = json.loads(resp.content)
    # if content.get("ret") == 1:
    #     print "OK"
    print content['msg']


def main():
    email = ''
    passwd = ''
    if not email:
        email = raw_input("Input you email address: ")
    if not passwd:
        passwd = raw_input("Input password: ")
    _cookies = login(email, passwd)

    if _cookies:
        print "login successfully !  ----   email: {email} - " \
              "password: {password}".format(email=email, password=passwd)
        save_path = "{folder}{name}{ext}".format(folder=folder,
                                                 name=email.split("@")[0],
                                                 ext='.json')
        # save_configure(_cookies, save_path)
        checkin(_cookies)
    print "Error: email or password error ."


if __name__ == "__main__":
    main()
