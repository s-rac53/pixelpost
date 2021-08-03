from django.shortcuts import render, get_object_or_404
from .models import Customer, Service, Work, Portfolio


def homepage(request):

    return render(request,'PPP/homepage.html')

def contact(request):

    if request.method == 'POST':
        customer = Customer()
        customer.fname = request.POST.get('fname')
        customer.lname = request.POST.get('lname')
        customer.extension = request.POST.get('countryCode')

        customer.number = request.POST.get('number')
        customer.email = request.POST.get('email')
        customer.description = request.POST.get('description')
        customer.location = request.POST.get('location')
        customer.company = request.POST.get('company')
        print(customer.fname)
        print("hi")
        customer.save()
        return render(request,'PPP/contact.html',{'message':'done'})


    return render(request,'PPP/contact.html',)



def about(request):

    return render(request,'PPP/aboutus.html',)


def services(request):

    services = Service.objects.all

    return render(request,'PPP/services.html',{'services':services})


def works(request):

    works = Work.objects.filter()

    return render(request,'PPP/works.html',{'works':works})  


def portflio(request):

    portfolios = Portfolio.objects.all

    return render(request,'PPP/portfolio.html',{'portfolios':portfolios})  
















