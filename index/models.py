from django.db import models
from django.utils.translation import gettext_lazy  as _
# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=300,blank=True, null=True,verbose_name=_("Name"))
    email=models.EmailField(max_length=700,blank=True, null=True,verbose_name=_("Email"))
    subject=models.CharField(max_length=800,blank=True, null=True,verbose_name=_("Subject"))
    message=models.TextField(max_length=1000,blank=True, null=True,verbose_name=_("Message"))
    

    class Meta:
        verbose_name = 'Contact Me'
        verbose_name_plural = 'Contact Us'


    def __str__(self):
        return self.name
    



