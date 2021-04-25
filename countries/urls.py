from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^api/countries$', views.countries_list),
    url(r'api/countries/(?P<pk>[0-9]+)$', views.countries_detail)
    # url('api/countries', views.countries_list),
    # url('api/countries/<pk>', views.countries_detail)
]
