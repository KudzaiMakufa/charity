from django.shortcuts import render
import calendar
from datetime import datetime
from django.contrib.auth.decorators import login_required , permission_required
from listrequests.forms import Charity_Request_Form,Charity_Request_Donor_Form
from listrequests.models import  Charity_Request ,Charity_Request_Donor
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# @login_required
# def dashboard_index(request):

    
    
#     url = "dashboard/index.html"    
#     with PyPISimple() as client:
#         requests_page = client.get_project_page('requests')
#     requests_page = client.get_project_page('requests')
#     pkg = requests_page.packages[0]
#     print(pkg.version)
    
#     context = {
#         'title': pkg.version,
       
        
      
#     }

#     return render(request , url , context) 


def create_request(request):
    form = None
    url = "requests/create_request.html" 
    if request.method == 'POST':
        form = Charity_Request_Form(request.POST, request.FILES)
  

        
        if(form.is_valid()):
            form_data = form.cleaned_data
            
            if(form_data['password'] != form_data['confirm_password']):
                messages.add_message(request, messages.ERROR, 'Passwords did not match')
                return HttpResponseRedirect(reverse('listrequests:create_request'))
            else:
                data = form.save(commit=False)
                data.created_at = timezone.now()
                data.updated_at = timezone.now()
               
                data.save()
                messages.add_message(request, messages.INFO, 'Application submited , check later')
                return HttpResponseRedirect(reverse('listrequests:requests'))
     
    else:
        form = Charity_Request_Form()
    
    context = {
        
        'title': "Apply for Charity Listing",
        'form':form
        
    } 
     
    return render(request , url , context)
def create_request_donor(request):
    form = None
    url = "requests/create_request_donor.html" 
    if request.method == 'POST':
        form = Charity_Request_Donor_Form(request.POST, request.FILES)
  

        
        if(form.is_valid()):
            form_data = form.cleaned_data
            
            if(form_data['password'] != form_data['confirm_password']):
                messages.add_message(request, messages.ERROR, 'Passwords did not match')
                return HttpResponseRedirect(reverse('listrequests:create_request_donor'))
            else:
                data = form.save(commit=False)
                data.created_at = timezone.now()
                data.updated_at = timezone.now()
               
                data.save()
                messages.add_message(request, messages.INFO, 'Application submited , check later')
                return HttpResponseRedirect(reverse('listrequests:create_request_donor'))
     
    else:
        form = Charity_Request_Donor_Form()
    
    context = {
        
        'title': "Apply for Donor Listing",
        'form':form
        
    } 
     
    return render(request , url , context)


@login_required
def list_requests(request):
    allrequests = Charity_Request.objects.all().order_by('-id')
    url = "requests/list_requests.html" 
    context = {
        
        'title': "Show Listing Requests",
        'libraries':allrequests
        
    } 
    return render(request , url , context)

@login_required
def list_requests_donor(request):
    allrequests = Charity_Request_Donor.objects.all().order_by('-id')
    url = "requests/list_requests_donor.html" 
    context = {
        
        'title': "Show Donor Registration Requests",
        'libraries':allrequests
        
    } 
    return render(request , url , context)

@login_required
def approve_request(request ,lib_id=None):
    req = Charity_Request.objects.get(pk=lib_id)

    req.approved = 1
    req.save()

    # create user 
    try:
        user = User.objects.create_user(req.email, req.email, req.password)
        user.save()
        user.last_name = req.organisation_name
        user.first_name = req.organisation_name
        user.save()


        # add user to doctor group 
    
        my_group = Group.objects.get(name='charity') 
        my_group.user_set.add(user)
        
        
        
    except:
        messages.add_message(request, messages.ERROR, ' Username or emails exists')

    messages.add_message(request, messages.INFO, 'Application approved ')
    return HttpResponseRedirect(reverse('listrequests:requests'))

