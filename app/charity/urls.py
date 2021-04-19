"""vulncheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from home import urls as home_urls
from mainmenu import urls as mainmenu_urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls  import url
from django.conf.urls.static import static
from listrequests import urls as listrequests_urls
from donation import urls as donation_urls
from donation import views as donation_view

urlpatterns = [
   
        url(r'^paypal/', include('paypal.standard.ipn.urls')),
        url(r'^payment_process/$', donation_view.payment_process, name='payment_process' ),
     
    path('home/', include(home_urls, namespace="home")),
    path('mainmenu/', include(mainmenu_urls, namespace="mainmenu")),
    path('listrequests/', include(listrequests_urls, namespace="listrequests")),
    path('donation/', include(donation_urls, namespace="donation")),
    
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'CHARITY'
admin.site.site_title = 'CHARITY'
