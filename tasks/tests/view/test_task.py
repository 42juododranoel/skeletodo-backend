import pytest

pytestmark = [pytest.mark.django_db]


def test_task_list_empty(heman):
    response = heman.get('/tasks/')

    assert response.status_code == 200
    assert 'No tasks are available' in response.text


def test_task_list_not_empty_after_creating_task(heman, task):
    task.update(text='foobarbaz')

    response = heman.get('/tasks/')

    assert 'foobarbaz' in response.text


def test_task_list_redirect_when_anon(anon):
    response = anon.get('/tasks/')

    assert response.status_code == 302


def test_task_create_redirect_when_anon(anon):
    response = anon.get('/tasks/create/')

    assert response.status_code == 302


def test_task_detail_redirect_when_anon(anon, task):
    response = anon.get(f'/tasks/{task.id}/')

    assert response.status_code == 302


def test_task_delete_redirect_when_anon(anon, task):
    response = anon.get(f'/tasks/{task.id}/delete/')

    assert response.status_code == 302
