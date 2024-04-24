from fighter.views import *
from user.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ufc-fighter-vs-api', ufc_fighter_API)

urlpatterns = [
    path('hello', hello.as_view()),
    path('ufc_fighter', ufc_fighter_api),
    path('ufc_fighters', ufc_fighters_api),
    path('ufc_fighter/<id>', ufc_fighter_by_id_api),
    path('ufc_fighter/search/<search_param>', search_ufc_fighter.as_view()),
    path('', include(router.urls)),
    path('user-register', user_register_api.as_view()),
    path('user-login', user_login_api.as_view()),
    path('auth-check', authenticated_check_API.as_view()),
    path('register-ufc-fighter', register_ufc_fighter_api.as_view()),
    path('weight-division/<id>', weight_division_api.as_view())
]