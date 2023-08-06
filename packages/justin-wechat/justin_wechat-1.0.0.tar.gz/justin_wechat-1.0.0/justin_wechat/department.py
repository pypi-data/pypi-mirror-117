import json
import requests


class department:
    # 获取部门列表
    @classmethod
    def get_departments(cls, access_token, department_id=None):
        if department_id is not None:
            department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=" \
                             f"{access_token}&id={department_id} "
        else:
            department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={access_token}&id="
        deparment_data = json.loads(requests.get(url=department_url).content)
        if deparment_data["errcode"] == 0:
            return deparment_data["department"]
        else:
            return deparment_data["errmsg"]

    # 删除部门
    @classmethod
    def del_departments(cls, access_token, department_ids):
        deldepartments_res = []
        if department_ids:
            for department_id in department_ids:
                deldepartment_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=" \
                                    f"{access_token}&id={department_id}"
                deldepartment_data = json.loads(requests.get(url=deldepartment_url).content)
                deldepartments_res.append((deldepartments_res, deldepartment_data["errmsg"]))
            return deldepartments_res
        else:
            return "Department id is null"

    # 更新部门
    @classmethod
    def update_department(cls, access_token, department_id, name=None, name_en=None, parentid=None, order=None):
        updatedepartment_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=" \
                               f"{access_token}"
        updatedepartment_data = {
            "id": department_id,
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order
        }
        return json.loads(requests.post(url=updatedepartment_url, data=updatedepartment_data).content)["errmsg"]

    # 创建部门
    @classmethod
    def create_department(cls, access_token, name, parentid, department_id=None, name_en=None, order=None):
        createdepartment_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=" \
                               f"{access_token}"
        createdepartment_data = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": department_id
        }
        return json.loads(requests.post(url=createdepartment_url,data=createdepartment_data).content)["errmsg"]
