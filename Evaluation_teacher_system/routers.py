from django.urls import path
from rest_framework.routers import SimpleRouter

from Evaluation_teacher_system.rating.viewsets import CreateRatingViewSet, ListRatingViewSet
from Evaluation_teacher_system.user.viewsets import UserViewSet
from Evaluation_teacher_system.college.viewsets import CreateCollegeViewSet, ListCollegeViewSet
from Evaluation_teacher_system.subject.viewsets import CreateSubjectViewSet, ListSubjectViewSet
from Evaluation_teacher_system.teacher.viewsets import CreateTeacherViewSet, ListTeacherViewSet, GetTeacherViewSet
from Evaluation_teacher_system.Authentication.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# COLLEGE

routes.register(r'college/create', CreateCollegeViewSet, basename='college-create')
routes.register(r'college/list', ListCollegeViewSet, basename='college-list')

# TEACHER

routes.register(r'teacher/create', CreateTeacherViewSet, basename='teacher-create')
routes.register(r'teacher/list', ListTeacherViewSet, basename='teacher-list')
routes.register(r'teacher/get', GetTeacherViewSet, basename='teacher-get')

# SUBJECT

routes.register(r'subject/create', CreateSubjectViewSet, basename='subject-create')
routes.register(r'subject/list', ListSubjectViewSet, basename='subject-list')

# RATING

routes.register(r'rating/create', CreateRatingViewSet, basename='rating-create')
routes.register(r'rating/list', ListRatingViewSet, basename='rating-list')

urlpatterns = [
    *routes.urls,
]
