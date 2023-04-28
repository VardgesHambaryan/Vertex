from django.contrib import admin
from .models import (
    Introduction,   OurService,   SingleService,
    OurGallery,     About,        ContactUs,
    Opinion,        BackGround,
)

@admin.register(Introduction)
class IntroductionModelAdmin(admin.ModelAdmin):
    list_display = ('title' , 'date')
    list_display_links = ('title' , 'date')
    search_fields = ('title' , 'txt')

@admin.register(OurService)
class OurServicesModelAdmin(admin.ModelAdmin):
    list_display = ('title' , )
    list_display_links = ('title' , )
    search_fields = ('title' , 'txt1' , 'txt2')

admin.site.register(SingleService)

@admin.register(OurGallery)
class OurGalleryModelAdmin(admin.ModelAdmin):
    list_display = ('title' , 'name')
    list_display_links = ('title' , 'name')
    search_fields = ('title' , 'name')


@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('title' ,)
    list_display_links = ('title' ,)
    search_fields = ('title' ,)


@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('title' ,)
    list_display_links = ('title' ,)
    search_fields = ('title' , 'txt')


@admin.register(Opinion)
class OpinionModelAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email')
    list_display_links = ('name' , 'email')
    search_fields  = ('name' , 'email' , 'message')

admin.site.register(BackGround)