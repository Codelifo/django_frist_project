from django.urls import path
from first_app.views import home,addTask,ShowTask,editTask,DeleteTask,CompTask
urlpatterns = [
    path('', home,name='home'),
    path('add_task/', addTask, name='add_task'),
    path('show_task/', ShowTask, name='show_task'),
    path('edit_task/<int:id>', editTask, name='edit_task'),
    path('Delete_Task/<int:id>', DeleteTask, name='Delete_Task'),
    path('complated_Task/<int:id>', CompTask, name='comp_Task'),
]
