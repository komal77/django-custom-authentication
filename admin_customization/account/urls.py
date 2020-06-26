from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('registration/', SignUpView.as_view(), name='registration' ),
    path('login/', LoginView.as_view(), name='login' ),
    path('profile/', ProfileView.as_view(), name='profile' ),
    # path('profile/<int:id>', ProfileView.as_view(), name='profile' ),
    # path('delete/<int:pk>', views.delete, name='delete'),
    path('logout/', LogoutView.as_view(), name='logout' ),
]