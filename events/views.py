from django.shortcuts import render
from .models import Event


def get_index(request):
    queryset = Event.objects.all()
    events_list = []

    for n in queryset:
        events_list.append({
            'event_name': n.event_name,
            'event_date': n.event_date,
            'event_description': n.event_description,
            'event_pk': n.event_pk,
        })

    context = {'all_events': events_list}

    return render(request, 'events.html', context)


def get_event_detail(request, event_pk):
    queryset = Event.objects.get(pk = event_pk)

    context = {
        'event_detail': queryset
    }

    return render(request, 'event_detail.html', context)
