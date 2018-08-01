from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlite3 import dbapi2 as sqlite
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类:
Base = declarative_base()

class DBSession:
    # 初始化数据库连接:
    __engine__ = create_engine('sqlite:///rate.db',echo=True)
    # 创建DBSession类型:
    dbSession = sessionmaker(bind=__engine__)