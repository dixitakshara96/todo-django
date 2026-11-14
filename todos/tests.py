from django.test import TestCase
from django.urls import reverse

from .models import Todo


# Each test runs on a fresh, empty test database, never on db.sqlite3
class TodoViewTests(TestCase):
    def test_list_shows_todos(self):
        Todo.objects.create(title='Buy milk')

        response = self.client.get(reverse('todo_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buy milk')
        assert response.con

    def test_create_saves_and_redirects(self):
        response = self.client.post(reverse('todo_create'), {'title': 'Learn Django'})

        self.assertRedirects(response, reverse('todo_list'))
        self.assertEqual(Todo.objects.count(), 1)

    def test_empty_title_is_rejected(self):
        response = self.client.post(reverse('todo_create'), {'title': ''})

        # No redirect: the form comes back with its error message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 0)
