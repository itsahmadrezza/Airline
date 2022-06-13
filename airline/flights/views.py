from django.shortcuts import render

from .models import Flight, Passenger, Airport
# Create your views here.

def index(request):
    return render(request, 'flights/index.html', {
        "flights": Flight.objects.all()
    })
    
        
    
def flight(request, flight_id): # <- for get
    flight = Flight.objects.get(id = flight_id) # dictunary for post flight information
    passengers = flight.passengers.all()
    return render(request, 'flights/flight.html', {
        "flight": flight,
        "Passengers": passengers
    })


    