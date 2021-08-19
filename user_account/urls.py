from django.urls import path
from . import views  
from .views import MyPasswordChangeView, MyPasswordResetDoneView



app_name = 'user_account'

urlpatterns = [
  
  path('',views.UserRegistration,name='registration'),
  path('user_login/',views.UserLogin,name='user_login'),
  path('profile/',views.UserProfile,name='profile'),
  path('change-password/',MyPasswordChangeView.as_view(),name='password-change-view'),
  path('password-reset-done/',MyPasswordChangeView.as_view(),name='password-change-done-view'),
  path('logout/',views.UserLogout,name='logout'),
  
]


handler404 = 'job_posting.views.error_404_view'