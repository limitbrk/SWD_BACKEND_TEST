from django.urls import path
from todo import views

urlpatterns = [

    # ========== API Endpoints ==================================+++++++++++++++=======================================
   path("", views.TodoAPIView.as_view(), name="todolist"),
   path("<int:id>", views.TodoWithIDAPIView.as_view(), name="todolist"),
]