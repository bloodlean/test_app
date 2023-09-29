from django.urls import path, include
from .views import event, event_detail

urlpatterns = [
    path('event/', event),
    path('event/<int:pk>/', event_detail),

    path('auth/', include('dj_rest_auth.urls'))
]