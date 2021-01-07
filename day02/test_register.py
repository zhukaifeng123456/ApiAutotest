import pytest
import requests


# 登录功能的测试数据,列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{"mobilephone": 15006008107, "pwd": 123456,"msg":"手机号码已被注册"},
                        {"mobilephone": 15006008107, "pwd": "","msg":"密码不能为空"}])
def register_data(request):  # request是pytest中的关键字，固定写法
    return request.param  # 通过request.param返回每一组数据，固定写法


def test_register(register_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为:{register_data}")
    r = requests.post(url, data=register_data)
    assert r.json()['msg'] == register_data['msg']


#####################################################################################################
@pytest.fixture(params=[{"data":{"mobilephone": 15006008107, "pwd": 123456},
                                 "expect":{"status":0,"code":"20110","data":None,"msg":"手机号码已被注册"}},
                        {"data":{"mobilephone": 15006008107, "pwd": 1234},
                                 "expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}}])
def register_data1(request):  # request是pytest中的关键字，固定写法
    return request.param  # 通过request.param返回每一组数据，固定写法

def test_register1(register_data1):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为:{register_data1['data']}")
    r = requests.post(url, data=register_data1['data'])
    print(r.text)
    assert r.json()['msg'] == register_data1['expect']['msg']
    assert r.json()['status'] == register_data1['expect']['status']
    assert r.json()['code'] == register_data1['expect']['code']


