from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
import datetime
from .forms import CarForm

class DashboardView(View):
    def get(self,request):
        form = CarForm
        return render(request, 'cars.html',{'form':form})
    
    def post(self, request):
        fee = 0
        result = 0
        bhm = 26
        duty = 0
        form = CarForm(request.POST or None)
        if form.is_valid():
            cost = form.cleaned_data['price']
            year = form.cleaned_data['year']
            size_of_engine = form.cleaned_data['size_of_engine']
            type_of_car = form.cleaned_data['type_of_car']
            if int(datetime.date.today().year) - int(year) <= 3 and size_of_engine == "1000cm dan kichik":
                bhm = bhm * 30
                duty = 0.05
            elif int(datetime.date.today().year) - int(year) <= 3 and size_of_engine == "1000cm dan - 2000cm gacha":
                bhm = bhm * 120
                duty = 0.05
            elif int(datetime.date.today().year) - int(year) <= 3 and size_of_engine == "2000cm dan - 3000cm gacha":
                bhm = bhm * 180
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) <= 3 and size_of_engine == "3000cm dan - 3500cm gacha":
                bhm = bhm * 240
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) <= 3 and size_of_engine == "3500cm dan katta":
                bhm = bhm * 300
                duty = 0.15
            #ishlab chiqarilganiga 3 yildan o'tgan
            elif int(datetime.date.today().year) - int(year) >= 3 and size_of_engine == "1000cm dan kichik":
                bhm = bhm * 90
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) >= 3 and size_of_engine == "1000cm dan - 2000cm gacha":
                bhm = bhm * 210
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) >= 3 and size_of_engine == "2000cm dan - 3000cm gacha":
                bhm = bhm * 330
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) >= 3 and size_of_engine == "3000cm dan - 3500cm gacha":
                bhm = bhm * 390
                duty = 0.15
            elif int(datetime.date.today().year) - int(year) >= 3 and size_of_engine == "3500cm dan katta":
                bhm = bhm * 480
                duty = 0.15
            if type_of_car == "Benzin-Dizel":
                if size_of_engine == "1000cm dan kichik":
                    fee = (cost * 0.12) + bhm
                    fee += cost * 0.002
                    result = cost + fee
                elif size_of_engine == "1000cm dan - 2000cm gacha" or size_of_engine == "2000cm dan - 3000cm gacha" or size_of_engine == "3000cm dan - 3500cm gacha" or size_of_engine == "3500cm dan katta":
                    duty = cost * duty
                    fee = (cost * 0.12) + bhm + duty
                    fee += cost * 0.002
                    result = cost + fee
            elif type_of_car == "Elektr-Gibrid":
                fee = (cost * 0.12) + bhm
                fee += cost * 0.002
                result = cost + fee
        form.save()
        messages.success(request, f"Mashina narxi: {cost}")
        messages.success(request, f"Umumiy narxi: {result}")
        messages.success(request, f"Qo'shilgan summa: {fee}")
        return redirect('dashboard')