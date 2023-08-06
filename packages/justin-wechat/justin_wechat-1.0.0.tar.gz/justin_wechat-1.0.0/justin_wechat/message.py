import json

import requests


class message:

    # 发送前的部门，人员，标签拼凑和检查
    @classmethod
    def touser_totag_toparty(cls, touser=None, totag=None, toparty=None):
        if touser is not None or totag is not None or toparty is not None:
            res = []

            if touser is not None:
                tousers = ""
                if len(touser) >= 2:
                    for x in touser:
                        tousers += x + "|"
                    tousers = tousers[0:-1]
                else:
                    tousers = touser[0]
                res.append(tousers)

            if totag is not None:
                totags = ""
                if len(totag) >= 2:
                    for x in totag:
                        totags += x + "|"
                    totags = totags[0:-1]
                else:
                    totags = totag[0]
                res.append(totags)

            if toparty is not None:
                topartys = ""
                if len(toparty) >= 2:
                    for x in toparty:
                        topartys += x + "|"
                    topartys = topartys[0:-1]
                else:
                    topartys = toparty[0]
                res.append(topartys)
            return res

        else:
            return None

    # 消息发送之后的返回值
    @classmethod
    def after_send_message(cls, send_message_url, send_message_data):
        send_message_res = json.loads(requests.post(url=send_message_url, data=send_message_data).content)
        res = {"invaliduser": send_message_res["invaliduser"],
               "invalidparty": send_message_res["invalidtag"],
               "invalidtag": send_message_res["invalidtag"],
               "msgid": send_message_res["msgid"],
               "response_code": send_message_res["response_code"]}
        return res

    # 文本消息
    @classmethod
    def send_text_message(cls, access_token, agentid, content, safe=None, enable_id_trans=None,
                          enable_duplicate_check=None, duplicate_check_interval=None,
                          touser=None, totag=None, toparty=None):
        send_text_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_text_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "text",
                "agentid": agentid,
                "text": {
                    "content": content
                },
                "safe": safe,
                "enable_id_trans": enable_id_trans,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_text_url, send_text_data)

    # 图片消息
    @classmethod
    def send_imaget_message(cls, access_token, agentid, media_id, safe=None,
                            enable_duplicate_check=None, duplicate_check_interval=None,
                            touser=None, totag=None, toparty=None):
        send_image_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_image_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "image",
                "agentid": agentid,
                "image": {
                    "media_id": media_id
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_image_url, send_image_data)

    # 语音消息
    @classmethod
    def send_voice_message(cls, access_token, agentid, media_id, safe=None,
                           enable_duplicate_check=None, duplicate_check_interval=None,
                           touser=None, totag=None, toparty=None):
        send_voice_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_voice_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "voice",
                "agentid": agentid,
                "voice": {
                    "media_id": media_id
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_voice_url, send_voice_data)

    # 视频消息
    @classmethod
    def send_video_message(cls, access_token, agentid, media_id, safe=None, title=None, description=None,
                           enable_duplicate_check=None, duplicate_check_interval=None,
                           touser=None, totag=None, toparty=None):
        send_video_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_video_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "video",
                "agentid": agentid,
                "video": {
                    "media_id": media_id,
                    "title": title,
                    "description": description
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_video_url, send_video_data)

    # 文件消息
    @classmethod
    def send_file_message(cls, access_token, agentid, media_id, safe=None,
                          enable_duplicate_check=None, duplicate_check_interval=None,
                          touser=None, totag=None, toparty=None):
        send_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_file_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "file",
                "agentid": agentid,
                "video": {
                    "media_id": media_id,
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_file_url, send_file_data)

    # 文本卡片消息
    @classmethod
    def send_textcard_message(cls, access_token, agentid, media_id, title, description, url, btntxt=None, safe=None,
                              enable_duplicate_check=None, duplicate_check_interval=None,
                              touser=None, totag=None, toparty=None):
        send_textcard_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_textcard_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "textcard",
                "agentid": agentid,
                "video": {
                    "media_id": media_id,
                    "title": title,
                    "description": description,
                    "url": url,
                    "btntxt": btntxt
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_textcard_url, send_textcard_data)

    # 图文消息
    @classmethod
    def send_news_message(cls, access_token, agentid, title, description, url=None, picurl=None, appid=None,
                          pagepath=None, safe=None, enable_duplicate_check=None, duplicate_check_interval=None,
                          touser=None, totag=None, toparty=None):
        send_news_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_news_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "news",
                "agentid": agentid,
                "news": {
                    "articles": [
                        {
                            "title": title,
                            "description": description,
                            "url": url,
                            "picurl": picurl,
                            "appid": appid,
                            "pagepath": pagepath,
                        }
                    ]
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_news_url, send_news_data)

    # 图文消息（mpnews）
    @classmethod
    def send_mpnews_message(cls, access_token, agentid, title, thumb_media_id, content, digest=None, author=None,
                            content_source_url=None, safe=None, enable_duplicate_check=None,
                            duplicate_check_interval=None,
                            touser=None, totag=None, toparty=None):
        send_mpnews_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_mpnews_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "mpnews",
                "agentid": agentid,
                "mpnews": {
                    "articles": [
                        {
                            "title": title,
                            "thumb_media_id": thumb_media_id,
                            "author": author,
                            "content_source_url": content_source_url,
                            "content": content,
                            "digest": digest
                        }
                    ]
                },
                "safe": safe,
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_mpnews_url, send_mpnews_data)

    # markdown消息
    @classmethod
    def send_markdown_message(cls, access_token, agentid, content, enable_duplicate_check=None,
                              duplicate_check_interval=None,
                              touser=None, totag=None, toparty=None):
        send_markdown_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        ttt = cls.touser_totag_toparty(touser, totag, toparty)
        if ttt:
            send_markdown_data = {
                "touser": ttt[0],
                "toparty": ttt[1],
                "totag": ttt[2],
                "msgtype": "markdown",
                "agentid": agentid,
                "markdown": {
                    "content": content
                },
                "enable_duplicate_check": enable_duplicate_check,
                "duplicate_check_interval": duplicate_check_interval
            }
            cls.after_send_message(send_markdown_url, send_markdown_data)
