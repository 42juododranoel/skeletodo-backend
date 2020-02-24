import pytest

pytestmark = [pytest.mark.django_db]


def test_task_list_empty(heman):
    response = heman.get('/tasks/')

    assert response.status_code == 200
    assert '<p>No tasks are available.</p>' in response.text


def test_task_list_not_empty_after_creating_task(heman, task):
    task.update(text='foobarbaz')

    response = heman.get('/tasks/')

    assert 'foobarbaz' in response.text


def test_task_list_redirect_when_anon(anon):
    response = anon.get('/tasks/')

    assert response.status_code == 302


def test_create_task_get(heman):
    response = heman.get('/tasks/create/')

    assert response.status_code == 200
    assert '<form method="post">' in response.text


def test_create_task_post_redirect_to_detail(heman):
    response = heman.post('/tasks/create/', {'text': 'foobarbaz'}, follow=True)

    assert response.status_code == 200
    assert 'foobarbaz' in response.text
    assert response.redirect_chain == [('/tasks/1/', 302)]


def test_create_task_redirect_when_anon(anon):
    response = anon.get('/tasks/create/')

    assert response.status_code == 302


def test_task_detail_get(heman, task):
    task.update(text='foobarbaz')

    response = heman.get('/tasks/1/')

    assert response.status_code == 200
    assert 'foobarbaz' in response.text


def test_task_detail_redirect_when_anon(anon, task):
    response = anon.get('/tasks/1/')

    assert response.status_code == 302


def test_delete_task_get(heman, task):
    response = heman.get('/tasks/1/delete/')

    assert response.status_code == 200
    assert '<form method="post">' in response.text


def test_delete_task_post_redirect_to_list(heman, task):
    response = heman.post('/tasks/1/delete/', follow=True)

    assert response.status_code == 200
    assert '<p>No tasks are available.</p>' in response.text
    assert response.redirect_chain == [('/tasks/', 302)]


def test_task_delete_redirect_when_anon(anon, task):
    response = anon.get('/tasks/1/delete/')

    assert response.status_code == 302
