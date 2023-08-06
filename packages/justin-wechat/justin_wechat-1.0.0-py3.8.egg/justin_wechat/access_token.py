import json
import requests


class AccessToken:
    @classmethod
    def get_accesstoken(cls, corpid, corpsecret):
        accesstoken_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        accesstoken_data = json.loads(requests.get(url=accesstoken_url).content)
        if accesstoken_data["errcode"] == 0:
            return accesstoken_data["access_token"]
        else:
            return accesstoken_data["errmsg"]
