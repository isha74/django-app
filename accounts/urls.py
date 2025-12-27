<<<<<<< HEAD
# connects url routes to view- if someone visit this url, run this

from django.urls import path
from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),  # send req to reg API
    path('login/', LoginAPI.as_view()),        # send req to login API
]

from .views import register_page, login_page

urlpatterns += [
    path('register-page/', register_page),
    path('login-page/', login_page),
]
=======
from django.urls import path
from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
>>>>>>> 3f85a9bbd5836cfdf73939b78cbc06714c794b70
