"""
URL configuration for connectjcuServer project.

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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from connectjcuServer.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path('api/',include('api.urls')),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/blogs/', include('blogs.urls')),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/resources/', include('resources.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/qna/', include('qna.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
