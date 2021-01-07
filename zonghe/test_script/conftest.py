'''
脚本层的一些公共方法
'''
#########################################
'''
python导入包的规则
1、安装目录找包
2、如果使用IDE:当前工程路径、当前执行文件所在路径、python安装目录下找包。
3、命令行执行时：从当前执行文件路径、python安装目录下找包。
命令执行时，报错找不到包。解决办法：把工程路径，放到sys.path中。
'''
import sys
import os
print(sys.path)
cp = os.path.realpath(__file__)
cd = os.path.dirname(cp)
cd = os.path.dirname(cd)
cd = os.path.dirname(cd)
sys.path.append(cd)
#print(sys.path)
##########################################

import pytest


from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

env_path = r"data_env\env.ini"


@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path, "url")


@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path, "db"))


@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()
