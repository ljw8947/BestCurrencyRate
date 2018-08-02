from models import CurrencyRate
from dbsession import DBSession,Base
from searcher.boc_searcher import BOCPriceSearcher
from searcher.cmb_searcher import CMBPriceSearcher
from searcher.travelex_searcher import TravelexPriceSearcher
from datetime import datetime


#boc get data
bocSearch= TravelexPriceSearcher()
bocData=bocSearch.getAllHistoryData()

session=DBSession.dbSession()
session.add_all(bocData)
session.commit()

result=session.query(CurrencyRate).all()
for item in result:
    print(item)
