from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    
    img = Image.objects.all().order_by('-date')  
    return render(request, 'home.html', {'img': img, 'form': form})

def delete_img(request, id):
    img = get_object_or_404(Image, id=id)
    img.delete()  
    return redirect('/')


