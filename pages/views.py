from django.shortcuts import render
# Create your views here.

# We are using functional based views 

def index(request):
    # render is a special django function that creates a shortcut for communicating with the web browser
    # It returns the appropriately formatted response without you having to code the intermediate steps
    # We are returning the original request object from the browser and the name of our site template
    return render(request, 'base.html') 