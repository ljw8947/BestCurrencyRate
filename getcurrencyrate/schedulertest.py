from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor,ProcessPoolExecutor

jobstores={
    'default':SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}
executors={
    'default':ThreadPoolExecutor(20),
    'processpool':ProcessPoolExecutor(5)
}
job_defaults={
    'coalesce':False,
    'max_instances':3
}
scheduler=BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc
)
from datetime import datetime
import time
def getTime():
    now=datetime.now()
    with open('jobresult.txt','a') as f:
        f.write(str(now)+'\n')

sched=BlockingScheduler()
scheduler.add_job(getTime,'interval',id='getTime',replace_existing=True,seconds=3
    ,end_date='2018-08-02 16:21:30')
scheduler.start()
#time.sleep(30)