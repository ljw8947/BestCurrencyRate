
from .cmb_searcher import CMBPriceSearcher
from .boc_searcher import BOCPriceSearcher
from .travelex_searcher import TravelexPriceSearcher

#travelex get data
travelexSearcher=TravelexPriceSearcher()
travelexData=travelexSearcher.getAllHistoryData()
for item in travelexData:
    item.save()


#boc get data
bocSearch= BOCPriceSearcher()
bocData=bocSearch.getAllHistoryData()
for item in bocData:
    item.save()

#cmb get data
cmbSearcher=CMBPriceSearcher()
cmbData=cmbSearcher.getAllHistoryData()
for item in bocData:
    item.save()