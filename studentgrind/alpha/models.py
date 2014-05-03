from django.db import models
from datetime import datetime    
import os.path

# Create your models here.
CURRENCY_CHOICES = (
        ('INR', 'INR'),
        ('USD', 'USD'),
    )
class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscription = models.CharField(max_length=100)
    userId = models.IntegerField()
    subscription_dt = models.DateTimeField()
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30) 
    dob = models.DateField()
    #imageref = models.CharField(db_column='imageref',max_length=140)
    type = models.CharField(max_length=20)
    contactPhone = models.CharField(max_length=140)
    emailId = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    createDate = models.DateTimeField()
    facebook = models.CharField(max_length=140)
    linkedIn = models.CharField(max_length=140)
    github = models.CharField(max_length=140)

class CustomUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)


class CustomUser(models.Model):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    def is_authenticated(self):
        return True
	
	
class Student(models.Model):
    userId = models.AutoField(primary_key=True)
    archetype = models.CharField(max_length=45)
    collegeName = models.CharField(max_length=45,blank = True, null=True)
    goalStatement = models.CharField(max_length=45)
    pedigree = models.CharField(max_length=45)
    salary = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    image = models.ImageField(upload_to="static/student-photo/", max_length=140, blank = True, null=True)
    video = models.FileField(upload_to="static/student-video/", max_length=140, blank = True, null=True)
    candidate = models.BooleanField(default = False)

    
class Skill(models.Model):
    skillId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
	#name = models.CharField(max_length = 30)
    description = models.TextField(blank = True)
    verificationId = models.IntegerField(blank = True, null = True)
    skillScore = models.FloatField(blank = True, null = True)

class Verification(models.Model):
	verificationId = models.AutoField(primary_key=True)
	projectId = models.IntegerField(blank = True, null = True)
	performanceId = models.IntegerField(blank = True, null = True)
	skillId = models.IntegerField(blank = True, null = True)
	certificationId = models.IntegerField(blank = True, null = True)
	academicId = models.IntegerField(blank = True, null = True)
	honorId = models.IntegerField(blank = True, null = True)
	languageId = models.IntegerField(blank = True, null = True)
	volunteerId = models.IntegerField(blank = True, null = True)
	verifiedFor = models.IntegerField(blank = True, null = True)
	verifiedBy = models.IntegerField(blank = True, null = True)
	status = models.CharField(max_length=45, blank = True, null = True)
	projectDescription = models.TextField(blank = True, null = True)
	verificationDescription = models.TextField(blank = True, null = True)
	verifiedDate = models.DateTimeField(auto_now_add = True)
	company = models.CharField(max_length=60, blank = True, null = True)
	when = models.DateField(blank = True, null = True)
	workQuality = models.IntegerField(default=0)	
	communication = models.IntegerField(default=0)
	expertise = models.IntegerField(default=0)
	onTime = models.IntegerField(default=0)
	responsiveness = models.IntegerField(default=0)
	withinBudget = models.IntegerField(default=0)
	ownerShip = models.IntegerField(default=0)
	professionalism = models.IntegerField(default=0)
	wouldHireAgain = models.IntegerField(default=0)
	comments = models.TextField(blank = True, null = True)
	authorized = models.BooleanField(blank = True, default = '')
	authorize_notes = models.CharField(max_length = 150, blank = True, null = True)
	authorize_action = models.BooleanField(default = False)
	authorize_action_by = models.IntegerField(blank = True, null = True)


	def get_verifier(self):
		try:
			return User.objects.get(userId = self.verifiedBy)
		except:
			return None
	def get_verifyFor(self):
		try:
			return User.objects.get(userId = self.verifiedFor)
		except:
			return None

	
class Academic(models.Model):
    academicId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    institutionId = models.IntegerField(blank = True, null = True)
    degree = models.CharField(max_length=45, blank = True, null = True)
    graduationScore = models.DecimalField(max_digits=5, decimal_places=2,blank = True, null = True)
    verificationId =  models.IntegerField(blank = True, null = True)
    academicScore = models.DecimalField( max_digits=5, decimal_places=2, blank = True, null = True)
    
