# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify


def create_slug(sender, instance, signal, *args, **kwargs):
    # verifique se há id e atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        # obter informações de Slug
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        # salvar slug vazio
        if not getattr(instance, slug_name, None):
            # criar slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            # set slug
            setattr(instance, slug_name, slug)
            # save instance
            instance.save()
