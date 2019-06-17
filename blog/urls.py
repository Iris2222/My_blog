from django.urls import path
from  . import views
urlpatterns=[
#path('',views.index, name='index'),

path('', views.main, name='main'),
path('Educational', views.education, name='education'),
path('log', views.login, name='login'),
path('gallery1', views.gallery1, name='gallery'),
path('Artists', views.artist, name='artists'),
path('styleh', views.styleh, name='styles'),
path('nova', views.nova, name='novicecourses'),
path('marker', views.markers, name='markers'),
path('acr', views.acryl, name='acryl'),
path('akva', views.wc, name='watercolors'),
path('graph', views.graphics, name='graphics'),
]
