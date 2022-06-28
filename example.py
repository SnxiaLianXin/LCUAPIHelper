import psutil
import base64
import requests


class LoLHelper:
    port = str
    token = str
    author = dict

    def __init__(self, port: str, token: str):
        self.port = port
        self.token = token
        tokens = base64.b64encode(("riot:%s" % token).encode())
        self.author = { "Authorization":"Basic %s" % tokens.decode() }

    def get(self, api: str):
        result = requests.get(
            url = ("https://127.0.0.1:%s%s" % (self.port, correct(api))),
            headers = self.author,
            verify = False
        )
        if result.status_code == 200:
            try:
                result.encoding = "utf-8"
                return result.text
            finally:
                result.close()
        else:
            return ""

    def post(self, api: str, data: str):
        result = requests.post(
            url = "https://127.0.0.1:%s%s" % (self.port, correct(api)),
            headers = self.author,
            verify = False,
            json = data
        )
        if result.status_code == 200:
            try:
                result.encoding = "utf-8"
                return result.text
            finally:
                result.close()
        else:
            return ""

    def patch(self, api: str, data: str):
        result = requests.patch(
            url = "https://127.0.0.1:%s%s" % (self.port, correct(api)),
            headers = self.author,
            verify = False,
            json = data
        )
        if result.status_code == 200:
            try:
                result.encoding = "utf-8"
                return result.text
            finally:
                result.close()
        else:
            return ""

    def put(self, api: str, data: str):
        result = requests.put(
            url = "https://127.0.0.1:%s%s" % (self.port, correct(api)),
            headers = self.author,
            verify = False,
            json = data
        )
        if result.status_code == 200:
            try:
                result.encoding = "utf-8"
                return result.text
            finally:
                result.close()
        else:
            return ""
    
    def delete(self, api: str):
        return requests.delete(
            url = "https://127.0.0.1:%s%s" % (self.port, correct(api)),
            headers = self.author,
            verify = False
        ).status_code


def correct(api:str):
    if api[0] != "/":
        return "/%s" % api
    return api


def checkProcessAlive(processName: str):
    for x in psutil.process_iter():
        if x.name().removesuffix(".exe") == processName:
            return True
    return False


def init():
    port = str
    token = str
    cmds = list[str]
    for process in psutil.process_iter():
        if process.name().removesuffix(".exe") == "LeagueClientUx":
            cmds = process.cmdline()
            break
    for cmd in cmds:
        ary = cmd.split("=")
        if ary[0] == "--remoting-auth-token":
            token = ary[1]
        if ary[0] == "--app-port":
            port = ary[1]
    return LoLHelper(port, token)


if checkProcessAlive("LeagueClient"):
    # 初始化LOLHelper类
    lHelper = init()
    # 获取当前召唤师信息
    print(lHelper.get("lol-summoner/v1/current-summoner"))
    # 获取当前召唤师生涯信息
    # print(lHelper.get("lol-summoner/v1/current-summoner/summoner-profile"))
    # 设置生涯背景图片
    # lHelper.post("lol-summoner/v1/current-summoner/summoner-profile",{"key":"backgroundSkinId","value":"1000"})
else:
    print("未检测到游戏进程，请先运行游戏")
