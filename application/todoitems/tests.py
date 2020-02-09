import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def todoitem():
    return mixer.blend('todoitems.Todoitem')


def test_text_not_longer_than_4096(todoitem):
    with pytest.raises(ValidationError) as exception:
        todoitem.update(text=('ツ' * 4097))

    assert exception.value.message_dict['text'][0] \
        == 'Ensure this value has at most 4096 characters (it has 4097).'


@pytest.mark.parametrize(
    'value, message',
    [
        ['', 'This field cannot be blank.'],
        [None, 'This field cannot be null.'],
    ]
)
def test_text_cant_be_empty(todoitem, value, message):
    with pytest.raises(ValidationError) as exception:
        todoitem.update(text=value)

    assert exception.value.message_dict['text'][0] == message
