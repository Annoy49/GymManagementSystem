from django.urls import path,include
from django.contrib import admin
# gym_management/urls.py
from gym import views  # If views.py is inside the gym app


urlpatterns = [
    path('members/', views.member_list, name='member_list'),
    path('admin/', admin.site.urls),
    path('gym/', include('gym.urls')),
]
