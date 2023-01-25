from django.db import models


class Main(models.Model):

    title = models.CharField('Название профессии', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', blank=True, upload_to='pictures/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class DemandChart(models.Model):

    title = models.CharField('Название графика', max_length=100)
    image = models.ImageField('График', upload_to='charts/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'График востребованности'
        verbose_name_plural = 'Графики востребованности'


class GeoChart(models.Model):

    title = models.CharField('Название графика', max_length=100)
    image = models.ImageField('График', upload_to='charts/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'График географии'
        verbose_name_plural = 'Графики географии'


class Skills(models.Model):

    year = models.CharField('Год', max_length=4)
    skills = models.TextField('Навыки')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Ключевой навыки'
        verbose_name_plural = 'Ключевый навыки'