@login_required
def approve_request_donor(request ,lib_id=None):
    req = Charity_Request.objects.get(pk=lib_id)

    req.approved = 1
    req.save()

    # create user 
    try:
        user = User.objects.create_user(req.email, req.email, req.password)
        user.save()
        user.last_name = req.organisation_name
        user.first_name = req.organisation_name
        user.save()


        # add user to doctor group 
    
        my_group = Group.objects.get(name='charity') 
        my_group.user_set.add(user)
        
        
        
    except:
        messages.add_message(request, messages.ERROR, ' Username or emails exists')

    messages.add_message(request, messages.INFO, 'Application approved ')
    return HttpResponseRedirect(reverse('listrequests:create_request_donor'))

    # context = {
    #     "item":req[0], 
     
    # }
    # return render(request, 'requests/list_requests.html', context)
    
# @login_required
# def vuln_check(request ,lib_id=None):
#     library = Library.objects.filter(id=lib_id).order_by('-id')
#     f = open(library[0].library_list.path, "r")
#     print("------------------")

#     lines = f.readlines()

#     data = []
   
#     for line in lines:
#         # here comes the vuln scanner logic
#         sep = '=='
#         stripped = line.split(sep, 1)[0]
#         lib_version = line.split(sep, 1)[1]
#         is_safe = False
#         # print(line.strip())
#         # print("-------without end-------")
#         # print(line.split(sep, 1)[0])
#         # print("------with end-----")
      
#         # check updates and security
#         with PyPISimple() as client:
#             requests_page = client.get_project_page(stripped.strip())
        
#         requests_page = client.get_project_page(stripped.strip())
#         pkg_params = {}

#         if(library[0].data_mode == 'application'):

#             try:
#                 try:
#                     vulners_api = vulners.Vulners(api_key="4QIYDKA0NXPHUWXJNQYLISIZEZZH8FM25YNK0L518VOWJJEOWO81XGMH2KSL81KJ")
#                     results = vulners_api.softwareVulnerabilities(stripped.strip(), lib_version.strip())
#                     print(len(stripped.strip()))
#                     print(len(lib_version.strip()))
#                     # results = vulners_api.softwareVulnerabilities("httpd", "1.3")
#                     exploit_list = results.get('exploit')
#                     vulnerabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]
#                     # print(vulnerabilities_list[0][0]['type'])
                    

#                 except:
#                     is_safe = True
#                     print("safe")
#                 pkg = requests_page.packages[0]
#                 pkg_params = {"name":pkg.project , "current_version":lib_version.strip() , "latest_version":pkg.version ,"digest":pkg.get_digests()['sha256'] , 'url':pkg.url ,'is_signed':pkg.has_sig ,'is_safe':is_safe}
#             except:
#                  pkg_params = {"name":stripped.strip() , "current_version":lib_version.strip() , "latest_version":"n/a" ,"digest":"n/a",'is_safe':is_safe}

#              # scan safety-db
            
#         elif(library[0].data_mode == 'services'):
#             pkg_params = {"name":stripped.strip() , "current_version":lib_version.strip() , "latest_version":"n/a" ,"digest":"n/a" ,'is_safe':is_safe}
#         elif(library[0].data_mode == 'windows'):
#             try:
#                 vulners_api = vulners.Vulners(api_key="4QIYDKA0NXPHUWXJNQYLISIZEZZH8FM25YNK0L518VOWJJEOWO81XGMH2KSL81KJ")
#                 win_vulners = vulners_api.kbAudit(os="Windows Server 2012 R2", kb_list=["KB4072650", "KB2959936", "KB2894856", "KB2896496"])
#                 need_2_install_kb = win_vulners['kbMissed']
#                 affected_cve = win_vulners['cvelist']

#             except:
#                 is_safe = True
#                 print(is_safe)
#             pkg_params = {"name":stripped.strip() , "current_version":lib_version.strip() , "latest_version":"n/a" ,"digest":"n/a",'is_safe':is_safe}
#         else:pass
        


        
       

#         data.append(pkg_params.copy())
    
        
           
 
#     print("------------------")
#     f.close()
#     context = {
#         "item":library[0],
#         "data":data 
       
#     }
#     return render(request, 'dashboard/vulncheck.html', context)