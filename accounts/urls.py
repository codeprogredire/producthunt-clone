from django.urls import path

from . import views


urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),

    # Dont forget to change the route to home page later on.
    path('logout',views.logout, name='logout'),
]