"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/add_note/', views.add_note, name='add_note'),
    path('notes/<int:pk>/edit', views.edit_note, name='edit_note'),
    path('notes/<int:pk>/delete', views.delete_note, name='delete_note'),
    path('notes/search_notes', views.search_notes, name='search_notes'),
    path('notes/sort_notes', views.sort_notes, name='sort_notes'),
    path('notes/<int:pk>/add_comment', views.add_comment, name='add_comment'),
    path('admin/', admin.site.urls),
]
