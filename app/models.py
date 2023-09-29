from django.db import models

class Event(models.Model):

    title = models.CharField('Имя события', max_length=256, default='Событие')
    description = models.TextField('Описание события', blank=True, null=True)
    date = models.DateField('Дата события', auto_now=True)
    is_important = models.BooleanField('Важность события', default=False)
    image = models.ImageField('Фото события', upload_to='event-images')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'