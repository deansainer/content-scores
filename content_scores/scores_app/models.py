from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Content_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Score(models.Model):
    score_num = models.FloatField()

    def __str__(self):
        return f'{self.score_num}'


class Content(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_type = models.ForeignKey(Content_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
