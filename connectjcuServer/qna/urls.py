from django.urls import path

from .import views

urlpatterns = [
    path('',views.QnaMixinListView.as_view(), name = "qna-list"),
    path('<int:pk>/', views.QnaMixinDetailView.as_view(), name='qna-detail')
]