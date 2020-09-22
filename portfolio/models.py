from django.db import models
from account.models import User

# # Create your models here. 

# # CUSTOM USER WIL IK AANPASSEN
class Profile(models.Model):
	
	profile_id = models.AutoField(primary_key=True)
	profile_title = models.CharField(max_length = 50)
	first_name = models.CharField(max_length= 100)
	last_name = models.CharField(max_length= 100)
	birth_date = models.DateField()
	phone = models.CharField(max_length=20)
	profile_email = models.EmailField()
	driver_license = models.BooleanField()
	about_me = models.TextField()

	def __str__(self):
		return self.first_name + " " + self.last_name
		
class Interest(models.Model):
	interest = models.TextField(primary_key=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.interest

class Adres(models.Model):

	profile = models.OneToOneField(
		Profile,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	city = models.CharField(max_length=100)
	street = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=20)
	house_number = models.CharField(max_length=10)

	def __str__(self):
		return self.street + " " + self.house_number

class Work_experience(models.Model):
	job_id = models.AutoField(primary_key=True)
	job_title = models.CharField(max_length=50)
	job_description = models.TextField()
	job_start_date = models.CharField(max_length=100)
	job_end_date = models.CharField(null=True, max_length=100)
	job_employer = models.CharField(max_length=100)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.job_title + " at " + self.job_employer

class Education(models.Model): 
	edu_id = models.AutoField(primary_key=True)
	edu_name = models.CharField(max_length=100)
	edu_institution = models.CharField(max_length=100)
	edu_start_date = models.CharField(max_length=100)
	edu_end_date = models.CharField(max_length = 100, null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.edu_name + " at " + self.edu_institution

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_title = models.CharField(max_length= 50)
	live_link = models.URLField(null=True, blank=True)
	github_link = models.URLField(null=True, blank=True)
	date_start = models.CharField(max_length=100)
	date_end = models.CharField(max_length = 100, null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.project_title



class Description(models.Model):
	project = models.OneToOneField(
		Project,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	short = models.TextField()
	stakeholders = models.TextField()
	problem = models.TextField()
	solution= models.TextField()


class Image(models.Model):
	image = models.ImageField(upload_to = 'pics')
	thumbnail = models.BooleanField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)


class Tag(models.Model):
	technology = models.CharField(max_length=100)
	project = models.ManyToManyField(Project)

	def __str__(self):
		return self.technology

class Contact(models.Model):
	contact_id = models.AutoField(primary_key=True)
	contact_email= models.EmailField()
	contact_subject = models.CharField(max_length=100)
	contact_name = models.CharField(max_length=100)
	contact_description = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.contact_email

class Social(models.Model):
	social_name = models.CharField(max_length=100, primary_key=True)
	social_link  = models.URLField(null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	def __str__(self):
		return self.social_name