from django.urls import path
from v3API.views import connect_to_ctct,ConnectCTCT, SignUpView,SuccessView 

urlpatterns = [
    path('jmml', SignUpView.as_view(), name="signup"),
    path('jmml<code>', SignUpView.as_view(), name="withcode"),
    path('', ConnectCTCT.as_view(), name="connect"),
    path('success', SuccessView.as_view(), name="success")

]
