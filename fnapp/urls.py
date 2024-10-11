from django.urls import path

from fnapp import views

urlpatterns = [

    #path("", views.login, name="login"),
    path("", views.check, name="check"),
    path("checkfn", views.checkfn, name="checkfn"),
    path("logincode",views.logincode,name="logincode"),
    path("register",views.logincode,name="register"),

   # path("google_check", views.google_check, name="google_check"),
    #path("google_checkfn", views.google_checkfn, name="google_checkfn"),

]
