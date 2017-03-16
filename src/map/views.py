from django.shortcuts import render
from django.http.response import HttpResponse
from map.models import RoadNetwork

def index(request):
    """
    Renders the
    """
    context = {}

    return render(request, 'map/index.dtl', context)


def result(request):
    context = {}
    lookupID = request.GET.get('element-id')

    lookup_object = RoadNetwork.objects.get(pk=lookupID)

    #print(dir(lookup_object))
    #print(dir(lookup_object.geometry))
    lookup_object.geometry.transform(4326)

    lookup_geometry = lookup_object.geometry.geojson


    context = {
    'lookup_ID' : lookupID,
    'lookup_Geometry' : lookup_geometry
    }


    return render(request, 'map/result.dtl', context)
