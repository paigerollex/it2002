from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.

def library(request):
    form = LibraryForm()
    context = {"form1":form}
    
    # if request.method == 'POST':
    #     f = LibraryForm(request.POST)
    #     if f.is_valid():
    #         lb = Library.objects.get(library_id=request.POST.get("library"))
    #         lv = Level.objects.get(level_id=request.POST.get("level"))
    #         st = Seat.objects.get(seat_id=request.POST.get("seat"))
    #         day = request.POST.get("date")
    #         start = request.POST.get("start_time")
    #         end = request.POST.get("end_time")
    #         Occupied.objects.create(matric_no=request.user.username,
    #                                 library=lb,
    #                                 level=lv,
    #                                 seat=st,
    #                                 book_date=day,
    #                                 start_time=start,
    #                                 end_time=end)
    #         print("Printing post:", lb)
    #         print("Printing post:", request.POST.get("start_time"))
    #         print("Printing post:", request.POST.get("end_time"))
    
    if request.method == 'GET':
        print("PRINTING VALUE:", request.GET.get("date"))
    return render(request, "library.html", context)

def level(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["level"])

def date(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["date"])

def start_time(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["start_time"])

def end_time(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["end_time"])

def seat(request):
    form = LibraryForm(request.GET)
    return HttpResponse(form["seat"])
