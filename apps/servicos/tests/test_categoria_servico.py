import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.servicos.models import CategoriaServicos
from core.django_assertions import assert_contains


@pytest.fixture
def categorias(db):
    return mommy.make(CategoriaServicos, 3)


@pytest.fixture
def resp(client, categorias):
    return client.get(reverse('servicos:lista_categoria_servicos'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_slug_categoria(resp, categorias):
    for cat in categorias:
        assert_contains(resp, cat.slug)


def test_link_edit_categoria(resp, categorias):
    for categoria in categorias:
        categoria_link = reverse('servicos:edtar_categoria_servicos', args=(categoria.slug,))
        assert_contains(resp, f'href="{categoria_link}"')


