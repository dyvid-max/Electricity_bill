from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Connection(models.Model):
    # Define connection types at the class level
    CONNECTION_TYPES = (
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    connection_id = models.CharField(max_length=10, unique=True)
    connection_type = models.CharField(max_length=20, choices=CONNECTION_TYPES)
    start_date = models.DateField()
    occupation = models.CharField(max_length=100)
    load = models.DecimalField(max_digits=10, decimal_places=2)
    plot_no = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.connection_id} - {self.customer}"

class Bill(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    consumer_id = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    previous_reading = models.DecimalField(max_digits=10, decimal_places=2)
    total_units = models.DecimalField(max_digits=10, decimal_places=2)
    charge_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def calculate_total(self):
        return self.total_units * self.charge_per_unit
    
    def __str__(self):
        return f"Bill {self.id} for {self.connection.customer}"

class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=10)
    cvc = models.CharField(max_length=4)
    
    def __str__(self):
        return f"Payment for Bill {self.bill.id}"