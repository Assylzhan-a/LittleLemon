from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import menu, booking
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer


