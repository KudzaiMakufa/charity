from django.urls import path
from donation import views
app_name = 'donation'
urlpatterns = [ 
    
    # path('', views.home_login , name="login"),
    path('create', views.create_donation ,name="create_donation"),
    path('list', views.list_donations ,name="list_donations"),
    path('make_donation/<int:don_id>', views.make_donation ,name="make_donation"),
    path('my_requests', views.my_requests ,name="my_requests"),
    path('paynow/<int:amount>', views.paynow ,name="paynow"),




]
