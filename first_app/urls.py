from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.users,name='users'),
    path('',views.other,name='other'),
    path('',views.relative,name='relative')
]
