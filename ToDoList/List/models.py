from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    text = models.TextField('Текст', blank=True)
    is_done = models.BooleanField(default=False)
    pub_date = models.DateTimeField('Время создания', auto_now_add=True)

    def make_it_done(self):
        self.is_done = True

    def make_it_undone(self):
        self.is_done = False

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
