from django.urls import path
from . import views  



app_name = 'job_posting'

urlpatterns = [
    path('',views.Jobs,name='jobs'),
    path('job_detail/<int:id>/', views.Job_Detail,name='job_detail'),
    path('cat/<slug:category_slug>/',views.job_category,name='job_category'),
    path('industry/<slug:industry_slug>/',views.job_industry,name='job_industry'),
    path('location/<slug:location_slug>/',views.job_location,name='job_location'),
    # path('create_job/',views.Create_Job,name='create_job'),
    path('search',views.Search,name='search')

]
