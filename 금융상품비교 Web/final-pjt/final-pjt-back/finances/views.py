from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .serializers import FinanceSerializer, OptionSerializer
from .models import Finance,Option
# Create your views here.
SAVE_API = settings.SAVE_API
RATE_API = settings.RATE_API

@api_view(['GET'])
def finance_list(request):
    URL = 'http://finlife.fss.or.kr/finlifeapi/'
    deposit_URL = URL + 'depositProductsSearch.json'
    deposit_params = {
        'auth' : SAVE_API,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }
    response = requests.get(deposit_URL,params=deposit_params).json()
    deposit_finances = response['result']['baseList']
    deposit_financeserializer = FinanceSerializer(data=deposit_finances, many=True)
    if deposit_financeserializer.is_valid():
        deposit_financeserializer.save(prdt_category='deposit')
    deposit_options = response['result']['optionList']
    for deposit_option in deposit_options:
        fin_prdt_cd = deposit_option['fin_prdt_cd']
        deposit_optionserializer = OptionSerializer(data=deposit_option)
        finance = Finance.objects.get(fin_prdt_cd=fin_prdt_cd)
        if deposit_optionserializer.is_valid() and not Option.objects.filter(finance=finance, save_trm=deposit_option['save_trm']).exists():
            deposit_optionserializer.save(finance=finance)

    saving_URL = URL + 'savingProductsSearch.json'
    saving_params = {
        'auth' : SAVE_API,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }
    response = requests.get(saving_URL,params=saving_params).json()
    saving_finances = response['result']['baseList']
    saving_financeserializer = FinanceSerializer(data=saving_finances, many=True)
    if saving_financeserializer.is_valid():
        saving_financeserializer.save(prdt_category='saving')
    saving_options = response['result']['optionList']
    for saving_option in saving_options:
        fin_prdt_cd = saving_option['fin_prdt_cd']
        saving_optionserializer = OptionSerializer(data=saving_option)
        finance = Finance.objects.get(fin_prdt_cd=fin_prdt_cd)
        if saving_optionserializer.is_valid() and not Option.objects.filter(finance=finance, save_trm=saving_option['save_trm']).exists():
            saving_optionserializer.save(finance=finance)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        finances = Finance.objects.all()
        serializer = FinanceSerializer(finances, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def options(request):
    if request.method == 'GET':
        options = Option.objects.all()
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def exchange(request):
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

    params = {
        'authkey': RATE_API,
        'data':'AP01',
        'searchdate': '20240517',
    }
    response = requests.get(URL,params=params).json()
    return JsonResponse({'response':response})