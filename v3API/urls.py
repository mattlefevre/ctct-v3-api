from django.urls import path
from v3API.views import ConnectCTCT, SignUpView,SuccessView 

urlpatterns = [
    path('', ConnectCTCT.as_view(), name="connect"),
    path('jmml', SignUpView.as_view(), name="signup"),
    path('success', SuccessView.as_view(), name="success"),
]
