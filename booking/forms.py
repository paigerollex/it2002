from dbm.ndbm import library
from django import forms
from .models import *
from dynamic_forms import DynamicField, DynamicFormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .widgets import DatePickerInput, TimePickerInput
from django.db.models import Q, F
from django.shortcuts import  get_object_or_404


class LibraryForm(DynamicFormMixin, forms.Form):
    lvl = '-'
    
    def level_choices(form):
        library = form['library'].value()
        return Level.objects.filter(library=library)
    
    def level_initial(form):
        library = form['library'].value()
        return Level.objects.filter(library=library).first()
    
    def seat_choices(form):
        return Occupied.objects.filter(level=form['level'].value())
    
    def seat_initial(form):
        level = form['level'].value()
        return Seat.objects.filter(level=level).first()
    
    library = forms.ModelChoiceField(
        queryset=Library.objects.all(),
        initial=Library.objects.all().first()
    )
    
    level = DynamicField(
        forms.ModelChoiceField,
        queryset=level_choices,
        #initial=level_initial
    )
    
    date = forms.DateField(widget=DatePickerInput)
    
    start_time = forms.TimeField(widget=TimePickerInput)
    
    end_time = forms.TimeField(widget=TimePickerInput)
    
    seat = DynamicField(
        forms.ModelChoiceField,
        queryset=seat_choices,
        #initial=seat_initial
    )
    
