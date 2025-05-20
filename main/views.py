from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "main/index.html", { 
        "main": now.month == 5 and now.day == 17
     })