class Honor(models.Model):
    honorId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    honor = models.CharField(max_length=45)
    honorType = models.CharField(max_length=45, blank = True, null = True)
    honorLevel = models.CharField(max_length=45, blank = True, null = True)
    verificationId = models.IntegerField(blank = True, null = True)

class Score(models.Model):
    scoreId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    scoreDate = models.DateTimeField(default=datetime.now())
    academicScore = models.FloatField()
    grindScore = models.FloatField()
    performanceScore = models.FloatField()
    
class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    description = models.CharField(max_length=1000, blank = True)
    project_deadline = models.DateField()
    name = models.CharField(max_length=140)
    img = models.ImageField(upload_to = 'project_images',max_length=140, blank = True)
    currency = models.CharField(max_length = 5, choices=CURRENCY_CHOICES)
    project_value = models.IntegerField()
    participate_leaderboard = models.BooleanField(default = False)
    winner = models.CharField(max_length=140, blank=True, null = True)
    status = models.CharField(max_length=10, blank=True, null = True)

class Membership(models.Model):
    membershipId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    description = models.CharField(max_length=140)
           
class Performance(models.Model):
	performanceId = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = "static/student/performance-image/", blank = True, null = True)
	userId = models.IntegerField()
	description = models.TextField(blank = True, null = True)
	verificationId = models.IntegerField(blank = True, null = True)
	start_date = models.DateField(blank = True)
	end_date = models.DateField(blank = True)
	currency = models.CharField(max_length = 5, choices=CURRENCY_CHOICES)
	project_value = models.CharField(max_length = 15,blank = True, null = True)
	role = models.TextField(blank = True, null = True)
	team_detail = models.TextField(blank = True, null = True)
	doc = models.FileField(upload_to="static/student/performance-doc/", blank = True, null = True)
	video = models.FileField(upload_to="static/student/performance-video/", blank = True, null = True)
	performanceScore = models.FloatField(blank = True, null = True)

class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    createDate = models.DateTimeField(default=datetime.now())
    cvv = models.IntegerField()
    #imageref = models.CharField(db_column='imageref',max_length=140)
    expiration =  models.CharField(max_length=10)
    paymentNumber = models.CharField(max_length=25)
    paymentType = models.CharField(max_length=25)
    sequence = models.IntegerField()
    userId = models.IntegerField()
      
class Institution(models.Model):
    userId = models.AutoField(primary_key=True)
    bankAccountNumber =  models.CharField(max_length=45)
    bankName = models.CharField(max_length=45)
    bankRoutingNumber= models.CharField(max_length=45)
    contact =  models.CharField(max_length=45)
    contactEmailAddress = models.CharField(max_length=45)
    contactPhone= models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    website= models.CharField(max_length=45)

class Enterprise(models.Model):
    userId = models.AutoField(primary_key=True)
    contact =  models.CharField(max_length=45)
    contactEmailAddress = models.CharField(max_length=45)
    contactPhone= models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    website= models.CharField(max_length=45)
    image = models.ImageField(upload_to='enterprise-image', blank = True, null = True)

class Address(models.Model):
    addressId = models.AutoField(primary_key=True)
    addressType = models.IntegerField()
    street1 = models.CharField(max_length=140)
    street2 = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    zipcode = models.CharField(max_length=10)
    
class UserAddress(models.Model):
    userAddressId = models.AutoField(primary_key=True)
    addressId = models.IntegerField()
    userId = models.IntegerField()

class Contribution(models.Model):
    contributionId = models.AutoField(primary_key=True)
    institutionId = models.IntegerField()
    memo = models.CharField(max_length=140)
    paymentId = models.IntegerField()
    userId = models.IntegerField()
    amount = models.FloatField()

class Campaign(models.Model):
    campaignId = models.AutoField(primary_key=True)
    campaignMaterial = models.CharField(db_column='imageref',max_length=140)
    name = models.CharField(max_length=140)
    userId = models.IntegerField()

