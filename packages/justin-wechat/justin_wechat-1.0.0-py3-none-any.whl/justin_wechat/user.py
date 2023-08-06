import json
import requests
import department


class user:

    # 获取活跃成员数量
    @classmethod
    def get_active_users(cls, access_token):
        activeusers_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat?access_token={access_token}"
        activeusers_res = json.loads(requests.post(url=activeusers_url).content)
        if activeusers_res["errcode"] == 0:
            return activeusers_res["active_cnt"]
        else:
            return activeusers_res["errmsg"]

    # 获取加入企业二维码
    @classmethod
    def get_join_qrcode(cls, size_type, access_token):
        size_types = {1: "171 x 171", 2: "399 x 399", 3: "741 x 741", 4: "2052 x 2052"}
        if size_type in size_types:
            get_join_qrcode_url = f" https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode?access_token=" \
                                  f"{access_token}&size_type={size_types[size_type]}"
            get_join_qrcode_res = json.loads(requests.get(url=get_join_qrcode_url).content)
            if get_join_qrcode_res["errcode"] == 0:
                return get_join_qrcode_res["join_qrcode"]
            else:
                return get_join_qrcode_res["errmsg"]
        else:
            return "Qrcode size type incorrect."

    # 邀请成员
    @classmethod
    def invite_users(cls, access_token, user=None, party=None, tag=None):
        if (type(user) is list or None) and (type(party) is list or None) and (type(tag) is list or None):
            invite_url = f"https://qyapi.weixin.qq.com/cgi-bin/batch/invite?access_token={access_token}"
            invite_data = {
                "user": user,
                "party": party,
                "tag": tag
            }
            return json.loads(requests.post(url=invite_url, data=invite_data).content)["errmsg"]
        else:
            return "type of user, party and tag must be list or None"

    # 二次验证
    @classmethod
    def authsucc(cls, access_token, userid):
        authsucc_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/authsucc?access_token=" \
                       f"{access_token}&userid={userid}"
        return json.loads(requests.get(url=authsucc_url).content)["errmsg"]

    # userid与openid互换
    @classmethod
    def convert_openid_userid(cls, access_token, convert_id, convert):
        # 0:userid转openid; 1:openid转userid
        if convert == 0:
            convert_to_openid_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid?access_token=" \
                                    f"{access_token}"
            convert_to_openid_data = {
                "userid": convert_id
            }
            convert_to_openid_res = json.loads(
                requests.post(url=convert_to_openid_url, data=convert_to_openid_data).content)
            if convert_to_openid_res["errcode"] == 0:
                return convert_to_openid_res["openid"]
            else:
                return convert_to_openid_res["errmsg"]
        elif convert == 1:
            convert_to_userid_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_userid?access_token=" \
                                    f"{access_token}"
            convert_to_userid_data = {
                "openid": convert_id
            }
            convert_to_userid_res = json.loads(
                requests.post(url=convert_to_userid_url, data=convert_to_userid_data).content)
            if convert_to_userid_res["errcode"] == 0:
                return convert_to_userid_res["userid"]
            else:
                return convert_to_userid_res["errmsg"]
        else:
            return "0:Convert userid to openid; 1:Convert openid to userid."

    # 获取部门成员详情
    @classmethod
    def get_department_users_details(cls, access_token, deparment_id, fetch_child=0):
        # fetch_child : 1/0：是否递归获取子部门下面的成员
        get_department_users_details_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/list?" \
                                           f"access_token={access_token}&" \
                                           f"department_id={deparment_id}&fetch_child={fetch_child}"
        get_department_users_details_res = json.loads(requests.get(url=get_department_users_details_url).content)
        if get_department_users_details_res["errcode"] == 0:
            return get_department_users_details_res["userlist"]
        else:
            return get_department_users_details_res["errmsg"]

    #  获取部门成员
    @classmethod
    def get_department_users(cls, access_token, deparment_id, fetch_child=0):
        # fetch_child : 1/0：是否递归获取子部门下面的成员
        get_department_users_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?" \
                                   f"access_token={access_token}&" \
                                   f"department_id={deparment_id}&" \
                                   f"fetch_child={fetch_child}"
        get_department_users_res = json.loads(requests.get(url=get_department_users_url).content)
        if get_department_users_res["errcode"] == 0:
            return get_department_users_res["userlist"]
        else:
            return get_department_users_res["errmsg"]

    # 批量删除成员 和 单个删除成员
    @classmethod
    def batchdelete_users(cls, access_token, userid):
        if type(userid) is list:
            batchdelete_users_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token={access_token}"
            batchdelete_users_data = {
                "useridlist": userid
            }
            batchdelete_users_res = json.loads(requests.post(url=batchdelete_users_url,
                                                             data=batchdelete_users_data).content)
            return batchdelete_users_res["errmsg"]
        else:
            delete_users_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}" \
                               f"&userid={userid}"
            return json.loads(requests.get(url=delete_users_url).content)["errmsg"]

    # 更新成员
    def update_user(self):
        pass

    # 读取成员
    @classmethod
    def get_user(cls, access_token, userid):
        get_user_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}" \
                       f"&userid={userid}"
        get_user_res = json.loads(requests.get(url=get_user_url).content)
        if get_user_res["errcode"] == 0:
            return get_user_res
        else:
            return get_user_res["errmsg"]

    # 创建成员
    def create_user(self):
        pass

    # 一步获取全部成员
    @classmethod
    def get_allusers(cls, access_token, details=True, is_fetch_child=0):
        # details 为 true，获取详情，未 false 获取简单信息
        # fetch_child = 0 不递归， fetch_child = 1 递归
        # 获取所有部门ID
        departments = department.department.get_departments(access_token)
        department_ids = []

        for d in departments:
            department_ids.append(d["id"])

        for department_id in department_ids:
            if details:
                return cls.get_department_users_details(department_id, is_fetch_child)
            else:
                return cls.get_department_users(department_id, is_fetch_child)
