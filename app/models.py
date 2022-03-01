from email.mime import image
from django.db import models
from datetime import datetime
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from crum import get_current_user   
# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User







class KidTable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()


class ImageTable(models.Model):
    kid = models.ForeignKey(KidTable, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)
    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}" width="150" height="150" />')

    image_tag.short_description = 'Image'

    created_on = models.DateTimeField(default = datetime.now)
    updated_on = models.DateTimeField(default=datetime.now)
    is_approved = models.BooleanField(default=False)
    approved_by  = models.CharField(max_length=100)
    FOOD_CHOICES = [
        ('veg', 'Veg'),
        ('fruit', 'Fruit'),
        ('grain', 'Grain'),
        ('protein', 'Protein'),
        ('dairy', 'Dairy'),
        ('condiment', 'Condiment'),
        ('unknown', 'Unknown')
    ]
    Food_group =   models.CharField(
        max_length=30,
        choices=FOOD_CHOICES,
        default='veg',
    )


def send_email(sender, **kwargs):
    if kwargs['instance'].Food_group == 'unknown':
        email_subject = 'Unknown image added'
        htmlgen = f"You have added unknown image. Please check the image and add it to the database."
        print('hi', kwargs['instance'].kid.name)
        print(send_mail( email_subject, htmlgen, settings.EMAIL_HOST_USER, [kwargs['instance'].kid.email], fail_silently=False))
post_save.connect(send_email, sender=ImageTable)




