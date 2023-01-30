from django.shortcuts import render
from .forms import Register

def register_view(request):

    form = Register()
    
    context = {
        'form': form
    }

    return render(request, 'register.html', context)
