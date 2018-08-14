import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from getcurrencyrate.models import CurrencyRate
from getcurrencyrate.dbsession import DBSession, Base
from getcurrencyrate import json_util
import json

bp = Blueprint('rate', __name__, url_prefix='/rate')


@bp.route('/getrate', methods=('GET', 'POST'))
def getRate():
    session = DBSession.dbSession()
    result = session.query(CurrencyRate)[:100]
    return render_template("getrate.html", rateList=result)


@bp.route('/getLineStack', methods=(['GET']))
def getLineStack():
    session = DBSession.dbSession()
    result = session.query(CurrencyRate)[:100]
    return render_template("getLineStack.html", rateList=result)


@bp.route('/getLineStack', methods=(['POST']))
def getLineStackPost():
    session = DBSession.dbSession()
    print("request:"+str(request.form))
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    currnecyCode = request.form['currencyCode']
    result = session.query(CurrencyRate).filter(
        CurrencyRate.currencyCode == currnecyCode,
        CurrencyRate.date >= startDate,
        CurrencyRate.date <= endDate).order_by(
            CurrencyRate.date).all()
    travelexList=[item.serialize for item in result if item.sourceCode=='Travelex']
    cmbList=[item.serialize for item in result if item.sourceCode=='CMB']    
    return  jsonify(data={'travelex':travelexList,'cmb':cmbList})

