from blog.models import Category
from django.test import TestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
# Create your tests here.
class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username="username1",password="test123")
        testpost = Post.objects.create(category_id = 2 ,title = 'post',excerpt='post',content='post',author_id=1, slug='post-title',status='published')