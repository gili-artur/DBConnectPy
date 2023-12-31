from django.db import models


# Create your models here.
class People(models.Model):
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=30)
    birthdate = models.DateField('Дата рождения')
    city = models.CharField('Город', max_length=20)
    telephone = models.CharField('Телефон', max_length=11, unique=True)

    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
