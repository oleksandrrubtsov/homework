from django.test import TestCase
from note.models import Stuff, Task, Post

class StuffTestCase(TestCase): 
    def setUp(self):
        Stuff.objects.create(first_name='Oleksandr',last_name='Rubtsov',city='Kyiv')
        Stuff.objects.create(first_name='Eduard',last_name='Rubtsov',city='Kharkiv')

        

    def test_creation(self):
        stuff1 = Stuff.objects.get(first_name='Oleksandr')
        stuff2 = Stuff.objects.get(first_name='Eduard')
        self.assertEqual(stuff1.last_name,"Rubtsov")
        self.assertEqual(stuff2.last_name,"Rubtsov")
        self.assertEqual(stuff1.city,"Kyiv")
        self.assertEqual(stuff2.city,"Kharkiv")



class TaskTestCase(TestCase):
    def setUp(self) -> None:
        Task.objects.create(title='Buy groceries', description = 'Mils, eggs, bread')
        
    def test1_creation(self):
        task1 = Task.objects.get(title= "Buy groceries")
        self.assertEqual(task1.description, "Mils, eggs, bread")






class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_content(self):
        post1 = Post.objects.get(id=1)
        expected_content = 'This is a test post.'
        self.assertEqual(post1.content, expected_content)

    def test_post_str_representation(self):
        post = Post.objects.get(id=1)
        expected_str = 'Test Post'
        self.assertEqual(str(post), expected_str)