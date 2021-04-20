from django.urls import path
# from task_manager_app.views import index
from .views import *

urlpatterns = [
    # path()
    path('register/', UserRegistrationApi.as_view()),
    path('users/', UserListApi.as_view()),

]
