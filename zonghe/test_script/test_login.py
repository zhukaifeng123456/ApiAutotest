import pytest


# def test_login():
#     #注册用户
#     #下发登录的请求
#     #检查结果
#     #删除注册的用户
#     pass
from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture()
def register(setup_data,url,db,baserequests):
    ##############1############
    mobilephone = setup_data['casedata']['mobilephone']
    # 初始化环境：删除注册有用户（数据库中可能有其他人测试的数据，与本用例冲突）
    Db.delete_user(db,mobilephone)
    #下发注册的请求
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    ############3##############
    #清理环境：删除注册的用户（在数据库中添加的数据，测试完成后没理掉）
    Db.delete_user(db, mobilephone)

def test_login2(url,register,baserequests,login_data):
    #############2##############
    print("下发登录的请求")
    r = Member.login(url, baserequests, login_data['casedata'])
    print("检查结果")
    # assert str(r.json()['code']) == str(login_data['expect']['code'])
    # assert str(r.json()['msg']) == str(login_data['expect']['msg'])
    # assert str(r.json()['status']) == str(login_data['expect']['status'])

    Asserts.check(r.json(),login_data['expect'],"code,msg,status")
