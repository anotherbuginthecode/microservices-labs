from django.urls import path

from .views import (
    RegisterView,
    ListUserView,
    SingleUserView,
    MeView)

urlpatterns = [
    path('', ListUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('<int:id>/', SingleUserView.as_view()),
    path('me/', MeView.as_view()),
]