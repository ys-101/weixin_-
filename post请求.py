# 这里的"User-Agent"最好为手机浏览器的标识
headers = {
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
}

# 添加data，`req_id`、`pass_ticket`。
data = {
    "is_only_read": "1",
    "is_temp_url": "0",
    "appmsg_type": "9",
    'reward_uin_count': '0'
}
# link文章链接去微信公众号平台抓包获取。
mid = link.split("&")[1].split("=")[1]
idx = link.split("&")[2].split("=")[1]
sn = link.split("&")[3].split("=")[1]
_biz = link.split("&")[0].split("_biz=")[1]


# 根据获取到的参数，构造PSOT请求的params
params = {
    "__biz": _biz,
    "mid": mid,
    "sn": sn,
    "idx": idx,
    "key": key,
    "pass_ticket": pass_ticket,
    "appmsg_token": appmsg_token,
    "uin": uin,
    "wxtoken": "777",
}
# post请求提交后，将返回的respone转为json
# 获取阅读量点赞数
json = requests.post(url, headers=headers, data=data, params=params).json()