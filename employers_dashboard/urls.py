from django.urls import path
from . import views  



app_name = 'employers_dashboard'

urlpatterns = [
   path('',views.Home,name='home'),
   path('create_job/',views.Create_Job,name='create_job'),
   path('edit_job/<id>/',views.Edit_Job,name='edit_job'),
   path('<id>/delete/',views.Job_Delete,name='job_delete'),
   path('employer_detail/<id>/',views.Employer_Detail,name='employers_detail'),
   # path('applicant_detail/<id>/',views.Applicant_Detail,name='applicant_detail')

]
