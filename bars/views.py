from django.shortcuts import render
from django.http import HttpResponse

barsList = [
    {
        'id':1,
        'name':'The Flying Cock',
        'location':'NYC',
        'topRated':False
    },
    {
        'id':2,
        'name':'8th Street Tavern',
        'location':'Hoboken',
        'topRated':True
    },
    {
        'id':3,
        'name':'Carmine Street Beers',
        'location':'NYC',
        'topRated':True
    }
]

def get_bars(request):
    context = {'bars':barsList}
    return render(request, 'bars/bars.html', context)

def get_bar(request, pk):
    barObject = None

    for bar in barsList:
        if bar['id'] == pk:
            barObject = bar

    return render(request, 'bars/single-bar.html', {'bar':barObject})
