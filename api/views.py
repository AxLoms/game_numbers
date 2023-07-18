from django.shortcuts import render
import random
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.

number = random.randint(1,100)
attempts = 10
def chek_number(request):
    global attempts
    global number

    response = {
    "hint":"",
    "attempts":""
    }
    

    user_number = int(request.GET.get("user_number"))

    if user_number > number:
        attempts -= 1
        response["hint"] = "Меньше"
        response["attempts"] = attempts
        
    if user_number < number:
        attempts -= 1
        response["hint"] = "Больше"
        response["attempts"] = attempts

    if attempts == 0:
       response["hint"] = "Вы проиграли ахаххахахаха"
       response["attempts"] = attempts     
        
       number = random.randint(1,100)
    
    if user_number == number:
        response["hint"] = "Ты выйграл бро)"
        response["attempts"] = attempts  
        
        number = random.randint(1,100)
        
    return JsonResponse(response,json_dumps_params={'ensure_ascii':False})


def number_s(request):
    global number
    global attempts
    number = random.randint(1,100)
    attempts = 10
    return HttpResponse("reset") 

    
def base(request):
    return render (request, 'base.html')

