from django.contrib import admin
from .models import *

# Register your models here.


# Register your models here.
# admin.site.register(Industry)
# admin.site.register(Category)
# admin.site.register(Location)
# admin.site.register(Job_Posting)



# @admin.register(Applicant)
# class ApplyJobAdmin(admin.ModelAdmin):
# 	list_display = ['firstName','job']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug':('name',)}





@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug':('name',)}



@admin.register(Industry)
class Industry(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug':('name',)}


@admin.register(Job_Posting)
class JobAdmin(admin.ModelAdmin):
	list_display = ['title','responsibilities','preferred_skills','additional_skills','status']




@admin.register(Applicant)
class ApplyJobAdmin(admin.ModelAdmin):
	list_display = ['firstName','job']