"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# this tow inport use for import images file to our project and only use in localhost
from django.conf import settings
from django.conf.urls.static import static
# ------------------------------------------------
from django.contrib import admin
from django.urls import include, path
# -------------------------------------------
from core.views import contact
import core.views 
from item.views import detail,addnew,delete,edit,items


urlpatterns = [
    path('inbox/',include('conversation.urls')),

    # path('',core.views.index,name='index'),
    path('', include('core.urls')),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', edit, name='edit'),

    path('new/',addnew,name='new'),
    # path('/items/', include('item.urls')), 
    # path('items/',include('item.urls')),
    # path('contact/',contact,name='contact'),
    path('dashboard/',include('dashboard.urls')),
    path('items/',items,name='items'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
# static use with tow import to desplay img in local host