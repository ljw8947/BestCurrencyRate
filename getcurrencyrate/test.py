from models import CurrencyRate
from dbsession import DBSession,Base

print(CurrencyRate.__table__)   
Base.metadata.create_all(DBSession.__engine__)