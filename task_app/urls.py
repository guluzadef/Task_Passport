from django.urls import path, include
from .views import PassportApi,PersonCreate,PersontListApi,PassportListApi,PersonApi

urlpatterns = [

#     path('passport/', PassportCreate.as_view(), name='index'),
    path('person/', PersonCreate.as_view(), name='person-create'),
    path('person/<int:pk>', PersonApi.as_view(), name='person'),
    path('passport/<int:pk>', PassportApi.as_view(), name='passport'),
    path('personlist/', PersontListApi.as_view(), name='person-list'),
    path('passportlist/', PassportListApi.as_view(), name='passport-list')
]
