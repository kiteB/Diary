"""DiaryProject URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from diary import views as D

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('diary')),
    path('', D.home, name='home'),
    path('search/', D.search, name='search'),
    path('<str:id>', D.detail, name='detail'),
    path('diary/', D.make_diary, name='diary'),
    path('delete/<str:id>', D.delete, name='delete'),

    # social login
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)