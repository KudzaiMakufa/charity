from django.urls import path
from listrequests import views
app_name = 'listrequests'
urlpatterns = [ 
    path('create', views.create_request ,name="create_request"),
    path('requests', views.list_requests ,name="requests"),
    path('approve/<int:lib_id>', views.approve_request , name="approve"),
    # path('vuln_check/<int:lib_id>', views.vuln_check , name="vuln_check"),


    
 
]