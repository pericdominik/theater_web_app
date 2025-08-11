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
    path('calendar/', views.calendar_week, name='calendar_week'),
    path('predstave/<int:pk>/like/add/', views.like_add, name='predstava_like_add'),
    path('predstave/<int:pk>/like/remove/', views.like_remove, name='predstava_like_remove'),
]
