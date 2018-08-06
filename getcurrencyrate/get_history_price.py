
from searcher.cmb_searcher import CMBPriceSearcher
from searcher.boc_searcher import BOCPriceSearcher
from searcher.travelex_searcher import TravelexPriceSearcher
from models import CurrencyRate
from dbsession import DBSession,Base

session=DBSession.dbSession()

# #travelex get data
# travelexSearcher=TravelexPriceSearcher()
# travelexData=travelexSearcher.getAllHistoryData()
# session.add_all(travelexData)
# session.commit()

#boc get data
bocSearch= BOCPriceSearcher()
bocData=bocSearch.getAllHistoryData()
session.add_all(bocData)
session.commit()

# #cmb get data
# cmbSearcher=CMBPriceSearcher()
# cmbData=cmbSearcher.getAllHistoryData()
# session.add_all(cmbData)
# session.commit()