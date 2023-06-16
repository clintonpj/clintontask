from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('new', views.new, name='new')

    # path('form_submission', views.form_submission, name='form_submission'),

]
