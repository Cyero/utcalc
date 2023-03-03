from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserData
from .forms import UserForm


def calc(request) -> render:
    db, created = UserData.objects.get_or_create(user_id=request.user)
    data = UserData.objects.all().values().filter(user_id=request.user)
    form = UserForm()
    for d in data:
        form.fields["electricity_past"].initial = d['electricity_past']
        form.fields["water_past"].initial = d['water_past']
        form.fields["electricity_tariff"].initial = d['electricity_tariff']
        form.fields["water_tariff"].initial = d['water_tariff']
    return render(request, 'calc/index.html', {"data": data, "form": form})


def get_name(request) -> HttpResponseRedirect or render:
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            electricity_past = form.cleaned_data['electricity_current']
            water_past = form.cleaned_data['water_current']
            electricity_tariff = form.cleaned_data['electricity_tariff']
            water_tariff = form.cleaned_data['water_tariff']
            db = UserData.objects.all().values().filter(user_id=request.user)
            db.update(electricity_past=electricity_past, water_past=water_past, electricity_tariff=electricity_tariff,
                      water_tariff=water_tariff)
            return HttpResponseRedirect("result")
    else:
        form = UserForm()
    return render(request, "calc/result.html", {"form": form})
