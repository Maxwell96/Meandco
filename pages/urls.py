from django.urls import path
from . import views 


urlpatterns = [
    # When a user navigates to the site root this will set the pagename to an empty string, we do 
    # this because the path function can't capture an empty string
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    # We are using a capturing group. Everything inside the angle brackets will be captured and send
    # to the view as a string parameter (pagename)
    path('<str:pagename>', views.index, name='index'),
]