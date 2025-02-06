from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from info.models import Info
from .models import Info

# Create your views here.

def info(request):
    infos = Info.objects.all()
    return render(request, 'info.html', {'infos':infos})

def addInfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        adress = request.POST.get('address')
        NativePlace = request.POST.get('native_place')
        occuppation = request.POST.get('occupation')
        study = request.POST.get('study')
        school = request.POST.get('school')
        university = request.POST.get('university')
        degree = request.POST.get('degree')
        description = request.POST.get('description')
        
        info = Info(name=name, image=image, dob=dob, phone=phone, adress=adress, NativePlace=NativePlace, occuppation=occuppation, study=study, school=school, university=university, degree=degree, description=description, addDate=datetime.today())

        info.save()

    return render(request, 'addInfo.html')

def infoDetails(request, info_Id):
    info = get_object_or_404(Info, pk=info_Id)
    return render(request, 'infoDetails.html', {'info':info})
