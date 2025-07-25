from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import attendance_chart, employee_logs
urlpatterns = [
    path('capture_Employee/', views.capture_Employee, name='capture_Employee'),
    path('', views.home, name='home'),
    path('selfie-success/', views.selfie_success, name='selfie_success'),
    path('capture-and-recognize/', views.capture_and_recognize, name='capture_and_recognize'),
    path('Employees/attendance/', views.Employee_attendance_list, name='Employee_attendance_list'),
    path('Employees/', views.Employee_list, name='Employee-list'),
    path('Employees/<int:pk>/', views.Employee_detail, name='Employee-detail'),
    path('Employees/<int:pk>/authorize/', views.Employee_authorize, name='Employee-authorize'),
    path('Employees/<int:pk>/delete/', views.Employee_delete, name='Employee-delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('camera-config/', views.camera_config_create, name='camera_config_create'),
    path('camera-config/list/', views.camera_config_list, name='camera_config_list'),
    path('camera-config/update/<int:pk>/', views.camera_config_update, name='camera_config_update'),
    path('camera-config/delete/<int:pk>/', views.camera_config_delete, name='camera_config_delete'),
    path('attendance-chart/', views.attendance_chart, name='attendance_chart'),
 path('User_login/', views.employee_login, name='employee_login'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('logout1/', views.logout_view, name='logout1'),
path('logs/<str:emp_id>/',views.employee_logs, name='employee_logs'),
path('check-employee-id/', views.check_employee_id, name='check_employee_id'),
]
    

