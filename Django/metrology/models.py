from django.db import models
from django.urls import reverse


class Metrology(models.Model):
    organisation = models.CharField(max_length=150, verbose_name="Наименование")
    name_SI = models.TextField(verbose_name="Наименование типа СИ")
    registration_number = models.TextField(blank=True, verbose_name="Регистрационный номер")
    data_Power = models.DateTimeField(auto_now_add=True, verbose_name="Дата поверки")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def get_absolute_url(self):
        return reverse('', kwargs={"pk": self.pk})

    def __str__(self):
        return self.organisation
        return self.photo

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
        ordering = ['-data_Power']

class Offers(models.Model):
    organisation = models.CharField(max_length=150, verbose_name="Наименование услуги")
    name_SI = models.TextField(verbose_name="Номер услуги")
    is_published = models.BooleanField(default=False, verbose_name="Публикация")

    class Meta:
        verbose_name = "Очередь"
        verbose_name_plural = "Очередь"
        ordering = ['organisation']