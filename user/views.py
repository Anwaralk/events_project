from django.shortcuts import render
from django.contrib.auth import login
from .forms import Register

def register_view(request):
    form = Register()

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)

            return redirect('home')
    
    context = {
        'form': form
    }

    return render(request, 'register.html', context)
