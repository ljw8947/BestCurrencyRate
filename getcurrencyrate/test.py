from models import CurrencyRate
from dbsession import DBSession,Base
from searcher.boc_searcher import BOCPriceSearcher
from datetime import datetime


#boc get data
bocSearch= BOCPriceSearcher()
bocData=bocSearch.getAllHistoryData()

session=DBSession.dbSession()
session.add_all(bocData)
session.commit()

result=session.query(CurrencyRate).all()
for item in result:
    print(item)
