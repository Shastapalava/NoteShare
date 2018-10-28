from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import ordUser
# Create your views here.
def home(request):
    users = ordUser.objects.all()
    return render(request, 'home.html', {'user': users})

def ordUser_detail(request, id):
    try:
        user = ordUser.objects.get(id = id)
    except ordUser.DoesNotExist:
        raise Http404('User not found')

    return render(request, 'ordUser_detail.html', {'user': user})