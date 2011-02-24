# Create your views here.
###########
# IMPORTS #
###########

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import *

#######################
# FUNCTION DEFINITIONS #
#######################

def view_page(request):
    """
    Function return a dashboard in list form where we can see the company details and number of members.
    """
    # Retrive all the data from the table competitors 
    data_list=Data.objects.all()

    # Return the Dashboard & display the list of competitors
    return render_to_response('dashboard.html', {'data_list': data_list})

def add_new(request):
    """
    Function allow to add a new company to the dashboard.
    """
    # Keep empty all the data member
    context = name = url = country = active_since = location = ''

    # get the data from user using method = post from <form> tag 
    # Check the data is posted or not
    if request.POST:
        context = request.POST.get('context')
        name = request.POST.get('name')
        url = request.POST.get('url')
        country = request.POST.get('country')
        active_since = request.POST.get('active_since')
        location = request.POST.get('location')
        
        # Create or update the data using create method 
        Data.objects.create(context = context,
                            name    = name,
                            url     = url,
                            country = country,
                            active_since = active_since,
                            location = location)
        
        # Redirected to dashboard and display updated competitors list
        return HttpResponseRedirect('/dashboard/')

    return render_to_response('addnewcompany.html')


def login_user(request):
    """
    Function for login with username and password.
    """
    state = "Please log in "
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticating username and passward it will return 1 or 0
        user = authenticate(username=username, password=password)
        if user is not None: 

            # If value return 1 then user is active     
            if user.is_active:

                # Login that user and redirected to competitors list
                login(request, user)
                state = "You are successfully logged in!"
            return HttpResponseRedirect('/dashboard/')
        else:
            state = "Your username or password is incorrect."

    return render_to_response('login.html',{'state':state, 'username': username})
