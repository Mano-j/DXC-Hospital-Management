from django.urls import path, include

from django.contrib.auth import views as auth_views
from .views import doctor_page_view, doctorDetails, index


app_name = 'homepage'
urlpatterns = [
    
    path("accounts/profile/", doctor_page_view, name="doctor_page_view"),



    path("",index, name="index" ),
    path("yourPage/", doctor_page_view, name="doctor_page_view"),
    path('<int:id>/', doctorDetails, name='doctorDetails'),


    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),

    path('staffLogin/', auth_views.LoginView.as_view(template_name="staffLogin.html"), name="staff_login"),
    path('doctorLogin/', auth_views.LoginView.as_view(template_name="doctorLogin.html"), name="doctor_login"),
    
]