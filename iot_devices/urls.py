from django.urls import path
from iot_devices import views
from .views import AddNewDev, Dashboard, EditDev

from django.contrib.auth.decorators import login_required


app_name='iot_devices'

urlpatterns = [
    path('', login_required(Dashboard.as_view()), name='dashboard'),
    path('device/new', AddNewDev.as_view(), name='new_device'),
    path('device/<int:id>/', views.ViewDev),
    path('device/<int:id>/edit', EditDev.as_view(), name='edit_device'),
    path('device/<int:id>/update', views.EditDev.as_view(), name='update_device'),
    path('device/<int:id>/destroy', views.DeleteDev),

]