from django.shortcuts import render
from django.http import HttpResponse
from .models import CurrencyRate
def index(request):
    return HttpResponse("This is getRate Job")

def getAll(request):
    l=CurrencyRate.objects.all()
    return HttpResponse(l)