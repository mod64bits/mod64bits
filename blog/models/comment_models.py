# Core Django imports.
from django.db import models
from django.utils import timezone

# Blog application imports.
from blog.models.article_models import Article


class Comment(models.Model):

    name = models.CharField("Nome", max_length=250, null=False, blank=False)
    email = models.EmailField()
    comment = models.TextField("Comentário", null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField("Aprovado?", default=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"Comment by {self.name} em {self.article}"
