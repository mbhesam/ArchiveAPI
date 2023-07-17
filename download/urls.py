from django.urls import path
from download.views import File
urlpatterns = [
    path('<path:file_path>',File.as_view()),
]

