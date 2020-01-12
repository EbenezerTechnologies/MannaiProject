from django.urls import path
from . import views
from examples.views import login_view, register_view, logout_view, logout_Final,connection_manage

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('profile/', views.Profile.as_view(), name='profile'),
    # Device URL

    path('device', views.DeviceIndex.as_view(), name='indexDevice'),
    path('created/', views.DeviceCreateView.as_view(), name='create_device'),
    path('updated/<int:pk>', views.DeviceUpdateView.as_view(), name='update_device'),
    path('readd/<int:pk>', views.DeviceReadView.as_view(), name='read_device'),
    path('deleted/<int:pk>', views.DeviceDeleteView.as_view(), name='delete_device'),
    path('executec/<int:pk>', views.DeviceExecuteView.as_view(), name='execute_device'),

    # Customer URL
    path('customer', views.CustomerIndex.as_view(), name='indexCustomer'),
    path('createc/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('updatec/<int:pk>', views.CustomerUpdateView.as_view(), name='update_customer'),
    path('readc/<int:pk>', views.CustomerReadView.as_view(), name='read_customer'),
    path('deletec/<int:pk>', views.CustomerDeleteView.as_view(),name='delete_customer'),

    # Customer Device URL

    path('customerdevice', views.CustomerDeviceIndex.as_view(), name='indexCustomerDevice'),
    path('createcd/', views.CustomerDeviceCreateView.as_view(), name='create_customerdevice'),
    path('updatecd/<int:pk>', views.CustomerDeviceUpdateView.as_view(), name='update_customerdevice'),
    path('readcd/<int:pk>', views.CustomerDeviceReadView.as_view(), name='read_customerdevice'),
    path('deletecd/<int:pk>', views.CustomerDeviceDeleteView.as_view(),name='delete_customerdevice'),


    path('login/', login_view),
    path('register/', register_view),
    path('logout/', views.logout_view.as_view(), name='logout'),
    path('log/', logout_Final),
    
    path('execute/',connection_manage, name='execute_device'),
]
