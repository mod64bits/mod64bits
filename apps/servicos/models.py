from django.db import models
from django.db.models import signals


from core.signals import create_slug


class CategoriaServicos(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da Categoria', unique=True)
    descricao = models.CharField('Descrição', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=CategoriaServicos)


class Servicos(models.Model):
    servico = models.CharField('Nome', max_length=50, help_text='Nome da Categoria', unique=True)
    categoria_servico = models.ForeignKey(CategoriaServicos, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'servico'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


signals.post_save.connect(create_slug, sender=Servicos)
