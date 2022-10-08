from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", login_required(views.lista_password), name='index'),
    path("password/create", login_required(views.create_new_password), name='create_new_password'),
    path("password/view", login_required(views.view_password), name='view_password'),
    path("password/update", login_required(views.update_password), name='update_password'),
    path("password/delete", login_required(views.delete_password), name='delete_password'),
]