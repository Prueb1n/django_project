from django.urls import path
from post.views import hola_mundo,HolaMundoView

urlpatterns=[

    path("",hola_mundo),
    path("cualquier",HolaMundoView.as_view())
]