class Alumni(models.Model):
    userId = models.AutoField(primary_key=True)
    mentorship = models.CharField(max_length=140)

class Accomplishment(models.Model):
    accomplishmentId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=140)
    userId = models.IntegerField()

class PairingAnalytics(models.Model):
    pairingAnalyticsId = models.AutoField(primary_key=True)
    pairingsId = models.IntegerField()
    likeCtr = models.IntegerField()
    commentCtr = models.IntegerField()           
       
class OrderView(models.Model):
    orderId = models.IntegerField(db_column='orderId')    
    itemId = models.IntegerField(db_column='itemId')    
    name = models.CharField(db_column='name',max_length=140)
    price = models.FloatField(db_column='price')
    imageref = models.CharField(db_column='imageref',max_length=140)
    
    class Meta:
        db_table = 'alpha_order_view'
        managed = False
    
#### New table created for storing Student Project Submission
class Submission(models.Model):
	submissionId = models.AutoField(primary_key = True)
	projectId = models.IntegerField()
	userId = models.IntegerField()
	solutionDetails = models.TextField(blank = True, null = True)
	projectUrl = models.CharField(max_length = 200,blank = True, null = True)
	
	
class Documents(models.Model):
	submissionId = models.IntegerField(blank = True, null = True)
	file = models.FileField(upload_to="static/student/project-files/", blank = True, null = True)
	def filename(self):
		return os.path.basename(self.file.name)
	def file_link(self):
		if self.file:
			return "<a href='%s'>download</a>" % (self.file.url,)
		else:
			return "No attachment"

	file_link.allow_tags = True
	
class ProjectDocuments(models.Model):
	submissionId = models.IntegerField(blank = True, null = True)
	file = models.FileField(upload_to="static/student/New-project-files/", blank = True, null = True)
	def filename(self):
		return os.path.basename(self.file.name)
	def file_link(self):
		if self.file:
			return "<a href='%s'>download</a>" % (self.file.url,)
		else:
			return "No attachment"

	file_link.allow_tags = True
	

class Assessment(models.Model):
	userId = models.IntegerField()
	performanceId = models.IntegerField(blank = True, null = True)
	projectId = models.IntegerField(blank = True, null = True)
	challenge1Type = models.CharField(max_length = 100, blank = True, null = True)
	challenge1Desc = models.TextField(blank = True, null = True)
	challenge2Type = models.CharField(max_length = 100, blank = True, null = True)
	challenge2Desc = models.TextField(blank = True, null = True)
	challenge1Date = models.DateField(blank = True, null = True)
	challenge2Date = models.DateField(blank = True, null = True)
	perfScore = models.CharField(max_length = 20, blank = True, null = True)
	growthDesc = models.TextField(blank = True, null = True)
	demoDesc = models.TextField(blank = True, null = True)
	promoted = models.BooleanField(default = False)
	majorGoalDesc = models.TextField(blank = True, null = True)
	mgrRehireDesc = models.TextField(blank = True, null = True)
	subordHireDesc = models.TextField(blank = True, null = True)
	gotoPersonDesc = models.TextField(blank = True, null = True)
	mentoredDesc = models.TextField(blank = True, null = True)

class Volunteer(models.Model):
	volunteerId = models.AutoField(primary_key = True)
	userId = models.IntegerField()
	name = models.CharField(max_length = 100, blank = True, null = True)
	
class Language(models.Model):
	languageId = models.AutoField(primary_key = True)
	userId = models.IntegerField()
	name = models.CharField(max_length = 100, blank = True, null = True)
	
class Test(models.Model):
	testId = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	dueDate = models.DateField(blank = True, null = True)
	createdDate = models.DateField(auto_now_add = True)
	status = models.CharField(max_length = 30, blank = True, null = True)
	assessmentFor = models.IntegerField(blank = True, null = True)
	category = models.CharField(max_length = 100, blank = True, null = True)
	assessmentBy = models.IntegerField(blank = True, null = True)
	assessTime = models.CharField(max_length = 30, blank = True, null = True)
	
	
