from django.urls import path
from v3API.views import ConnectCTCTView, SignUpView,SuccessView 

urlpatterns = [
    path('', ConnectCTCTView.as_view(), name="connect"),
    path('jmml', SignUpView.as_view(), name="jmml"),
    path('success', SuccessView.as_view(), name="success"),
]
