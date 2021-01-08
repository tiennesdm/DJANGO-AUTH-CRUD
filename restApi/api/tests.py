from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Book
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='first todo', subtitle='a body here', author='shubham mehta', isbn='hello' )

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEquals(expected_object_name, 'first todo')








