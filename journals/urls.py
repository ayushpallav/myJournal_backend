from django.conf.urls import url
from journals import views


# SET THE NAMESPACE!
app_name = 'journals'


urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
