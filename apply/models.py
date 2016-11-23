from django.db import models
from transliterate import translit
from slugify import slugify


def ruslugify(smth):
    return slugify(translit(smth, 'ru', reversed=True))

def upload_location(instance, filename):
    return "%s_%s/%s" % (ruslugify(instance.second_name), ruslugify(instance.first_name), filename)

class Apply(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    email = models.CharField("Почта", blank=True, max_length=100)
    attachments = models.FileField("Проект", blank=True, upload_to=upload_location)
    attachment_02 = models.FileField(blank=True, upload_to=upload_location)
    attachment_03 = models.FileField(blank=True, upload_to=upload_location)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)

# Create your models here.
