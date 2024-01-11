from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Restaurant, Booking

# Create your views here.
class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.filter(status=1).order_by("city")
    template_name = "mainpage/index.html"

def restaurant_detail(request, slug):
    queryset = Restaurant.objects.filter(status=1)
    restaurant = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "mainpage/restaurant_detail.html",
        {"restaurant": restaurant},
    )