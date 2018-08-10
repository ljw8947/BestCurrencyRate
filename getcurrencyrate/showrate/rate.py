import functools
from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from getcurrencyrate.models import CurrencyRate
from getcurrencyrate.dbsession import  DBSession,Base


bp=Blueprint('rate',__name__,url_prefix='/rate')



@bp.route('/getrate',methods=('GET','POST'))
def getRate():
    session=DBSession.dbSession()
    result=session.query(CurrencyRate)[:100]
    return render_template("getrate.html",rateList=result)

@bp.route('/getLineStack',methods=('GET','POST'))
def getLineStack():
    session=DBSession.dbSession()
    if request.method=="POST":
        startDate=request.form['startDate']
        endDate=request.form['endDate']
        currnecyCode=request.form['currencyCode']
        result=session.query(CurrencyRate).filter(
            CurrencyRate.sourceCode==sourceCode,CurrencyRate.currencyCode==currnecyCode\
            ,CurrencyRate.date>=startDate,CurrencyRate.date<=endDate)
    else:
        result=session.query(CurrencyRate)[:100]
    return render_template("getLineStack.html",rateList=result)

