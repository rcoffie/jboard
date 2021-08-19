from django.shortcuts import render,redirect,get_object_or_404
from job_posting .models import *
from job_posting .forms import *

# Create your views here.






def Home(request):
	jobs = Job_Posting.objects.all().filter(employer= request.user)
	context = {'jobs':jobs}
	return render(request,'employers_dashboard/index.html',context)





def Create_Job(request):
	if request.method == 'POST':
		form = JobPostingForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			user = request.user
			if user.is_authenticated:
				form.employer = request.user
				form.save()
				return redirect('employers_dashboard:home')
	else:
		form = JobPostingForm()

	context = {'form':form}

	return render(request,'employers_dashboard/create_job.html',context)




def Edit_Job(request, id):

	job = get_object_or_404(Job_Posting, id=id)
	form = JobPostingForm(request.POST or None, instance=job)
	if request.user == job.employer:
		if form.is_valid():
			form.save()
			return redirect('employers_dashboard:home')
		else:
			pass
	else:
		return redirect('employers_dashboard:home')

	context = {'form':form}
	return render(request,'employers_dashboard/edit_job.html',context)




def Job_Delete(request, id):

	job = get_object_or_404(Job_Posting, id=id)
	if request.method == 'POST':
		job.delete()
		return redirect('employers_dashboard:home')






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



# def Employer_Detail(request, id):
	
# 	job = get_object_or_404(Job_Posting, id=id)
# 	applicants = Applicant.objects.filter(job=job).order_by('-id')
# 	context = {'job':job,'applicants':applicants}


# 	return render(request, 'employers_dashboard/employers_detail.html',context)





def Employer_Detail(request, id):

	job = get_object_or_404(Job_Posting, id=id)
	applicants = Applicant.objects.filter(job=job).order_by('-id')
	if request.user == job.employer:
		context = {'job':job,'applicants':applicants}
	else:
		return redirect('job_posting:jobs')



	return render(request, 'employers_dashboard/employers_detail.html',context)





# def Applicant_Detail(request, id):
# 	applicant = get_object_or_404(Applicant, id=id)
# 	context = {'applicant':applicant}


# 	return render(request,'employers_dashboard/applicant_detail.html',context)


