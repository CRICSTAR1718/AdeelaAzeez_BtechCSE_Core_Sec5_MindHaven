"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('account.html', views.Account),
    path('home/account.html', views.Account),
    path('journal/account.html', views.Account),
    path('blogweb/account.html', views.Account),
    path('login.html', views.log),
    path('home/login.html', views.log),
    path('jounal/login.html', views.log),
    path('blogweb/login.html', views.log),
    path('signup.html', views.Sign),
    path('home/signup.html', views.Sign),
    path('journal/signup.html', views.Sign),
    path('blogweb/signup.html', views.Sign),
    path('home/', views.homePage),
    path('home/home', views.homePage),
    path('journal/home', views.homePage),
    path('journal/newjournal', views.nj),
    path('home/newjournal', views.nj),
    path('blogweb/home', views.homePage),
    path('blogweb/', views.blogweb),
    path('journal/blogweb', views.blogweb),
    path('journal/blogweb', views.blogweb),
    path('home/blogweb', views.blogweb),
    path('blogweb/blogweb', views.blogweb),
    path('journal/', views.journal),
    path('home/journal', views.journal),
    path('journal/journal', views.journal),
    path('journalexisting.html', views.journal),
    path('blogweb/journal', views.journal),
    path('moodtracker/', views.index, name='index'),
    path('moodtracker.html', views.index, name='index'),
    path('home/moodtracker', views.index, name='index'),
    path('journal/moodtracker', views.index, name='index'),
    path('blogweb/moodtracker', views.index, name='index'),
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('add_journal_entry/', views.add_journal_entry, name='add_journal_entry'),
    path('get_journal_entries/', views.get_journal_entries, name='get_journal_entries'),
    path('delete_journal_entry/<int:entry_id>/', views.delete_journal_entry, name='delete_journal_entry'),
]