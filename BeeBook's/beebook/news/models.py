from django.db import models # type: ignore

class Articles(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text =  models.TextField("Сатья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'