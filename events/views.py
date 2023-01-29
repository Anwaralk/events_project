from django.shortcuts import render
from .models import Event
from events.forms import Register 
from django.http import HttpResponse


def get_index(request):
    queryset = Event.objects.all()
    events_list = []

    for n in queryset:
        events_list.append({
            'name': n.name,
            'date': n.date,
            'description': n.description,
            
        })
    
    
    context = {'all_events': events_list}

    return render(request, 'home.html', context)


# def get_event_detail(request, event_pk):
#     queryset = Event.objects.get(pk = event_pk)

#     context = {
#         'event_detail': queryset
#     }

#     return render(request, 'event_detail.html', context)

# def register_view(request):
#         form = Register()

#         context = {
#             'forms': form
#         }
#         return render(request, 'register.html', )
