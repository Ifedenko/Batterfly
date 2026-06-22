from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    service = models.CharField(max_length=100, verbose_name='Услуга')
    master = models.CharField(max_length=100, blank=True, verbose_name='Мастер')
    date = models.DateField(blank=True, null=True, verbose_name='Дата')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'