class Question(models.Model):
	questionId = models.AutoField(primary_key = True)
	assessmentId = models.IntegerField(blank = True, null = True)
	detail = models.CharField(max_length = 1000, blank = True, null = True)
	weightage = models.DecimalField(max_digits=2, decimal_places=1,blank = True, null = True)
	points = models.IntegerField(blank = True, null = True)
	answerId = models.IntegerField(blank = True, null = True)
	type = models.CharField(max_length = 60, blank = True, null = True)
	category = models.CharField(max_length = 100, blank = True, null = True)
	
class Answer(models.Model):
	answerId = models.AutoField(primary_key = True)
	detail = models.CharField(max_length = 500, blank = True, null = True)
	questionId = models.IntegerField(blank = True, null = True)
	
	
class UserAssessment(models.Model):
	user_assessmentId = models.AutoField(primary_key = True)
	assessmentId = models.IntegerField(blank = True, null = True)
	assessmentBy = models.IntegerField(blank = True, null = True)
	points_collected = models.DecimalField(max_digits=4, decimal_places=1,blank = True, null = True)
	status = models.CharField(max_length = 20, blank = True, null = True)
	
class AssignedAssessment(models.Model):
	assigned_assessmentId = models.AutoField(primary_key = True)
	assessmentId = models.IntegerField(blank = True, null = True)
	assessmentFor = models.IntegerField(blank = True, null = True)

class Candidate_Assigned_Assessment(models.Model):
	assigned_assessmentId = models.AutoField(primary_key = True)
	assessmentId = models.IntegerField(blank = True, null = True)
	assessmentFor = models.IntegerField(blank = True, null = True)

	
class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    
    def __unicode__(self):
        return self.image.name	
		
class SignUp(models.Model):
	emailId = models.CharField(max_length=60)
	signUpCode = models.CharField(max_length=10, blank=True, null=True)
	authorized = models.BooleanField(default = False)
	authorizedBy = models.IntegerField(blank = True, null = True)
	authorizedOn = models.DateField(blank = True, null = True)
	authorize_action = models.BooleanField(default = False)
	mail_sent = models.BooleanField(default = False)
	mail_sentOn = models.DateField(blank = True, null = True)
	requestedOn = models.DateTimeField(auto_now_add = True)
	authorize_notes = models.CharField(max_length = 150, blank = True, null = True)
	def __unicode__(self):
		return self.emailId
		
class StrengthsCode(models.Model):
	strengthCode = models.CharField(max_length=60,blank = True, null = True)
	assignedTo = models.IntegerField(blank = True, null = True)
	assignedOn = models.DateField(blank = True, null = True)
	authorize_action = models.BooleanField(default = False)
	mail_sent = models.BooleanField(default = False)
	mail_sentOn = models.DateField(blank = True, null = True)
	requestedOn = models.DateTimeField(blank = True, null = True)
	
class Strengths(models.Model):
	emailId = models.CharField(max_length=60, blank = True, null = True)
	strengths = models.CharField(max_length=60,blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class StrengthsReport(models.Model):
	emailId = models.CharField(max_length=60, blank = True, null = True)
	strengthsReport = models.FileField(upload_to="strength_report/",blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class Requisition(models.Model):
	createdBy = models.IntegerField(blank = True, null = True)
	division = models.CharField(max_length=60,blank = True, null = True)
	CostCenter = models.CharField(max_length = 100,blank = True, null = True)
	category = models.CharField(max_length = 50,blank = True, null = True)
	salary_range = models.CharField(max_length = 100,blank = True, null = True)
	location = models.CharField(max_length = 100,blank = True, null = True)
	dueBy = models.DateTimeField(null= True, blank =True)
	duration = models.CharField(max_length = 30,blank = True, null = True)
	status = models.CharField(max_length = 20,blank = True, null = True)
	why_this_position = models.CharField(max_length = 1000,blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class RequisitionSkill(models.Model):
	detail = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)

class RequisitionExperience(models.Model):
	detail = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)

class RequisitionTask(models.Model):
	detail = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)

