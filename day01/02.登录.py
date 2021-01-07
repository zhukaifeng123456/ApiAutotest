

import requests

# login_001验证用户输入合法的手机号码、密码，登录成功
# {"status":"1","code":"10001","data": "msg": "成功"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"18012345678","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "登录成功"

# login_002验证用户输入合法的手机号码、密码，服务器异常
# {"status":"0","code":"20102","data": "msg": "服务器异常"}


# login_003验证用户输入合法的手机号码，密码为空，登录失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"15006007018","pwd":""}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码不能为空"

# login_004验证用户输入合法的密码，手机号码为空，登录失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"","pwd":"abc1234"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# login_005验证手机号、密码为空，登录失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"","pwd":""}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# login_006验证输入未注册的手机号，登录失败
# {"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"15871034161","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == ""

# login_007验证输入长度不合法的手机号，登录失败
# {"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"123","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# login_008验证输入合法的手机号码，密码不合法，登录失败
# {"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"15006007018","pwd":"12345"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"

# login_009验证输入已注册的手机号码，密码错误，登录失败
# {"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone":"15006007018","pwd":"1258868"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"
