from django.conf.urls import url
from comments.views import update_output


urlpatterns = [
    url('', update_output, name='submission'),
]
