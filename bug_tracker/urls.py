"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('ticket/<int:ticket_id>/edit/', views.edit_ticket_view),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view),
    path('unassignticket/<int:ticket_id>/', views.unassign_view),
    path('done/<int:ticket_id>/', views.done_view),
    path('reopenticket/<int:ticket_id>/', views.reopen_view),
    path('invalidticket/<int:ticket_id>/', views.invalid_view),
    path('assignticket/<int:ticket_id>/', views.assign_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('addticket/', views.add_ticket),
    path('admin/', admin.site.urls),
]
