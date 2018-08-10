from sqlalchemy import Column, String, create_engine,FLOAT,VARCHAR,DATETIME,INTEGER
from sqlalchemy.ext.declarative import declarative_base
from .dbsession import Base
from datetime import datetime

class CurrencyRate(Base):
    __tablename__="currencyRate"

    rateID = Column(INTEGER(), primary_key=True,comment="key")
    sourceCode = Column(String(20),comment="数据源")
    currencyCode=Column(String(20),comment="币种代码")
    sellPrice=Column(FLOAT(),comment="售汇价")
    buyPrice=Column(FLOAT(),comment="结汇价")
    date=Column(DATETIME(),comment="生效日期")
    createTime=Column(DATETIME(),comment="创建日期")

    def __init__(self,souceCode='',currencyCode='',sellPrice=0,buyPrice=0,date=datetime.today()):
        self.sourceCode=souceCode
        self.currencyCode=currencyCode
        self.sellPrice=sellPrice
        self.buyPrice=buyPrice
        self.date=date
        self.createTime=datetime.now()

    def __str__(self):
        return "rateID:%s souceCode:%s currencyCode:%s sellPrice:%s buyPrice:%s date:%s createTime:%s" % \
            (self.rateID,self.sourceCode,self.currencyCode,\
                self.sellPrice,self.buyPrice,self.date,self.createTime)