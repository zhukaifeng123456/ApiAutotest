'''
pytest脚本：
1、文件以test_开头
2、测试类以Test开头
3、测试函数或者方法以test_开头
'''

import requests
url = "http://jy001:8081/futureloan/mvc/api/member/register"

def test_regsiter_001():
    cs = {"mobilephone":18012345678,"pwd":123456}
    r = requests.post(url,data=cs)
    assert r.json()['code'] =='20110'
    assert r.json()['msg'] == "手机号码已被注册"

def test_regsiter_002():
    cs = {"mobilephone": 18012345678, "pwd": 123456}
    r = requests.post(url, data=cs)
    assert r.json()['msg'] == '手机号码已被注册'

def test_regsiter_003():
    cs = {"mobilephone": 18012345678}
    r = requests.post(url, data=cs)
    assert r.json()['msg'] == '密码不能为空'

