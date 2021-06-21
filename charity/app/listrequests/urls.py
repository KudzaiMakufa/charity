from django.urls import path
from listrequests import views
app_name = 'listrequests'
urlpatterns = [ 
    path('create', views.create_request ,name="create_request"),
    path('create_request_donor', views.create_request_donor , name="create_request_donor"),
    path('requests', views.list_requests ,name="requests"),
    path('requests_donor', views.list_requests_donor ,name="requests_donor"),
    path('approve/<int:lib_id>', views.approve_request , name="approve"),
    path('approve_donor/<int:lib_id>', views.approve_request_donor , name="approve_donor"),

    path('delete_request/<int:lib_id>', views.delete_request , name="delete_request"),
    path('delete_request_donor/<int:lib_id>', views.delete_request_donor , name="delete_request_donor"),
   
    
    #path('vuln_check/<int:lib_id>', views.vuln_check , name="vuln_check"),


    
 
]