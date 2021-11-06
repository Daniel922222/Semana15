from typing import ValuesView
from django.urls import path


from DjandomiApp.views import home
from.import views
urlpatterns=[
    path('',views.home),
    path('registrardatos/',views.registrardatos),
    path('eliminardatos/<codigo>',views.eliminardatos),
    path('autor/',views.autor),
]