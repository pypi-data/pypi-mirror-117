import json
import requests


class customer:
    # 获取客户列表,返回的是 id
    @classmethod
    def get_externalcontact(cls, access_token, user_id):
        externalcontact_url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list?" \
                              f"access_token={access_token}&userid={user_id}"
        externalcontact_res = json.loads(requests.get(url=externalcontact_url).content)
        if externalcontact_res["errcode"] == 0:
            return externalcontact_res["external_userid"]

    # 获取客户详情
    @classmethod
    def get_externalcontact_details(cls, access_token, external_userid, cursor=None):
        externalcontact_details_url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/" \
                                      f"get?access_token={access_token}&" \
                                      f"external_userid={external_userid}&" \
                                      f"cursor={cursor}"

        externalcontact_details_res = json.loads(requests.get(url=externalcontact_details_url).content)
        if externalcontact_details_res["errcode"] == 0:
            return externalcontact_details_res["external_contact"]
        else:
            return externalcontact_details_res["errmsg"]

    # 批量获取客户详情
    @classmethod
    def get_batchexternalcontact(cls, access_token, userid_list, cursor=None, limit=None):
        batchexternalcontact_url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/batch/get_by_user?" \
                                   f"access_token={access_token}"
        batchexternalcontact_data = {
            "userid_list": userid_list,
            "cursor": cursor,
            "limit": limit
        }
        batchexternalcontact_res = json.loads(requests.post(url=batchexternalcontact_url,
                                                            data=batchexternalcontact_data).content)
        if batchexternalcontact_res["errcode"] == 0:
            return batchexternalcontact_res["external_contact_list"]
        else:
            return batchexternalcontact_res["errmsg"]
