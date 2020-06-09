import sys
sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB
# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event':[
        {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-06-08 10:00:00'},
        {'id':2,'name':'橙米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-06-08 10:00:00'},
        {'id':3,'name':'黄米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-06-08 10:00:00'},
        {'id':4,'name':'绿米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-06-08 10:00:00'},
        {'id':5,'name':'青米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-06-08 10:00:00'},
    ],
    # 嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'alen','phone':'12345678901','email':'alen@email.com','sign':0,'event_id':1},
        {'id':2,'realname':'has sign','phone':'12345678901','email':'alen@email.com','sign':1,'event_id':1},
        {'id':3,'realname':'Tom','phone':'12345678901','email':'alen@email.com','sign':0,'event_id':5},
    ],
}

# 将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()