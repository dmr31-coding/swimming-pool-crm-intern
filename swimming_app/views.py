from django.shortcuts import render

from . import models

from . import forms

# Create your views here.


# Home page
def home(request):
    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:3]
    return render(
        request, "bootstrap/home.html", {"banners": banners, "services": services}
    )


# PageDetail
def page_detail(request, id):
    page = models.Page.objects.get(id=id)
    return render(request, "bootstrap/page.html", {"page": page})


# FAQ
def faq_list(request):
    faq = models.Faq.objects.all()
    return render(request, "bootstrap/faq.html", {"faqs": faq})


# Enquiry
def enquiry(request):
    form = forms.EnquiryForm
    return render(request, "bootstrap/enquiry.html", {"form": form})
