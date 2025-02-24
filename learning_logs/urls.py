"""define url mode of learning_logs"""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('',views.index,name = 'index'),
    # show all topics
    path('topics/',views.topics,name = 'topics'),
    # detail page special topic
    path('topics/<int:topic_id>/',views.topic,name = 'topic'),
    # add new topic
    path('new_topic/',views.new_topic,name = 'new_topic'),
    # add new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name = 'new_entry'),
    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]