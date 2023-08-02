from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income, Token, User
import datetime

# Create your views here.
@csrf_exempt
def submit_expense(request):
    #TODO: validate token, amount, text
    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user=this_user, amount=request.POST["amount"],
                           text=request.POST["text"], date=date)

    return JsonResponse({
        "status": "ok"
    }, encoder=json.JSONEncoder)

@csrf_exempt
def submit_income(request):
    #TODO: validate token, amount, text
    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    else:
        date = request.POST['date']
    Income.objects.create(user=this_user, amount=request.POST["amount"],
                           text=request.POST["text"], date=date)

    return JsonResponse({
        "status": "ok"
    }, encoder=json.JSONEncoder)
