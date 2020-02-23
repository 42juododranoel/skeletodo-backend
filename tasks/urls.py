from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
