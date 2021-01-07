'''
fixture 带参数
'''

import pytest

# 登录功能的测试数据
@pytest.fixture(params=[{"mobilephone":18012345678,"pwd":123456},
                        {"mobilephone":18012345678,"pwd":12345},
                        {"mobilephone":18012345678,"pwd":""},
                        {"mobilephone":178,"pwd":123456}])
def login_data(request): #request是pytest中的关键字，固定写法
    return request.param # 通过request.param返回每一组数据，固定写法

# 数据驱动测试
# 登录功能的脚本测试
def test_login(login_data):
    print(f"登录功能,测试数据为：{login_data}")
    print(f"手机号：{login_data['mobilephone']}")
    print(f"密码：{login_data['pwd']}")