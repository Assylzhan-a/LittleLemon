from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import menu, booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer