from django.db import models


class Device(models.Model):
    CISCO1 = 1
    CISCO2 = 2
    CISCO3 = 3
    CISCO4 = 4
    DEVICE_TYPES = (
        (CISCO1, 'cisco_ios'),
        (CISCO2, 'cisco_nxos_ssh'),
        (CISCO3, 'cisco_s300'),
        (CISCO4, 'cisco_tp_tcce'),
    )
    device_name = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    IP_address = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPES)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.device_name

class Customer(models.Model):
    STATE = 1
    STATE_TYPES = (
        (STATE, 'doha'),
    )

    CITY1 = 1
    CITY2 = 2
    CITY3 = 3
    CITY4 = 4
    CITY5 = 5
    CITY6 = 6
    CITY7 = 7
    CITY8 = 8
    CITY9 = 9
    CITY10 = 10
    CITY_TYPES = (
        (CITY1, 'Abu Hamour'),
        (CITY2, 'Ain Khaled'),
        (CITY3, 'Bu Samra'),
        (CITY4, 'Al Dafna'),
        (CITY5, 'Fereej Bin Mahmoud'),
        (CITY6, 'Freej Al Murra'),
        (CITY7, 'Al Gharrafa'),
        (CITY8, 'Al Hilal'),
        (CITY9, 'Al Jeryan'),
        (CITY10,'Al Khor'),
    )
    customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    users_name = models.CharField(max_length=50)
    state_type = models.PositiveSmallIntegerField(choices=STATE_TYPES)
    city_type = models.PositiveSmallIntegerField(choices=CITY_TYPES)

    def __str__(self):
        return self.customer_name

class CustomerDevice(models.Model):
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)