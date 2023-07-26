from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from books.models import Book


# Create your tests here.

class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.books=Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isnb="9781735467221",
            )

    def test_api_listview(self):
        response=self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.books)    

