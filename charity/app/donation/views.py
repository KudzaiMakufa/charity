from django.shortcuts import render
import calendar
from datetime import datetime
from django.contrib.auth.decorators import login_required , permission_required
from donation.forms import Donation_Form
from donation.models import  Donation
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm


def payment_process(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100',
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('donation:list_donations')),
        'cancel_return': 'http://{}{}'.format(host, reverse('donation:list_donations')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'donation/payment_process.html', {'form': form})

def create_donation(request):
    form = None
    url = "donation/create_donation.html" 
    if request.method == 'POST':
        form = Donation_Form(request.POST, request.FILES)
        print(form)

        
        if(form.is_valid()):
            data = form.save(commit=False)
            data.created_at = timezone.now()
            data.updated_at = timezone.now()
            data.created_by = request.user.id
            data.save()
            messages.add_message(request, messages.INFO, 'Donation Request Created ')
            return HttpResponseRedirect(reverse('donation:list_donations'))
     
    else:
        form = Donation_Form()
    
    context = {
        
        'title': "Create a donation request campaign",
        'form':form
        
    } 
     
    return render(request , url , context)

@login_required
def list_donations(request):
    donations = Donation.objects.all().order_by('-id')
    url = "donation/list_donations.html" 
 
    context = {
        
        'title': "Show Donation Requests",
        'donations':donations
        
    } 
    return render(request , url , context)
@login_required
def my_requests(request):
    donations = Donation.objects.filter(created_by = request.user.id).order_by('-id')
    url = "donation/my_requests.html" 
 
    context = {
        
        'title': "Show My Donation Requests",
        'donations':donations
        
    } 
    return render(request , url , context)

@login_required
def make_donation( request , don_id = None):
    donation = Donation.objects.filter(id=don_id)
    url = "donation/make_donation.html" 
   
    context = {
        
        'title': "Make Donation",
        'donation':donation[0]
        
    } 
    return render(request , url , context)
@login_required
def paynow( request , amount = None):
  
    url = "donation/payment_process.html" 
   
    context = {
        
        'title': "Make Donation",
     
        
    } 
    return render(request , url , context)