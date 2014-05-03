from django.forms import ModelForm
from models import*
from multiuploader.forms import MultiuploaderField

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude=('userId','project_deadline','status')

class AssessForm(ModelForm):
	class Meta:
		model = Assessment
		exclude = ('userId','performanceId','challenge1Date','challenge2Date','projectId')
		
class PerformanceForm(ModelForm):
	class Meta:
		model = Performance
		exclude = ('userId','performanceId','verificationId','doc','video','performanceScore','start_date','end_date')

class VerifyForm(ModelForm):
	class Meta:
		model = Verification
		exclude = ('verifiedFor','verifiedBy','status','when','projectId','performanceId','skillId','workQuality','communication','expertise','onTime','responsiveness','withinBudget','ownerShip','professionalism','wouldHireAgain')
		
class AcademicForm(ModelForm):
	class Meta:
		model = Academic
		exclude = ('userId','institutionId','verificationId','academicScore')

class MembershipForm(ModelForm):
	class Meta:
		model = Membership
		exclude = ('userId')
		
class SkillForm(ModelForm):
	class Meta:
		model = Skill
		exclude = ('userId','verificationId','skillScore')
		
		
class HonorForm(ModelForm):
	class Meta:
		model = Honor
		exclude = ('userId')
		
		
class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		exclude = ('userId')
		
class LanguageForm(ModelForm):
	class Meta:
		model = Language
		exclude = ('userId')
		
class AssessmentForm(ModelForm):
	class Meta:
		model = Test
		exclude = ('assessmentFor','assessmentBy','status','createdDate','dueDate')