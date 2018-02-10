from django.conf.urls import url


from .views import index


app_name = 'polls'

urlpatterns = [
    url(r'^home$', index, name='index')
]