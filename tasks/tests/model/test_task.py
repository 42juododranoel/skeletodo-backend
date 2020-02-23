import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

pytestmark = [pytest.mark.django_db]


def test_text_not_longer_than_4096(task):
    with pytest.raises(ValidationError) as exception:
        task.update(text=('ツ' * 4097))

    assert exception.value.message_dict['text'][0] \
        == 'Ensure this value has at most 4096 characters (it has 4097).'


@pytest.mark.parametrize(
    'value, message',
    [
        ['', 'This field cannot be blank.'],
        [None, 'This field cannot be null.'],
    ]
)
def test_text_cant_be_empty(task, value, message):
    with pytest.raises(ValidationError) as exception:
        task.update(text=value)

    assert exception.value.message_dict['text'][0] == message


def test_task_has_user_foreign_key(task):
    assert isinstance(task.user, User)


def test_user_has_task_set(task):
    assert task in task.user.tasks.all()
