from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name="index"),
    path('create/', views.create_student_view, name="create_student"),
    path('view/', views.view_student_view, name="view_student"),
    path('view/<int:id>', views.view_student_one_view, name="view_student_one"),
    path('delete/<int:id>', views.delete_student_view, name="delete_student_view"),
]