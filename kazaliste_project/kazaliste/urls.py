from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.edit_profile, name='profile'),
    path('predstave/', views.predstave_list, name='predstave_list'),
    path('predstave/<int:pk>/', views.predstava_detail, name='predstava_detail'),
]
