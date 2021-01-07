

import requests

# sign_001验证用户使用合法的手机号、密码，昵称为空，注册成功
# {"status":"1","code":"10001","data": "msg": "成功"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15006007018","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"

# sign_002验证用户使用合法的手机号、密码、昵称，注册成功
# {"status":"1","code":"10001","data": "msg": "成功"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15006008107","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"

# sign_003验证用户使用合法的手机号、密码，昵称为空，注册失败，服务器异常
# {"status":"0","code":"20102","data": "msg": "服务器异常"}



# sign_004验证用户使用合法的手机号码，昵称、密码为空，注册失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15006008107","pwd":""}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码不能为空"

# sign_005验证用户手机号码、昵称为空，密码合法，注册失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# sign_006验证用户手机号码、密码、昵称为空，注册失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":""}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# sign_007验证用户使用合法的手机号码、昵称，密码为空，注册失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18006007167","pwd":"","regname":'丫丫'}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码不能为空"

# sign_008验证用户手机号码为空，密码、昵称合法，注册失败
# {"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":"aaa84758","regname":'wawa'}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# sign_009验证用户使用合法的手机号码，密码输入5位，注册失败
# {"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18006007167","pwd":"12345"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"

# sign_010验证用户使用合法的手机号码，密码输入3位，注册失败
# {"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18006007167","pwd":"123"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"

# sign_011验证用户使用合法的手机号码，密码输入19位，注册失败
# {"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18006007167","pwd":"1231231231231212312"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"

# sign_012验证用户使用长度为1的手机号码，注册失败
# {"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"1","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# sign_013验证用户使用长度为6的手机号码，注册失败
# {"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"123456","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# sign_014验证用户使用长度为10的手机号码，注册失败
# {"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"1234567890","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# sign_015验证用户使用长度为12的手机号码，注册失败
# {"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"12345678941012","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# sign_016验证用户使用长度为11的不合法手机号码，注册失败
# {"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"11111111111","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# sign_017验证用户使用已注册的手机号码，注册失败
# {"status":"0","code":"20110","data": "msg": "手机号码已被注册"}
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15006007018","pwd":"123456"}
r= requests.post(url,data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"

