from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes, name = 'home'),
    path('notes/', views.notes , name= 'notes'),
    path('notes/create/' , views.createNote, name = 'create'),
    path('notes/<str:pk>/', views.getNote, name= 'id'),
    path('notes/<str:pk>/update/', views.updateNote, name = 'update'),
    path('notes/<str:pk>/delete/', views.deleteNote, name = 'delete')
]