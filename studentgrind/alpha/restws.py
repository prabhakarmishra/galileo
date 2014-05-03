# Create your web services here

from django.http import HttpResponse
from models import Item
from django.shortcuts import get_object_or_404
from httplib import HTTPResponse
from django.core import serializers

def xml_view(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return HTTPResponse(serializers.serialize("xml",result), mimetype="text/xml")
    return wrapper

@xml_view
def index(request):
    return Item.objects.all()

@xml_view
def get(request, item_name):
    return get_object_or_404(Item, pk= item_name)