from django.shortcuts import render
import datetime
# Create your views here.
def festival(request,name):
    now=datetime.datetime.now()
    if(name=='new year'):
        return render(request,"festival.html", {
            "name": now.day==1 and now.month == 1
        })
    if (name == 'republic day'):
        return render(request, "festival.html", {
            "name": now.day == 26 and now.month == 12
        })
    if (name == 'independence day'):
        return render(request, "festival.html", {
            "name": now.day == 15 and now.month == 8
        })
    if (name == 'gandhi jayanti'):
        return render(request, "festival.html", {
            "name": now.day == 2 and now.month == 10
        })
    if (name == 'christmas'):
        return render(request, "festival.html", {
            "name": now.day == 25 and now.month == 12
        })