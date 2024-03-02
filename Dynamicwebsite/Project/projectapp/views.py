# Import necessary modules
from django.shortcuts import render
from .models import Place, my_team


# Define the view function named 'demo'
def demo(request):
    # Retrieve all objects from the 'Place' model
    obj = Place.objects.all()

    # Retrieve all objects from the 'my_team' model
    obj_my_team = my_team.objects.all()

    # Render the 'Register.html' template with the retrieved objects as context
    return render(request, "index.html", {'results': obj, 'my_team_result': obj_my_team})
from django.shortcuts import render

# Create your views here.
