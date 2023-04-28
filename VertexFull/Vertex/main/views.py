from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import (
    Introduction,         OurService,          SingleService,
    OurGallery,           About,                ContactUs,
    Opinion, BackGround
)
from .forms import OpinionForm
from django.urls import re_path
from django.core.mail import EmailMessage
from Vertex.settings import EMAIL_HOST_USER



class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        intros = Introduction.objects.all()
        services = OurService.objects.get()
        single_service = SingleService.objects.all()
        galleries = OurGallery.objects.all()
        about = About.objects.get()
        contact_us =  ContactUs.objects.get()
        bg = BackGround.objects.get()

        return render(request , self.template_name,
                      {
                        'intros':intros,
                        'services':services,
                        'single_service':single_service,
                        'galleries':galleries,
                        'about':about,
                        'contact_us': contact_us,
                        'bg':bg,
                      })
    
    def post(self ,request):
        if request.method == "POST":
            form = OpinionForm(request.POST)
            subject = f"Նոր Նամակ Vertex - ից"

            body = 'Ձեր կարծիքը կարևոր է մեզ համար'
            try:
                email = EmailMessage(
                subject = subject,
                body = body,
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')],
                )
                email.send()
            except Exception:
                pass

        if form.is_valid():
            Opinion.objects.create(**form.cleaned_data)
            return redirect('/')
        else:
            form = OpinionForm()

        return render(request , self.template_name , {'form':form})
    






