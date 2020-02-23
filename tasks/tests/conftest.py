import pytest
from django.test import Client
from mixer.backend.django import mixer


class TextResponseClient(Client):
    """Django test client with `.text` attribute in responses."""

    def request(self, **request):
        """Call super request method and add `.text` attribute to response."""
        response = super().request(**request)
        response.text = response.content.decode()
        return response


@pytest.fixture
def task():
    return mixer.blend('tasks.Task')


@pytest.fixture
def anon():
    """Use as `client` replacement when no authentication is required."""
    client = TextResponseClient()
    return client


@pytest.fixture
def heman(anon):
    """Use as `client` replacement when authenticated user is required."""
    anon.user = mixer.blend('auth.User')
    anon.force_login(user=anon.user)
    return anon


@pytest.fixture
def shera(anon):
    """Use as `client` replacement when not He-man user is required."""
    anon.user = mixer.blend('auth.User')
    anon.force_login(user=anon.user)
    return anon
