from django.shortcuts import render
from .models import Facility, Service ,Category  
from io import BytesIO
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from django.http import HttpResponse
import qrcode

# Create your views here.

def generate_qr_code(request):
    menu_url = request.build_absolute_uri('/')+'/'
    qr=qrcode.make(menu_url)
    buffer=BytesIO()
    qr.save(buffer,format='PNG')
    buffer.seek(0)
    return HttpResponse(buffer,content_type='image/png')
    
   

def index(request):
    
    facilities = Facility.objects.all()
    services = Service.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'index.html', {'facilities': facilities, 'services': services, 'categories': categories})




def facilities(request):
    categories = Category.objects.all()
    facilities = Facility.objects.all()
    return render(request, 'facilities.html', {'facilities': facilities, 'categories': categories})

def services(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services, 'categories': categories})





