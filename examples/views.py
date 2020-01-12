from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView,
                                           BSModalLoginView)
from .forms import UserLoginForm, UserRegisterForm
from .forms import DeviceForm, CustomerForm, CustomerDeviceForm, CommandForm
from .models import Device, Customer, CustomerDevice
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, get_user_model, login, logout)


class Home(generic.ListView):
    context_object_name = 'title'
    template_name = 'home.html'

    def get_queryset(self):
        return 'WELCOME TO MANNAI COMMAND CENTER'


class Profile(generic.ListView):
    context_object_name = 'title'
    template_name = 'profile.html'

    def get_queryset(self):
        return 'WELCOME TO MANNAI COMMAND CENTER'


class DeviceIndex(generic.ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'indexDevice.html'


class DeviceCreateView(BSModalCreateView):
    template_name = 'devices/create_device.html'
    form_class = DeviceForm
    success_message = 'Success: Device was created.'
    success_url = reverse_lazy('indexDevice')


class DeviceUpdateView(BSModalUpdateView):
    model = Device
    template_name = 'devices/update_device.html'
    form_class = DeviceForm
    success_message = 'Success: Device was updated.'
    success_url = reverse_lazy('indexDevice')


class DeviceReadView(BSModalReadView):
    model = Device
    template_name = 'devices/read_device.html'


class DeviceDeleteView(BSModalDeleteView):
    model = Device
    template_name = 'devices/delete_device.html'
    success_message = 'Success: Device was deleted.'
    success_url = reverse_lazy('indexDevice')


class CustomerIndex(generic.ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'indexCustomer.html'


class CustomerCreateView(BSModalCreateView):
    template_name = 'customers/create_customer.html'
    form_class = CustomerForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('indexCustomer')


class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'customers/update_customer.html'
    form_class = CustomerForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('indexCustomer')


class CustomerReadView(BSModalReadView):
    model = Customer
    template_name = 'customers/read_customer.html'


class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('indexCustomer')

# Customer Device Model

class CustomerDeviceIndex(generic.ListView):
    model = CustomerDevice
    context_object_name = 'customerdevices'
    template_name = 'indexCustomerDevice.html'


class CustomerDeviceCreateView(BSModalCreateView):
    template_name = 'customerdevices/create_customerdevice.html'
    form_class = CustomerDeviceForm
    success_message = 'Success: Customer Device was created.'
    success_url = reverse_lazy('indexCustomerDevice')


class CustomerDeviceUpdateView(BSModalUpdateView):
    model = CustomerDevice
    template_name = 'customerdevices/update_customerdevice.html'
    form_class = CustomerDeviceForm
    success_message = 'Success: Customer Device was updated.'
    success_url = reverse_lazy('indexCustomerDevice')


class CustomerDeviceReadView(BSModalReadView):
    model = CustomerDevice
    template_name = 'customerdevices/read_customerdevice.html'


class CustomerDeviceDeleteView(BSModalDeleteView):
    model = CustomerDevice
    template_name = 'customerdevices/delete_customerdevice.html'
    success_message = 'Success: Customer Device was deleted.'
    success_url = reverse_lazy('indexCustomerDevice')

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/profile')

    context = {
        'form': form,
    }
    return render(request, "authentication/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/login/')

    context = {
        'form': form,
    }
    return render(request, "authentication/signup.html", context)


class logout_view(generic.ListView):
    context_object_name = 'title'
    template_name = 'logout.html'

    def get_queryset(self):
        return 'Logged Out'

def logout_Final(request):
    logout(request)
    return redirect('/home/')


class DeviceExecute(generic.ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'connect.html'


class DeviceExecuteView(BSModalUpdateView):
    model = Device
    template_name = 'devices/execute_device.html'
    form_class = CommandForm
    success_message = 'Success: execute was updated.'
    success_url = reverse_lazy('indexDevice')

def connection_manage(request):
    if request.method == "POST":
        form = CommandForm(request.POST)
        if form.is_valid():
            from netmiko import ConnectHandler
            device = {}
            device['device_type'] = 'cisco_ios'
            device['ip'] = 'DESKTOP-CT4RSIT'
            device['username'] = ''
            device['password'] = ''
            cmd = request.POST.get('command', '')
            conn = ConnectHandler(**device)
            output = conn.send_command(cmd)
            return render(request, 'connect.html', {'form': form, 'output': output})
    else:
        form = CommandForm()
        return render(request, 'connect.html', {'form': form})
        
