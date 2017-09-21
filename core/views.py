from django.shortcuts import render

def get_template(request):
  if request.user.is_authenticated():
    base_template = 'base_auth.html'
  else:
    base_template = 'base_not_auth.html'

  return base_template

def index(request):
  return render(request, 'index.html', {'base_template': get_template(request)})

def employees(request):
  return render(request, 'employees.html', {'base_template': get_template(request)})

def clients(request):
  return render(request, 'clients.html', {'base_template': get_template(request)})

def products(request):
  return render(request, 'products.html', {'base_template': get_template(request)})

def sales(request):
  return render(request, 'sales.html', {'base_template': get_template(request)})