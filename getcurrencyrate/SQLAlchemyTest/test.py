# 导入:
from sqlalchemy import Column, String, create_engine,FLOAT,VARCHAR,DATETIME,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlite3 import dbapi2 as sqlite

# 创建对象的基类:
Base = declarative_base()

class CurrencyRate(Base):
    __tablename__="getrate_currencyrate"

    rateID = Column(INTEGER(), primary_key=True)
    sourceCode = Column(String(20))
    currencyCode=Column(String(20))
    sellPrice=Column(FLOAT())
    buyPrice=Column(FLOAT())
    date=Column(DATETIME())
    createTime=Column(DATETIME())

    def __str__(self):
        return "rateID:%d souceCode:%s currencyCode:%s sellPrice:%d buyPrice:%d date:%s createTime:%s" % \
            (self.rateID,self.sourceCode,self.currencyCode,self.sellPrice,self.buyPrice,self.date,self.createTime)


# 初始化数据库连接:
engine = create_engine('sqlite+pysqlite:///G:\github\BestCurrencyRate\getcurrencyrate\db.sqlite3', module=sqlite)
# 创建DBSession类型:
dbSession = sessionmaker(bind=engine)


# 创建Session:
session = dbSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
c=session.query(CurrencyRate).first()
print(c)