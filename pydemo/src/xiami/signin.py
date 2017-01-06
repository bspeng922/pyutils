# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import time
import cookielib


sign_url = "http://www.xiami.com/task/signin"
sign_method = "post"

logout_url = "http://www.xiami.com/member/logout"
login_url = "https://login.xiami.com/member/login"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36 Vivaldi/1.5.658.56"
headers = {'User-Agent': user_agent}


def login(account, pw):
    def get_page():
        resp = requests.get(login_url, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        login_tag = soup.find("div", id="xiami-login")
        xiamitoken = login_tag.select("input[name='_xiamitoken']")[0]['value']
        done = login_tag.find('input', {'name': 'done'})['value']
        submit = login_tag.find('input', {'name': 'submit'})['value']

        return {'account': account,
                'pw': pw,
                # 'from': 'web',
                'verifycode': '',
                # 'havanaId': '',
                'submit': submit,
                '_xiamitoken': xiamitoken,
                'done': done}

    post_data = get_page()
    sess = requests.session()
    resp = sess.post(login_url, data=post_data, headers=headers)
    print resp.cookies
    # print resp.cookies

    resp = sess.post(sign_url, headers=headers)
    print resp
    # print resp.content
    #
    # resp = requests.get("http://www.xiami.com/space/lib-song", headers=headers)
    # print resp.content



def main():
    account = "852354673@qq.com"
    pw = "TjFH5aS4tGjnskk"
    login(account, pw)


if __name__ == "__main__":
    main()
