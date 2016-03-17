from django.shortcuts import render
from microscope.models import Slide
# Create your views here.
def home(request):
    slide = Slide.objects.get(pk=1)
    return render(request, 'microscope/detail.html', {"slide":slide})
