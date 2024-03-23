from django.urls import path

from .import views

urlpatterns = [
    path('',views.BlogMixinListView.as_view(), name = "blog"),
    path('<int:pk>/', views.BlogMixinDetailView.as_view())
]