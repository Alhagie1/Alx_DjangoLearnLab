
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

# class RegistrationTests(TestCase):
#     def setUp(self):
#         self.client = Client()
    
#     def test_registration_page_loads(self):
#         response = self.client.get(reverse('register'))
#         self.assertEqual(response.status_code, 200)
    
#     def test_user_can_register(self):
#         response = self.client.post(reverse('register'), {
#             'username': 'newuser',
#             'email': 'new@example.com',
#             'password1': 'TestPass123!@#',
#             'password2': 'TestPass123!@#'
#         })
        
#         self.assertTrue(User.objects.filter(username='newuser').exists())
#         user = User.objects.get(username='newuser')
#         self.assertEqual(user.email, 'new@example.com')
#         self.assertEqual(response.status_code, 302)

# class LoginTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
    
#     def test_login_page_loads(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
    
#     def test_user_can_login(self):
#         response = self.client.post(reverse('login'), {
#             'username': 'testuser',
#             'password': 'testpass123'
#         })
        
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(response.wsgi_request.user.is_authenticated)

# class LogoutTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
    
#     def test_user_can_logout(self):
#         self.client.login(username='testuser', password='testpass123')
#         response = self.client.post(reverse('logout'))
#         self.assertEqual(response.status_code, 302)

# class ProfileTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
    
#     def test_profile_requires_login(self):
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 302)
    
#     def test_logged_in_user_can_view_profile(self):
#         from blog.models import Profile
#         Profile.objects.get_or_create(user=self.user)
        
#         self.client.login(username='testuser', password='testpass123')
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)

# The second test on the Post Model

class PostModelTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test post
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content here',
            author=self.user
        )
    
    def test_post_creation(self):
        """Test that post is created correctly"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertTrue(isinstance(self.post, Post))


class PostListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )
    
    def test_list_view_accessible_to_guest(self):
        """Test that guests can view post list"""
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    def test_list_view_accessible_to_logged_in_user(self):
        """Test that logged-in users can view post list"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )
    
    def test_detail_view_accessible_to_guest(self):
        """Test that guests can view post details"""
        response = self.client.get(
            reverse('blog:post-detail', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test content')


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_create_view_redirects_guest(self):
        """Test that guests are redirected to login"""
        response = self.client.get(reverse('blog:post-create'))
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertIn('/login/', response.url)
    
    def test_create_view_accessible_to_logged_in_user(self):
        """Test that logged-in users can access create form"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('blog:post-create'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_post_success(self):
        """Test that logged-in users can create posts"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('blog:post-create'), {
            'title': 'New Post',
            'content': 'New content here',
        })
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, 'New Post')
        self.assertEqual(Post.objects.first().author, self.user)


class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Original Title',
            content='Original content',
            author=self.user1
        )
    
    def test_update_view_redirects_guest(self):
        """Test that guests are redirected to login"""
        response = self.client.get(
            reverse('blog:post-update', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
    
    def test_update_view_accessible_to_author(self):
        """Test that author can access edit form"""
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(
            reverse('blog:post-update', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
    
    def test_update_view_blocked_for_non_author(self):
        """Test that non-authors cannot edit posts"""
        self.client.login(username='user2', password='testpass123')
        response = self.client.get(
            reverse('blog:post-update', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 302)  # Redirected
    
    def test_update_post_success(self):
        """Test that author can update their post"""
        self.client.login(username='user1', password='testpass123')
        response = self.client.post(
            reverse('blog:post-update', kwargs={'pk': self.post.pk}),
            {
                'title': 'Updated Title',
                'content': 'Updated content',
            }
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')


class PostDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user1
        )
    
    def test_delete_view_redirects_guest(self):
        """Test that guests are redirected to login"""
        response = self.client.get(
            reverse('blog:post-delete', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
    
    def test_delete_view_accessible_to_author(self):
        """Test that author can access delete confirmation"""
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(
            reverse('blog:post-delete', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
    
    def test_delete_view_blocked_for_non_author(self):
        """Test that non-authors cannot delete posts"""
        self.client.login(username='user2', password='testpass123')
        response = self.client.get(
            reverse('blog:post-delete', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 302)  # Redirected
    
    def test_delete_post_success(self):
        """Test that author can delete their post"""
        self.client.login(username='user1', password='testpass123')
        response = self.client.post(
            reverse('blog:post-delete', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(Post.objects.count(), 0)