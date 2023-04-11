from apiA.views import ViewAllStudents, StudentsDetails, ViewAllDepartment, ViewDepartmentDetails
from . import views

from django.urls import path

urlpatterns = [
    path('students/', views.ViewAllStudents.as_view(), name = 'student_list' ),
    path('students/<int:pk>/', views.StudentsDetails.as_view(), name = 'student_info' ),
    path('departments/', views.ViewAllDepartment.as_view(), name = 'department_list' ),
    path('departments/<str:pk>/', views.ViewDepartmentDetails.as_view(), name = 'department_info' ),
]