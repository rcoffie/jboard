from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q

from django.contrib import messages
from datetime import datetime 
from django.db.models.functions import Now

# Create your views here.



def error_404_view(request,exception):

	return render(requst, '404.html')




def categories(request):
	return {
	'categories':Category.objects.all()
	}


def locations(request):
	return {
	'locations':Location.objects.all()
	}


def industries(request):
	return {
	'industries':Industry.objects.all()
	}




def Jobs(request):

	jobs = Job_Posting.objects.order_by('-id').filter(expiration_date__gte=Now())
	context = {'jobs':jobs}

	return render(request,'job_posting/index.html',context)


def  job_industry(request,industry_slug):

	industry  = get_object_or_404(Industry, slug=industry_slug)
	jobs      = Job_Posting.objects.filter(industry=industry)
	context   = {'industry':industry,'jobs':jobs}

	return render(request,'job_posting/job_industry.html',context)

def job_category(request,category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	jobs      = Job_Posting.objects.filter(category=category)

	context = {'category':category,'jobs':jobs}
	return render(request,'job_posting/job_category.html',context)



def job_location(request, location_slug):

	location = get_object_or_404(Location, slug=location_slug)
	jobs     = Job_Posting.objects.filter(location=location)
	context  = {'location':location,'jobs':jobs}


	return render(request,'job_posting/job_location.html',context)




def Job_Detail(request, id):
	form = ApplicantForm()
	job = get_object_or_404(Job_Posting, id=id)
	if request.method == 'POST':
		form = ApplicantForm(request.POST, request.FILES)
		if form.is_valid():
			firstName = request.POST['firstName']
			lastName  = request.POST['lastName']
			email = request.POST['email']
			upload     = request.FILES['upload']
			# if Applicant.objects.filter(email=email).exists():
			if job.applicant_set.filter(email=email):
				messages.warning(request,'you have already applied for this job')
			else:
				applicant = Applicant.objects.create(firstName=firstName,lastName=lastName,email=email,job=job,upload=upload)
				applicant.save()
				
		else:
			applicant = Applicant.objects.create(firstName=firstName,lastName=lastName,email=email,job=job,upload=upload)
			applicant.save()
			return redirect('job_posting:jobs')

			

	context = {'job':job,'form':form}



	return render(request,'job_posting/job_detail.html',context)









# def Create_Job(request):

# 	form = JobPostingForm()


# 	context = {'form':form}


# 	return render(request,'job_posting/create_job.html',context)




def Search(request):
	jobs = Job_Posting.objects.all()
	query = request.GET.get('q')
	# print(query)
	if query:
		jobs = Job_Posting.objects.filter(
            
            Q(title__icontains=query)|
            Q(qualifiction_type__icontains=query)|
            Q(responsibilities__icontains=query)
          

			)

	context = {
	'jobs':jobs,
	}

	return render(request, 'job_posting/search.html',context)
