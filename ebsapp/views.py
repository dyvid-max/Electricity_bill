from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Customer, Connection, Bill, Payment
from .forms import CustomerForm, ConnectionForm, BillForm, PaymentForm

@login_required
def dashboard(request):
    total_customers = Customer.objects.count()
    total_connections = Connection.objects.count()
    total_bills = Bill.objects.count()
    
    context = {
        'total_customers': total_customers,
        'total_connections': total_connections,
        'total_bills': total_bills,
    }
    return render(request, 'billing/dashboard.html', context)

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'billing/customer_list.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'billing/add_customer.html', {'form': form})

@login_required
def connection_list(request):
    connections = Connection.objects.all()
    return render(request, 'billing/connection_list.html', {'connections': connections})

@login_required
def add_connection(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connection_list')
    else:
        form = ConnectionForm()
    return render(request, 'billing/add_connection.html', {'form': form})

@login_required
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

@login_required
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/add_bill.html', {'form': form})

def payment(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.bill = bill
            payment.amount = bill.calculate_total()
            payment.save()
            
            # Mark bill as paid
            bill.is_paid = True
            bill.save()
            
            return redirect('payment_success')
    else:
        form = PaymentForm()
    
    context = {
        'bill': bill,
        'form': form,
        'amount': bill.calculate_total()
    }
    return render(request, 'billing/payment.html', context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'billing/login.html', {'error': 'Invalid credentials'})
    return render(request, 'billing/login.html')

@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')