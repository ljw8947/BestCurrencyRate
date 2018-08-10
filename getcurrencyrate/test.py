from models import CurrencyRate
from dbsession import DBSession,Base
from searcher.boc_searcher import BOCPriceSearcher
from searcher.cmb_searcher import CMBPriceSearcher
from searcher.travelex_searcher import TravelexPriceSearcher
from datetime import datetime


session=DBSession.dbSession()
result=session.query(CurrencyRate)[:100]
print(str(result))
