from django.db import models
from user_account.models import Account 
from django.urls import reverse 

# Create your models here.

#QUALIFICATION
QUALIFICATION_TYPE = [

('Doctoral degree','Doctoral degree'),
('Masters Degree','Masters Degree'),
('Graduate Diploma','Graduate Diploma'),
('Bachelor Degree','Bachelor Degree'),
('Advanced Diploma / Associates Degree','Advanced Diploma / Associates degree'),
('Diploma','Diploma'),
('Professional Certificate','Professional Certificate'),
('Undisclosed','Undisclosed')

]


#EXPERIENCE 
EXPERIENCE_LEVEL = [

('Junior Level','Junior Level'),
('Mid Level','Mid Level'),
('Senior Level','Senior Level'),
('Undisclosed','Undisclosed')



]


#EMPLOYMENT TYPE 
EMPLOYMENT_TYPE = [
('Permanent','Permanent'),
('Contract','Contract'),
('Undisclosed','Undisclosed'),
]




#industry 
class Industry(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True,blank=True,null=True)


	


	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('job_posting:job_industry', args=[self.slug])




# Category model 
class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True,blank=True,null=True)


	class Meta:
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('job_posting:job_category', args=[self.slug])


	def __str__(self):
		return self.name




# Region Model 
class Location(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255,unique=True,blank=True,null=True)

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('job_posting:job_location', args=[self.slug])




#Job Post 
class Job_Posting(models.Model):


	title = models.CharField(max_length=255, db_index=True)
	responsibilities   = models.TextField(blank=True,null=True) 
	preferred_skills   = models.TextField(blank=True,null=True)
	experience         = models.IntegerField(null=True,blank=True)
	additional_skills  = models.TextField(null=True,blank=True)
	employment_type    = models.CharField(choices=EMPLOYMENT_TYPE,max_length=100)
	experience_level   = models.CharField(choices=EXPERIENCE_LEVEL,max_length=100,blank=True,null=True)
	qualifiction_type  = models.CharField(choices=QUALIFICATION_TYPE,max_length=100,blank=True,null=True)
	salary             = models.FloatField(null=True,blank=True)
	qualities          = models.TextField(null=True,blank=True)
	location           = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
	category           = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
	employer           = models.ForeignKey(Account,on_delete=models.CASCADE)
	industry           = models.ForeignKey(Industry,on_delete=models.CASCADE,null=True,blank=True)
	# top_job            = models.BooleanField(default=False)
	status             = models.BooleanField(default=False)
	date_created       = models.DateTimeField(auto_now_add=True)
	updated            = models.DateTimeField(auto_now=True)
	expiration_date    = models.DateField(blank=True,null=True)


	def __str__(self):
		return self.title


class Applicant(models.Model):
	job  = models.ForeignKey(Job_Posting, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=200)
	lastName  = models.CharField(max_length=200)
	email     = models.EmailField(max_length=200)
	upload    = models.FileField(upload_to='uploads/% Y/% m/% d/')
	date_created = models.DateTimeField(auto_now_add=True)



	def __str__(self):
		return self.firstName

    
