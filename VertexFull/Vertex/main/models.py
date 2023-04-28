from typing import Any
from django.db import models

# Create your models here.
class Introduction(models.Model):

    img = models.ImageField('Blog Image: ', upload_to='media')
    title = models.CharField('Blog Title: ', max_length=255)
    txt = models.TextField('Blog Text: ')
    date = models.DateField('Blog adding time: ')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'Introductions'

class OurService(models.Model):
    title = models.CharField('Services Title: ', max_length=255)
    txt1 = models.TextField('First Text: ')
    txt2 = models.TextField('Second Text: ')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'OurService'
        verbose_name_plural = 'OurServices'

class SingleService(models.Model):

    icon_link = models.CharField('Icon name ', max_length=255)
    txt = models.TextField('Text ')

    def __str__(self) -> str:
        return 'Single Service'
    
    class Meta:
        verbose_name = 'SingleService'
        verbose_name_plural = 'SingleService'

class OurGallery(models.Model):
    img_tn = models.ImageField('Image ' , upload_to='media', null=True)
    img = models.ImageField('Image ' , upload_to='media')

    title = models.CharField('Title', max_length=50)
    name = models.CharField('Name ', max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'OurGallery'
        verbose_name_plural = 'OurGalleries'

class About(models.Model):
    title = models.CharField('Title', max_length=50)
    txt1 = models.TextField('First Text: ')
    txt2 = models.TextField('Second Text: ')
    txt3 = models.TextField('Third Text: ')

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class ContactUs(models.Model):
    title = models.CharField('Title' , max_length=25)
    txt = models.TextField('Text: ') 


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'ContactUs'    
        verbose_name_plural = 'ContactUs'     

class Opinion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opinions'

class BackGround(models.Model):
    img1 = models.ImageField('Image 1',upload_to='media')
    img2 = models.ImageField('Image 2',upload_to='media')
    img3 = models.ImageField('Image 3',upload_to='media')
    img4 = models.ImageField('Image 4',upload_to='media')

    def __str__(self) -> str:
        return 'BackGround'
    
    class Meta:
        verbose_name = 'BackGround'
        verbose_name_plural = 'BackGrounds'
