from django.urls import path

from fnapp import views

urlpatterns = {
    path("", views.login, name="login"),
    path("register", views.register, name="register"),
    path("check", views.check, name="check"),
    path("Adminhome", views.Adminhome, name="Adminhome"),
    path("Chat", views.Chat, name="Chat"),
    path("news", views.news, name="news"),
    path("user", views.user, name="user"),
    path("userhome", views.userhome, name="userhome"),
    path("logincode",views.logincode,name="logincode"),

}
