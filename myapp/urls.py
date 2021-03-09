
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.KiteListView.as_view(), name='list'),
    path('detail/<int:pk>', views.KiteDetailView.as_view(), name='detail'),
    path('addkite', views.KiteCreateView.as_view(), name='addkite'),
    path('update/<int:pk>', views.KiteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.KiteDeleteView.as_view(), name='delete'),

]