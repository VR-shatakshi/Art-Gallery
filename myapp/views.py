from django.shortcuts import render,redirect
from .forms import ImageForm

from .models import Image
# Create your views here.
def home(request):
    form = ImageForm()
    
    if request.method == 'POST':
     form = ImageForm(request.POST,request.FILES)
     if form.is_valid():
      form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})
  
def delete_img(request, id):
    img = Image.objects.get(id=id)
    img.delete()
    return redirect('/')


