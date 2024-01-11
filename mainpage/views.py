from django.shortcuts import render
from django.views import generic
from .models import Restaurant, Booking

# Create your views here.
class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.filter(status=1).order_by("city")
    template_name = "mainpage/index.html"
    paginate_by = 6