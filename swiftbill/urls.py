from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout",),
   path('user', views.user, name="user"),
   path('airtime', views.airtime, name="airtime"),
   path('airtimeselect', views.airtimeselect, name="airtimeselect"),
   path('internet', views.internet, name="internet"),
   path('tv', views.tv, name="tv"),
   path('elec', views.elec, name="elec"),
   path('betting', views.betting, name="betting"),
   path('topup', views.topup, name="topup"),
   path('callback', views.callback, name="callback"),
   
]
