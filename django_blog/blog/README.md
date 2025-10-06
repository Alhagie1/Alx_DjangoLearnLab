This is a project name django_blog with an app name blog
Models: 
 The Post model with attributes such as:
 title, content, author and published date

 The Profil model  which is inheriting from the Django user model and it comes added attributes such as:
 bio which represent the biography of the user
 date_of_birth
 location
 created_at
 updated_at
 phone_number 
 profile_picture

The views.py file consist of some of view functions
login_view(), logout(), register_view() and profile_view()
which handle user login, logout, user registration and  user profile management.


Blog Post Management:

Class Base Views:
PostCreateView,
PostListview,
PostUpdateView,
PostDeleteView.


It involves the CRUD operations 

A login user can create post, edit post and delete post

A normal user can view posts from PostListView class