class RequisitionTeamNeed(models.Model):
	detail = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class Requisition_firstYearGoal(models.Model):
	goalCriteria = models.CharField(max_length = 150, blank  = True, null = True)
	percentDecision = models.CharField(max_length = 10, blank = True, null = True)
	importance = models.CharField(max_length  = 10, blank = True, null = True)
	when = models.CharField(max_length  = 30, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class Requisition_growthOpportunity(models.Model):
	detail = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class Requisition_Candidates(models.Model):
	candidateId = models.IntegerField(blank = True, null = True)
	match_percent = models.CharField(max_length=60, blank = True, null = True)
	available = models.CharField(max_length=60, blank = True, null = True)
	reason = models.CharField(max_length=60, blank = True, null = True)
	level = models.CharField(max_length=60, blank = True, null = True)
	requisitionId = models.IntegerField(blank = True, null = True)
	createdOn = models.DateTimeField(auto_now_add = True)

class Challenge_Feedback(models.Model):

	submissionId = models.IntegerField(blank = True, null = True)
	feedbackBy = models.IntegerField(blank = True, null = True)
	feedbackDate = models.DateField(auto_now_add = True)
	workQuality = models.IntegerField(blank = True, null = True)
	creativity = models.IntegerField(blank = True, null = True)
	innovation = models.IntegerField(blank = True, null = True)
	teamWork = models.IntegerField(blank = True, null = True)
	addressedProblem = models.IntegerField(blank = True, null = True)
	domainExpertise = models.IntegerField(blank = True, null = True)
	technicalExpertise = models.IntegerField(blank = True, null = True)
	solutionPresentation = models.IntegerField(blank = True, null = True)
	ownership = models.IntegerField(blank = True, null = True)
	winner = models.BooleanField(default = False)
	feedbackDetails = models.CharField(max_length = 1000, blank = True)
	
class Enterprise_Verification(models.Model):
	studentId = models.IntegerField(blank = False)
	projectDescription = models.CharField(max_length = 1000, blank = True, null= True)
	projectName = models.CharField(max_length = 250, blank = True, null = True)
	requestMsg = models.CharField(max_length = 250, blank = True, null = True)
	createdBy = models.IntegerField(blank = False)
	createdOn = models.DateTimeField(auto_now_add = True)
	status = models.CharField(max_length = 15)

class Candidate_Goal(models.Model):
	goalId = models.AutoField(primary_key = True)
	studentId = models.IntegerField()
	goalCriteria = models.CharField(max_length = 150, blank  = True, null = True)
	description = models.TextField(blank = True, null  = True)
	percentMet = models.CharField(max_length = 10, blank = True, null = True)
	importance = models.CharField(max_length  = 10, blank = True, null = True)
	when = models.CharField(max_length  = 30, blank = True, null = True)
	
class BuzzCategory(models.Model):
	categoryId = models.AutoField(primary_key = True)
	categoryName = models.CharField(max_length = 150)
	createdOn = models.DateTimeField(auto_now_add = True)
	
class Buzz(models.Model):
	buzzId = models.AutoField(primary_key = True)
	headline = models.CharField(max_length = 200, blank = True, null = True)
	categoryId = models.IntegerField(blank = True, null = True)
	publishedBy = models.IntegerField(blank = True, null = True)
	publishedOn = models.DateTimeField(auto_now_add = True)
	
class BuzzAssign(models.Model):
	buzzAssignId = models.AutoField(primary_key = True)
	buzzId = models.IntegerField()
	candidateId = models.IntegerField()
	assignedOn = models.DateTimeField()
	assignedBy = models.IntegerField()
	dueBy = models.DateTimeField()
	status = models.CharField(max_length = 20, blank = True, null = True)
	response = models.TextField(blank = True, null = True)
	respondedOn = models.DateTimeField(blank = True, null = True)
	