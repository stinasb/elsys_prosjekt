from django.urls import path


from . import views

app_name = 'punkt'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:punkt_id>/', views.detail, name = 'detail'),
]