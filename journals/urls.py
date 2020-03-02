from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from journals import views


# SET THE NAMESPACE!
app_name = 'journals'

Profilerouter = routers.DefaultRouter()
Profilerouter.register(r'profile', views.ProfileView)

urlpatterns=[
	path('', include(Profilerouter.urls)),
    url(r'^register/$',views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    path('entry/', views.JournalEntryView.as_view(), name='entry')
]
