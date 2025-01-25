from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.urls import reverse  







def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def web_dev(request):
    return render(request,'web-dev.html')

def team(request):
    return render(request,'team.html')

def nav(request):
    return render(request,'nav.html')

def offline(request):
    return render(request,'offline.html')

def online(request):
    return render(request,'online.html')

def funding(request):
    return render(request,'funding.html')

def temp(request):
    return render(request,'temp.html')


# ==============inquiry field=================================================



from django.shortcuts import render, redirect
from django.contrib import messages

def inquiry(request):
    if request.method == "POST":
        # Get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        message = request.POST.get('message')
        company = request.POST.get('company', 'N/A')  # Optional field
        designation = request.POST.get('designation', 'N/A')  # Optional field

        # Validate required fields
        if not all([name, email, contact_number, address, message]):
            messages.error(request, "All required fields must be filled!")
            return render(request, 'inquiry.html')

        # Prepare the message to send via WhatsApp
        whatsapp_message = (
            f"New Inquiry!\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Contact Number: {contact_number}\n"
            f"Address: {address}\n"
            f"Message: {message}\n"
            f"Company: {company}\n" 
            f"Designation: {designation}"
        )

        # Replace this with your actual phone number (with country code, no + sign, and no spaces)
        phone_number = '919769683658'

        # WhatsApp URL format for sending message
        whatsapp_url = f"https://wa.me/{phone_number}?text={whatsapp_message}"

        # Redirect the user to the WhatsApp link with the inquiry data
        return redirect(whatsapp_url)

    return render(request, 'inquiry.html')
