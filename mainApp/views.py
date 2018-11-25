from django.shortcuts import render

def index (request):
    return render(request, 'mainApp/homepage.html')

def contact (request):
    return render(request, 'mainApp/basic.html', {'values': ['За детальною інформацією телефонуйте:', '(066) 055 33 22']})

