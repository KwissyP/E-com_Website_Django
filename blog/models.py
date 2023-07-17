from django.db import models
from user.models import User
from django.urls import reverse
from django.utils import timezone

class CategoryArticle(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    description = models.TextField()
    category = models.ForeignKey(CategoryArticle, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_article', args=[str(self.id)])
    
    def get_comment_count(self):
        return self.note2_set.count()

class Note2(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser2', null=True, blank=True, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    text = models.TextField(max_length=300, default='valeur_par_défaut')
    created_at = models.DateTimeField(default=timezone.now)

class AnonymousUser2(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
