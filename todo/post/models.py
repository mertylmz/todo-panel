from django.db import models
from django.urls import reverse




class Personel(models.Model):
    personel = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'personels'

    def __str__(self):
        return self.personel


class Post(models.Model):
    description = models.TextField(verbose_name='Yapılacak:')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad:')
    # title = models.CharField(max_length=200, verbose_name='Proje Adı 1:', null='true')
    # title2 = models.CharField(max_length=200, verbose_name='Proje Adı 2:', null='true')
    # description2 = models.TextField(verbose_name='Açıklama:')

    pname = models.ForeignKey(Personel, on_delete=models.CASCADE, null='true', verbose_name='Personel:')



    def __str__(self):
       return self.name

    def get_absolute_url(self):
      return reverse('post:detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})