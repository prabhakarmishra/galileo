# Create your views here.
import oauth2 as oauth
import cgi
import simplejson as json
import re
from django.conf import settings
from alpha.models import Academic, User, Accomplishment, Address, Alumni, Campaign, Contribution, Enterprise, Institution, Payment, Performance, Membership, Project, Score, Skill, Student, Subscription, UserAddress, Verification, Honor
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from django.contrib.localflavor.generic.forms import DateTimeField
import MySQLdb
import datetime
import logging
import time
import xlrd
from django.db.models import Q
from django.core.urlresolvers import reverse
from alpha.forms import*
logger = logging.getLogger('alpha')
from datetime import date
from django.core.mail import send_mail, EmailMultiAlternatives,EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import logout as auth_logout
from django.contrib.messages.api import get_messages
import string
import random


def home(request):
	try:
		user = request.session['validate_user']
	except:
		pass
	status = request.GET.get('status')
	pass_status = request.GET.get('pass_status')
	return render(request,'index.html', locals())

def about_us(request):
	try:
		user = request.session['validate_user']
	except:
		pass
	return render(request,'about.html', locals())

def instAlumni(request):
	return render(request, 'instAlumni.html')
	
def join_studentgrind(request):
	user_type = request.GET.get('type')
	if user_type == 'Student':
		return render(request,'signup.html', {'userType':'Student'})
	if user_type == 'Alumni':
		return render(request,'alsignup.html', {'userType':'Alumni'})
	if user_type == 'Institution':
		return render(request,'institution.html', {'userType':'Institution'})
	if user_type == 'Enterprise':
		return render(request,'enterprise.html', {'userType':'Enterprise'})
	
def view_page (request, userId):
    try:
        user = User.objects.get(pk=userId)
    except  User.DoesNotExist:
        return render_to_response("create.html",{"userId": userId})
    fname = user.fname
    return render_to_response("view.html",{"userId":userId, "fname":fname})
    
def edit_page (request, userId):
    logger.debug('inside Edit Page')
    try:
        user = User.objects.get(pk=userId)
        fname = user.fname
        userType = user.type
        logger.debug('inside Edit Page - fname')
    except User.DoesNotExist:
        logger.debug('inside Edit Page - User Does not exist')
        return render_to_response("create.html",{"userId": userId})
    return render_to_response("edit.html",{"userId":userId, "fname":fname,"type":userType})
    
def save_page (request, userId):
    fname = request.POST["fname"]
    userType = request.POST["type"]
    create_dt = datetime.datetime.now()
    update_dt = datetime.datetime.now()

    try:
        user = User.objects.get(pk=userId)
        user.name = fname
        user.type = userType
    except User.DoesNotExist:
        user = User(id=userId, fname=fname, type=userType, create_dt=create_dt,update_dt=update_dt)
    user.save()
    return HttpResponseRedirect("/studentgrind/" + userId + "/")
"""
def create_user (request, userId):
    logger.debug('inside create_user')
    if request.method == 'POST':
		json_data = simplejson.loads(request.body)
		logger.debug('Raw Data: "%s"' % json_data)
		password = json_data['password']
		try:
			fName = json_data['fName']
			lName = json_data['lName']
		except:
			fName = ''
			lName = ''
		userType = json_data['type']
		if userType !='Student':
			try:
				dob = json_data['dob']
				contactPhone = json_data['contactPhone']
				gender = json_data['gender']
			except:
				dob = "2013-01-01"
				contactPhone = ""
				gender = ""
		emailId = json_data['emailId']
		logger.debug('password: %s' %  password)
		createDate = datetime.now()
		#imageref = json_data['imageref']
		try:
			facebook = json_data['facebook']
			linkedIn = json_data['linkedIn']
			github = json_data['github']
		except:
			facebook = ''
			linkedIn = ''
			github = ''
    # -- Remove comments above during actual integration = Test code
    #logger.debug('inside POST')
    #password = '1234'
    #fName = 'CIT'
    #lName = 'Edu'
    #dob = '1942-01-01'
    #userType = 'Institution'
    #contactPhone = '310-212-2802'
    #emailId = 'info@cit.edu'
    #gender = 'NA'
    #logger.debug('password: %s' %  password)
    #createDate = datetime.datetime.now()
    #facebook = 'info@cit.edu'
    #linkedIn = 'info@cit.edu'
    #github = 'info@cit.edu'
    
		try:
			user = User.objects.get(pk=userId)
			logger.debug('####### Create User');
		except User.DoesNotExist:
			logger.debug('####### Create User- User NOT FOUND');
			if userType == 'Student':
				user = User(emailId=emailId,fName=fName, lName=lName, password=password, type=userType,createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
			if userType == 'Enterprise':
				user = User(emailId=emailId, dob=dob, fName=fName, lName=lName, password=password, type=userType, contactPhone=contactPhone, gender=gender, createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
			if userType == 'Alumni':
				user = User(emailId=emailId, dob=dob, fName=fName, lName=lName, password=password, type=userType, contactPhone=contactPhone, gender=gender, createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
			if userType == 'Institution':
				user = User(emailId=emailId, dob=dob, fName=fName, lName=lName, password=password, type=userType, contactPhone=contactPhone, gender=gender, createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)

		user.save()
		registered_user = user
		request.session['registered_user'] = registered_user
		# Create entry in Student, Alumni, Enterprise or Institution table based "user type"
		if userType == 'Student':
			collegeName = json_data['collegeName']
			try:
				photo = json_data['photo']
			except:
				photo = ''
			try:
				video = json_data['video']
			except:
				video = ''
			#collegeName = 'MIT'
			try:
				student = Student.objects.get(pk=userId)
				logger.debug('####### Student exists');
			except Student.DoesNotExist:
				student = Student(userId=user.userId, collegeName=collegeName, photo = photo, video = video)
				logger.debug('####### Student not exists; created');
			student.save()    
		elif userType == 'Alumni':
			mentorship = json_data['mentorship']
			#mentorship = 'group'
			try:
				alumni = Alumni.objects.get(pk=userId)
				logger.debug('####### Alumni exists');
			except Alumni.DoesNotExist:
				alumni = Alumni(userId=user.userId, mentorship=mentorship)
			alumni.save()
		elif userType == 'Enterprise':
			name = json_data['collegeName']
			try:
				website = json_data['website']
			except:
				website = ''
			contact = str(json_data['fName'])+str(json_data['lName'])
			try:
				contactPhone = json_data['contactPhone']
			except:
				contactPhone = ''
			contactEmailAddress = json_data['emailId']     
			#image = request.FILES['image']
			try:
				image = json_data['image']
			except:
				image = ''
			#name = 'Google'
			#website = 'www.google.com'
			#contact = 'Ping Yiu'
			#contactPhone = '650-200-2000'
			#contactEmailAddress = 'pyiu@google.com'
			try:
				enterprise = Enterprise.objects.get(pk=userId)
				logger.debug('####### Alumni exists');
			except Enterprise.DoesNotExist:
				enterprise = Enterprise(userId=user.userId, name=name, website=website, contact=contact, contactPhone=contactPhone, contactEmailAddress=contactEmailAddress, image = image)
			enterprise.save()
		elif userType == 'Institution':
			name = json_data['name']
			website = json_data['website']
			contact = json_data['contact']
			contactPhone = json_data['contactPhone']
			contactEmailAddress = json_data['contactEmailAddress']
			bankName = json_data['bankName']
			bankRoutingNumber = json_data['bankRoutingNumber']
			bankAccountNumber = json_data['bankAccountNumber']
			#name = 'Google'
			#website = 'www.google.com'
			#contact = 'Ping Yiu'
			#contactPhone = '650-200-2000'
			#contactEmailAddress = 'pyiu@google.com'
			#bankName = 'Bank of America'
			#bankRoutingNumber = '121000358'
			#bankAccountNumber = '1234567890'
			try:
				institution = Institution.objects.get(pk=userId)
				logger.debug('####### Alumni exists');
			except Institution.DoesNotExist:
				institution = Institution(userId=user.userId, name=name, website=website, contact=contact, contactPhone=contactPhone, contactEmailAddress=contactEmailAddress, bankName=bankName, bankAccountNumber=bankAccountNumber, bankRoutingNumber=bankRoutingNumber)
			institution.save()
			
		logger.debug('userId: %s' %  user.userId)
		logger.debug('user emailId: %s' %  user.emailId)
    return HttpResponseRedirect("/users/" + emailId)
"""

## New Function for implementing signup via popup and without json data.	

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_user (request, userId):
    logger.debug('inside create_user')
    key=request.GET.get('key')
    if request.method == 'POST':
		#logger.debug('Raw Data: "%s"' % request.POST.get)
		password = request.POST.get('password')
		try:
			fName = request.POST.get('fName')
			lName = request.POST.get('lName')
		except:
			fName = ''
			lName = ''
		userType = request.POST.get('type')
		if userType !='Student':
			try:
				dob = request.POST.get('dob')
				contactPhone = request.POST.get('contactPhone')
				gender = request.POST.get('gender')
			except:
				dob = "2013-01-01"
				contactPhone = ""
				gender = ""
		emailId = request.POST.get('emailId')
		logger.debug('password: %s' %  password)
		createDate = datetime.now()
		#imageref = request.POST.get('imageref')
		try:
			facebook = request.POST.get('facebook')
			linkedIn = request.POST.get('linkedIn')
			github = request.POST.get('github')
		except:
			facebook = ''
			linkedIn = ''
			github = ''
    
		try:
			user = User.objects.get(pk=userId)
			logger.debug('####### Create User');
		except User.DoesNotExist:
			logger.debug('####### Create User- User NOT FOUND');
			if userType == 'Student':
				user = User(emailId=emailId,fName=fName, lName=lName, password=password, type=userType,createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
			if userType == 'Enterprise':
				user = User(emailId=emailId, dob=dob, fName=fName, lName=lName, password=password, type=userType, contactPhone=contactPhone, gender=gender, createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
			if userType == 'Candidate':
				user = User(emailId=emailId, dob=dob, fName=fName, lName=lName, password=password, type=userType, contactPhone=contactPhone, gender=gender, createDate=createDate, facebook=facebook, linkedIn=linkedIn, github=github)
		user.save()
		registered_user = user
		request.session['registered_user'] = registered_user
		# Create entry in Student, Alumni, Enterprise or Institution table based "user type"
		if userType == 'Student':
			collegeName = request.POST.get('collegeName')
			try:
				photo = request.POST.get('image')
			except:
				photo = ''
			try:
				video = request.POST.get('video')
			except:
				video = ''
			#collegeName = 'MIT'
			try:
				student = Student.objects.get(pk=userId)
				logger.debug('####### Student exists');
			except Student.DoesNotExist:
				student = Student(userId=user.userId, collegeName=collegeName, image = photo, video = video, candidate = False)
				logger.debug('####### Student not exists; created');
			student.save()
		elif userType == 'Candidate':
			collegeName = request.POST.get('collegeName')
			try:
				photo = request.POST.get('image')
			except:
				photo = ''
			try:
				video = request.POST.get('video')
			except:
				video = ''
			#collegeName = 'MIT'
			try:
				candidate = Student.objects.get(pk=userId)
				logger.debug('####### Candidate exists');
			except Student.DoesNotExist:
				candidate = Student(userId=user.userId, collegeName=collegeName, image = photo, video = video, candidate = True)
				logger.debug('####### Candidate not exists; created');
			candidate.save()
		elif userType == 'Enterprise':
			name = request.POST.get('collegeName')
			try:
				website = request.POST.get('website')
			except:
				website = ''
			contact = str(request.POST.get('fName'))+str(request.POST.get('lName'))
			try:
				contactPhone = request.POST.get('contactPhone')
			except:
				contactPhone = ''
			contactEmailAddress = request.POST.get('emailId')     
			#image = request.FILES('image')
			try:
				image = request.POST.get('image')
			except:
				image = ''
			try:
				enterprise = Enterprise.objects.get(pk=userId)
				logger.debug('####### Alumni exists');
			except Enterprise.DoesNotExist:
				enterprise = Enterprise(userId=user.userId, name=name, website=website, contact=contact, contactPhone=contactPhone, contactEmailAddress=contactEmailAddress, image = image)
			enterprise.save()
					
		logger.debug('userId: %s' %  user.userId)
		logger.debug('user emailId: %s' %  user.emailId)

		if key == "json":
			success = True
			msg = "Successfull"
			res = {'success':True, 'msg':msg}
			return HttpResponse(json.dumps(res), mimetype = "application/json")
			
    return redirect("/landing_page/")
	
	
	
	
def update_user (request, userId):
    logger.debug('inside update_user')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #emailId = json_data['emailId']
    #password = json_data['password']
    #createDate = datetime.datetime.now()
    #contactPhone = json_data['contactPhone']
    #fName = json_data['fName']
    #lName = json_data['lName']
    #userType = json_data['type']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    lName = 'Vijay'
    userType = 'Student'
    createDate = datetime.datetime.now()

    try:
        user = User.objects.get(pk=userId)
        logger.debug('####### Update User');
    except User.DoesNotExist:
        logger.debug('####### Update User - USER NOT FOUND userId: %s' %  userId);
        #user = User(emailId=emailId, fName=fName, lName=lName, password=password, contactPhone=contactPhone, createDate=createDate)
        user = User(lName=lName, createDate=createDate)
    #user.fName = fName
    user.lName = lName
    user.save()
    
    # Create entry in Student, Alumni, Enterprise or Institution table based "user type"
    if userType == 'Student':
        #collegeName = json_data['collegeName']
        collegeName = 'MIT'
        try:
            student = Student.objects.get(pk=userId)
            student.collegeName = collegeName
            logger.debug('####### Student exists');
        except Student.DoesNotExist:
            student = Student(userId=user.userId, collegeName=collegeName)
            logger.debug('####### Student not exists; created');
        student.save()    
    elif userType == 'Alumni':
        #mentorship = json_data['mentorship']
        mentorship = 'no'
        try:
            alumni = Alumni.objects.get(pk=userId)
            alumni.mentorship = mentorship
            logger.debug('####### Alumni exists');
        except Alumni.DoesNotExist:
            alumni = Alumni(userId=user.userId, mentorship=mentorship)
        alumni.save()

    return HttpResponseRedirect("/users/" + userId)

def create_performance (request, performanceId):
    logger.debug('inside create_performance')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    #video = json_data['video']
    #doc = json_data['doc']
    verificationId = '0'
    performanceScore = '0'
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    description = 'Lead mobile strategy through technology and marketing research'
    video = 'Sample Video'
    doc = 'Edu'
    userId = '9'
    verificationId = '0'
    performanceScore = '0'

    try:
        performance = Performance.objects.get(pk=performanceId)
        logger.debug('####### Create performance');
    except Performance.DoesNotExist:
        logger.debug('####### Create performance- User NOT FOUND');
        performance = Performance(performanceId=performanceId, description=description, video=video, doc=doc, userId=userId, verificationId=verificationId, performanceScore=performanceScore)
    performance.save()
    return HttpResponseRedirect("/performances/" + performanceId)

def update_performance (request, performanceId):
    logger.debug('inside update_performance')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    #video = json_data['video']
    #doc = json_data['doc']
    #verificationId = '0'
    #performanceScore = '0'
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    description = 'Lead mobile strategy through technology and marketing research'
    video = 'Strategy Video'
    doc = 'Mobile Design Guide'
    userId = '9'
    verificationId = '0'
    performanceScore = '0'

    try:
        performance = Performance.objects.get(pk=performanceId)
        logger.debug('####### Update performance');
    except Performance.DoesNotExist:
        logger.debug('####### Create performance- User NOT FOUND');
        performance = Performance(performanceId=performanceId, description=description, video=video, doc=doc, userId=userId, verificationId=verificationId, performanceScore=performanceScore)
    #user.fName = fName
    performance.description = description
    performance.video = video
    performance.doc = doc
    performance.save()
    return HttpResponseRedirect("/performances/" + performanceId)

def delete_performance (request, performanceId):
    logger.debug('inside delete_performance')
    logger.debug('------------')

    try:
        performance = Performance.objects.get(pk=performanceId)
        logger.debug('####### Delete performance');
    except Performance.DoesNotExist:
        logger.debug('####### Performance not found');
    
    performance.delete()    
    return HttpResponseRedirect("/performances/" + performanceId)

def create_accomplishment (request, accomplishmentId):
    logger.debug('inside create_accomplishment')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    description = 'Launched Facebook App for Android'
    userId = '9'

    try:
        accomplishment = Accomplishment.objects.get(pk=accomplishmentId)
        logger.debug('####### Create accomplishment');
    except Accomplishment.DoesNotExist:
        logger.debug('####### Create accomplishment- User NOT FOUND');
        accomplishment = Accomplishment(accomplishmentId=accomplishmentId, description=description, userId=userId)
    accomplishment.save()
    return HttpResponseRedirect("/accomplishments/" + accomplishmentId)

def update_accomplishment (request, accomplishmentId):
    logger.debug('inside update_accomplishment')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    description = 'Launched Facebook app for iPads'
    userId = '9'

    try:
        accomplishment = Accomplishment.objects.get(pk=accomplishmentId)
        logger.debug('####### Update accomplishment');
    except Accomplishment.DoesNotExist:
        logger.debug('####### Create accomplishment- User NOT FOUND');
        accomplishment = Accomplishment(accomplishmentId=accomplishmentId, description=description, userId=userId)
    #user.fName = fName
    accomplishment.description = description
    accomplishment.save()
    return HttpResponseRedirect("/accomplishments/" + accomplishmentId)

def delete_accomplishment (request, accomplishmentId):
    logger.debug('inside delete_accomplishment')
    logger.debug('------------')

    try:
        accomplishment = Accomplishment.objects.get(pk=accomplishmentId)
        logger.debug('####### Delete accomplishment');
    except Accomplishment.DoesNotExist:
        logger.debug('####### Accomplishment not found');
    
    accomplishment.delete()    
    return HttpResponseRedirect("/memberships/" + accomplishmentId)

def create_membership (request, membershipId):
    logger.debug('inside create_membership')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    description = 'Joined Y-combinator startup program'
    userId = '9'

    try:
        membership = Membership.objects.get(pk=membershipId)
        logger.debug('####### Create membership');
    except Membership.DoesNotExist:
        logger.debug('####### Create membership- User NOT FOUND');
        membership = Membership(membershipId=membershipId, description=description, userId=userId)
    membership.save()
    return HttpResponseRedirect("/memberships/" + membershipId)

def update_membership (request, membershipId):
    logger.debug('inside update_membership')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    description = 'Joined Google Venture incubator program'
    userId = '9'

    try:
        membership = Membership.objects.get(pk=membershipId)
        logger.debug('####### Update membership');
    except Membership.DoesNotExist:
        logger.debug('####### Update membership- User NOT FOUND');
        membership = Membership(membershipId=membershipId, description=description, userId=userId)
    #user.fName = fName
    membership.description = description
    membership.save()
    return HttpResponseRedirect("/memberships/" + membershipId)

def delete_membership (request, membershipId):
    logger.debug('inside delete_membership')
    logger.debug('------------')

    try:
        membership = Membership.objects.get(pk=membershipId)
        logger.debug('####### Delete membership');
    except Membership.DoesNotExist:
        logger.debug('####### Membership not found');
    
    membership.delete()    
    return HttpResponseRedirect("/memberships/" + membershipId)
        
def create_payment (request, paymentId):
    logger.debug('inside create_payment')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    #createDate = datetime.datetime.now()
    #sequence = json_data['sequence']
    #paymentType = json_data['paymentType']
    #paymentNumber = json_data['paymentNumber']
    #expiration = json_data['expiration']
    #cvv = json_data['cvv']
        
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    createDate = datetime.datetime.now()
    userId = '9'
    sequence = '1'
    paymentType = 'Visa'
    paymentNumber = '4388570012341000'
    expiration = '01/2014'
    cvv = '100'

    try:
        payment = Payment.objects.get(pk=paymentId)
        logger.debug('####### Create payment');
    except Payment.DoesNotExist:
        logger.debug('####### Create payment- User NOT FOUND');
        payment = Payment(createDate=createDate, userId=userId, sequence=sequence, paymentType=paymentType, paymentNumber=paymentNumber, expiration=expiration, cvv=cvv)
    payment.save()
    return HttpResponseRedirect("/payments/" + paymentId)

def update_payment (request, paymentId):
    logger.debug('inside update_payment')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    paymentNumber = '4388010120202000'
    expiration = '03/2015'
    cvv = '010'
    userId = '9'

    try:
        payment = Payment.objects.get(pk=paymentId)
        logger.debug('####### Update payment');
    except Payment.DoesNotExist:
        logger.debug('####### Update payment- User NOT FOUND');
        payment = Payment(paymentId=paymentId, userId=userId)
    #user.fName = fName
    payment.paymentNumber = paymentNumber
    payment.expiration = expiration
    payment.cvv = cvv
    payment.save()
    return HttpResponseRedirect("/payments/" + paymentId)

def request_verification (request, verificationId):
    logger.debug('inside request_verification')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #fName = json_data['fName']
    #lName = json_data['lName']
    #emailId = json_data['emailId']
    #userId = json_data['userId']
    #verifierId = json_data['verifierId']
    #verificationDescription = json_data['verificationDescription']
    #performanceId = json_data['performanceId']
    #verifyType = json_data['verifyType']
    userType = 'Verifier'
    password = 'TempPass1#'
    createDate = datetime.datetime.now()

    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    verifierId = '17'
    fName = 'John'
    lName = 'Doe'
    emailId = 'jdoe@stanford.edu'
    verificationDescription = 'I request you to verify the Individual study i successfully completed with you in 2009 for Python programming skills'
    status = 'Requested'
    userId = '9'
    performanceId = '2'
    verifyType = 'Skill'

    #if verifierId =='':
    try:
        user = User(fName=fName, lName=lName, emailId=emailId, type=userType, password=password, createDate=createDate)
        user.save()
    except:
        logger.debug('####### except');
        user = User.objects.get(pk=verifierId)
        logger.debug('####### Create User');
    
    try:
        verification = Verification.objects.get(pk=verificationId)
        logger.debug('####### Create Verification');
    except Verification.DoesNotExist:
        logger.debug('####### Create Verification- Verification NOT FOUND');
        verification = Verification(verifiedFor=userId, verifiedBy=user.userId, verificationDescription=verificationDescription, status=status, verifiedDate=createDate)
    verification.save()
    
    if verifyType == 'Performance':
        try:
            performance = Performance.objects.get(pk=performanceId)
            logger.debug('####### Got Performance');
        except:
            logger.debug('####### Unable to find Performance');
            
        performance.verificationId = verification.verificationId 
        performance.save()   
    else:
        try:
            skill = Skill.objects.get(pk=performanceId)
            logger.debug('####### Got Skill');
        except:
            logger.debug('####### Unable to find Skill');
            
        skill.verificationId = verification.verificationId 
        skill.save()   
    return HttpResponseRedirect("/verification/" + verificationId)

def create_skill (request, skillId):
    logger.debug('inside create_skill')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    description = 'Python programming'
    userId = '9'
    verificationId = '0'
    skillScore = '0'

    try:
        skill = Skill.objects.get(pk=skillId)
        logger.debug('####### Create membership');
    except Skill.DoesNotExist:
        logger.debug('####### Create skill- User NOT FOUND');
        skill = Skill(skillId=skillId, description=description, userId=userId, verificationId=verificationId, skillScore=skillScore)
    skill.save()
    return HttpResponseRedirect("/skills/" + skillId)

def update_skill (request, skillId):
    logger.debug('inside update_skill')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #description = json_data['description']
    #verificationId = json_data['verificationId']
    #skillScore = json_data['skillScore']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    description = 'Hive Development'
    userId = '9'
    verificationId = '0'
    skillScore = '0'

    try:
        skill = Skill.objects.get(pk=skillId)
        logger.debug('####### Update skill');
    except Skill.DoesNotExist:
        logger.debug('####### Update skill- User NOT FOUND');
        skill = Skill(skillId=skillId, description=description, userId=userId, verificationId=verificationId, skillScore=skillScore)
    #user.fName = fName
    skill.description = description
    skill.save()
    return HttpResponseRedirect("/skills/" + skillId)

def delete_skill (request, skillId):
    logger.debug('inside delete_skill')
    logger.debug('------------')

    try:
        skill = Skill.objects.get(pk=skillId)
        logger.debug('####### Delete skill');
    except Skill.DoesNotExist:
        logger.debug('####### Skill not found');
    
    skill.delete()    
    return HttpResponseRedirect("/skills/" + skillId)

def create_academic (request, academicId):
    logger.debug('inside create_academic')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #institutionId = json_data['institutionId']
    #degree = json_data['degree']
    #graduationScore = json_data['graduationScore']
    #verifiedBy = json_data['verifiedBy']
    #verifiedDate = json_data['verifiedDate']
    #academicScore = json_data['academicScore']
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    userId = '9'
    institutionId = '16'
    degree = 'Bach of Engineering'
    graduationScore = '0'
    verificationId = '0'
    academicScore = '0'

    try:
        academic = Academic.objects.get(pk=academicId)
        logger.debug('####### Create academic');
    except Academic.DoesNotExist:
        logger.debug('####### Create academic- Academic NOT FOUND');
        academic = Academic(academicId=academicId, userId=userId, institutionId=institutionId, academicScore=academicScore, degree=degree, verificationId=verificationId, graduationScore=graduationScore)
    academic.save()
    return HttpResponseRedirect("/academics/" + academicId)

def update_academic (request, academicId):
    logger.debug('inside update_academic')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #institutionId = json_data['institutionId']
    #degree = json_data['degree']
    #graduationScore = json_data['graduationScore']
    #verifiedBy = json_data['verifiedBy']
    #verifiedDate = json_data['verifiedDate']
    #academicScore = json_data['academicScore']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    userId = '9'
    institutionId = '16'
    degree = 'Masters of Engineering'
    graduationScore = ''
    verificationId = '0'
    academicScore = '0'

    try:
        academic = Academic.objects.get(pk=academicId)
        logger.debug('####### Update academic');
    except Academic.DoesNotExist:
        logger.debug('####### Update academic NOT FOUND');
        academic = Academic(academicId=academicId, userId=userId, institutionId=institutionId, academicScore=academicScore, degree=degree, verificationId=verificationId, graduationScore=graduationScore)
    academic.degree = degree
    academic.save()
    return HttpResponseRedirect("/academics/" + academicId)

def delete_academic (request, academicId):
    logger.debug('inside delete_academic')
    logger.debug('------------')

    try:
        academic = Academic.objects.get(pk=academicId)
        logger.debug('####### Delete academic');
    except Academic.DoesNotExist:
        logger.debug('####### Academic not found');
    
    academic.delete()    
    return HttpResponseRedirect("/academics/" + academicId)

def create_honor (request, honorId):
    logger.debug('inside create_honor')
    #if request.method == 'POST':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #honor = json_data['honor']
    #honorType = json_data['honorType']
    #honorLevel = json_data['honorLevel']
    
    # -- Remove comments above during actual integration = Test code
    logger.debug('inside POST')
    userId = '9'
    honor = 'Won NCAA Basketball Championship'
    honorType = 'Sports'
    honorLevel = 'National'
    verificationId = '0'

    try:
        honor = Honor.objects.get(pk=honorId)
        logger.debug('####### Create honor');
    except Honor.DoesNotExist:
        logger.debug('####### Create honor NOT FOUND');
        honor = Honor(honorId=honorId, userId=userId, honor=honor, honorType=honorType, honorLevel=honorLevel, verificationId=verificationId)
    honor.save()
    return HttpResponseRedirect("/honors/" + honorId)

def update_honor (request, honorId):
    logger.debug('inside update_honor')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #honor = json_data['honor']
    #honorType = json_data['honorType']
    #honorLevel = json_data['honorLevel']
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    userId = '9'
    honorString = 'Won Chess Grand Master'
    honorType = 'Sports'
    honorLevel = 'National'
    verificationId = '0'

    try:
        honor = Honor.objects.get(pk=honorId)
        logger.debug('####### Update honor');
    except Honor.DoesNotExist:
        logger.debug('####### Update honor NOT FOUND');
        honor = Honor(honorId=honorId, userId=userId, honor=honorString, honorType=honorType, honorLevel=honorLevel, verificationId=verificationId)
    honor.honor = honorString
    honor.save()
    return HttpResponseRedirect("/honors/" + honorId)

def delete_honor (request, honorId):
    logger.debug('inside delete_honor')
    logger.debug('------------')

    try:
        honor = Honor.objects.get(pk=honorId)
        logger.debug('####### Delete honor');
    except Honor.DoesNotExist:
        logger.debug('####### Honor not found');
    
    honor.delete()    
    return HttpResponseRedirect("/honors/" + honorId)

def contribute_to_institution(request, contributionId):
    logger.debug('inside contribute to institution')
    
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #userId = json_data['userId']
    #amount = json_data['amount']
    #memo = json_data['memo']
    #institutionId = json_data['institutionId']
    #paymentId = Payment.objects.get(pk=userId, sequence='1')
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    userId = '9'
    paymentId = '1'
    amount = '500.00'
    memo = 'Contribution for Library computers'
    institutionId = '17'
    
    try:
        contribute = Contribution.objects.get(pk=contributionId)
        logger.debug('Found Contribution')
    except:
        logger.debug('Creating new contribution')
        contribute = Contribution(institutionId=institutionId,userId=userId, amount=amount, memo=memo, paymentId=paymentId)
    
    contribute.save()
    return HttpResponseRedirect("/contributions/" + contribute.contributionId)

def update_verification (request, performanceId):
    logger.debug('inside update_verification')
    logger.debug('------------')
    #if request.method == 'PUT':
    #json_data = simplejson.loads(request.body)
    #logger.debug('Raw Data: "%s"' % json_data)
    #verificationId = json_data['verificationId']
    #verifiedDate = json_data['verifiedDate']
    #status = json_data['status']
    #performanceScore = json_data['performanceScore']
    #verifyType = json_data['verifyType']
    
    #Score needs to be updated for performance or skill -- How to retrieve Performance based on verificationId
    
    # -- Remove comments above during actual integration
    #createDate = datetime.datetime.now()
    userId = '9'
    verifiedDate = datetime.datetime.now()
    status = 'Completed'
    performanceScore = '8'
    verifyType = 'Skill'

    if verifyType == 'Performance':
        try:
            performance = Performance.objects.get(pk=performanceId)
            performance.performanceScore = performanceScore
            logger.debug('####### Updated Performance with perforamnceScore');
        except:
            logger.debug('####### Update Performance - Could not find performance');
    
        performance.save()
        verificationId = performance.verificationId
    else:
        try:
            skill = Skill.objects.get(pk=performanceId)
            skill.skillScore = performanceScore
            logger.debug('####### Updated Skill with score');
        except:
            logger.debug('####### Update Skill - Could not find Skill');
    
        skill.save()
        verificationId = skill.verificationId
    
    try:
        verification = Verification.objects.get(pk=verificationId)
        logger.debug('####### Update verification');
    except Verification.DoesNotExist:
        logger.debug('####### Update verification NOT FOUND');
        verification = Verification(verifiedFor=performance.userId, verifiedBy=userId, verifiedDate=verifiedDate, status=status, verificationId=verificationId)
    verification.status = status
    verification.verifiedDate = verifiedDate
    verification.save()
    return HttpResponseRedirect("/verification/" + "'" + verificationId + "'")

### Views written by rahul

def home_redirect(request):

	""" Redirect to particular url based on condition """

	validate_user = request.session('validate_user') or None
	user = validate_user
	today = date.today()
	pro_details = {}
	project_detail = {}
	assessmentDict = {}
	user_verificationList = []
	verificationDict = {}
	verificationDict_list = []
	assessmentDict_list = []
	
	if validate_user.type =='Student' or validate_user.type =='Candidate':
		try:
			student_data = Student.objects.get(userId = validate_user.userId)
			student = student_data
			request.session['userData'] = student


		except:
			student_data = ''
			student = ''
		projectList = Project.objects.filter(project_deadline__gte = today)[:9]
		for pro in projectList:
			submission_list = Submission.objects.filter(projectId = pro.projectId)
			
			submission_count = len(submission_list)
			project_diff = pro.project_deadline - today
			project_diff = project_diff.days
			project_detail = {'submission_count':submission_count, 'diff':project_diff}
			pro_details[pro] = project_detail
		performance_list = Performance.objects.filter(userId = validate_user.userId)
		certification_list = Membership.objects.filter(userId = validate_user.userId)
		academic_list = Academic.objects.filter(userId = validate_user.userId)
		skill_list = Skill.objects.filter(userId = validate_user.userId)
		volunteer_list = Volunteer.objects.filter(userId = user.userId)
		language_list = Language.objects.filter(userId = user.userId)
		honor_list = Honor.objects.filter(userId = user.userId)
		user_testList = UserAssessment.objects.filter(assessmentBy = user.userId )
		for test in user_testList:

			if Test.objects.filter(testId = test.assessmentId).exists():
				assessment = Test.objects.get(testId = test.assessmentId)

				days_passed =  today - assessment.dueDate
				days_passed = days_passed.days
				assessmentDict = {'assessment_name':assessment.name, 'category':assessment.category, 'days_passed':days_passed, 'score':test.points_collected }
				assessmentDict_list.append(assessmentDict)


			
		user_verificationList = Verification.objects.filter(verifiedBy = user.userId)
		for ver in user_verificationList:
			if ver.projectId:
				verification_for = Project.objects.get(projectId = ver.projectId)
			if ver.performanceId:
				per_exists = Performance.objects.filter(performanceId = ver.performanceId).exists()
				verification_for = Performance.objects.get(performanceId = ver.performanceId) if per_exists else ''
			if ver.skillId:
				verification_for = Skill.objects.get(skillId = ver.skillId)
			if ver.certificationId:
				verification_for = Membership.objects.get(membershipId = ver.certificationId)
			if ver.academicId:
				verification_for = Academic.objects.get(academicId = ver.academicId)
			if ver.honorId:
				verification_for = Honor.objects.get(honorId = ver.honorId)
			if ver.languageId:
				verification_for = Language.objects.get(languageId = ver.languageId)
			if ver.volunteerId:
				verification_for = Volunteer.objects.get(volunteerId = ver.volunteerId)
			verifier = User.objects.get(userId = ver.verifiedBy)
			days_passed =  datetime.now() - ver.verifiedDate 
			days_passed = days_passed.days
			verificationDict = {'verification_for':verification_for, 'verified_by':verifier, 'days_passed':days_passed}
			verificationDict_list.append(verificationDict)
		
		return render(request,'grinder-view.html',locals())
	
	if validate_user.type =='Alumni':
		return render(request,'alumniprofile.html',{'user':validate_user})
	if validate_user.type =='Enterprise':
		enterprise = Enterprise.objects.get(userId = validate_user.userId)
		get_projectList = Project.objects.filter(userId = enterprise.userId)
		request.session['userData'] = enterprise
		request.session['displayName'] = enterprise.name
		try:
			project1 = get_projectList[0]

		except:
			pass
		try:
			project2 = get_projectList[1]
		except:
			pass
		try:
			project3 = get_projectList[2]
		except:
			pass
		try:
			project4 = get_projectList[3]
		except:
			pass
		try:
			project5 = get_projectList[4]
		except:
			pass
		try:
			project6 = get_projectList[5]
		except:
			pass
		try:
			project7 = get_projectList[6]
		except:
			pass
		try:
			project8 = get_projectList[7]
		except:
			pass
		return render(request,'enterprise-view.html',locals())
	
	if validate_user.type =='Institution':
		return render(request,'institution-view.html',{'user':validate_user})
	if validate_user.type == "Admin":
		return redirect('/assessment-assign-admin/')
    
	return render(request, 'index.html')

		



def user_login(request):
	validate_user = ''
	if request.method == 'POST':
		user_mail = request.POST.get('emailid')
		pwd = request.POST.get('password')

		try:
			validate_user = User.objects.get(emailId = user_mail, password = pwd)

		except:
			validate_user = ''

		if validate_user !='' :
			request.session['validate_user'] = validate_user
			if validate_user.type == "Admin":
				return redirect('/assessment-assign-admin/')
			return render(request, 'howitwork.html', {'user':validate_user})
		else:
			return redirect('/?status=FAIL')
	return render(request, 'index.html')

def user_logout(request):
	try:
		del request.session['validate_user']
		del request.session['registered_user']
		del request.session['displayName']
	except KeyError:
		pass
	return redirect('/')




def pre_landing(request):
	request.session['validate_user'] = request.session.get('registered_user','')
	return render(request, 'howitwork.html', {'register_user':True, 'user':request.session['validate_user']})


def landing_view(request):
	try:
		user = request.session['registered_user']
	except:
		user = request.session['validate_user']
		pass
	pass_status = request.GET.get('pass_status')
	today = date.today()
	pro_details = {}
	project_detail = {}
	submitted_projectList = []
	user_verificationList = []
	assessmentDict = {}
	verificationDict = {}
	verificationDict_list = []
	assessmentDict_list = []
	registered_user = User.objects.get(userId = user.userId)
	if registered_user.type =="Student" or registered_user.type =="Candidate":
		request.session['validate_user'] = registered_user
		try:
			student = Student.objects.get(userId = user.userId)
		except:
			student = ''
		projectList = Project.objects.filter(project_deadline__gte = today)[:9]
		for pro in projectList:
			submission_list = Submission.objects.filter(projectId = pro.projectId)
			submission_count = len(submission_list)
			project_diff = pro.project_deadline - today
			project_diff = project_diff.days
			project_detail = {'submission_count':submission_count, 'diff':project_diff}
			pro_details[pro] = project_detail
		performance_list = Performance.objects.filter(userId = user.userId)
		certification_list = Membership.objects.filter(userId = user.userId)
		academic_list = Academic.objects.filter(userId = user.userId)
		skill_list = Skill.objects.filter(userId = user.userId)
		volunteer_list = Volunteer.objects.filter(userId = user.userId)
		language_list = Language.objects.filter(userId = user.userId)
		honor_list = Honor.objects.filter(userId = user.userId)
		user_testList = UserAssessment.objects.filter(assessmentBy = user.userId )
		for test in user_testList:
			try:
				assessment = Test.objects.get(testId = test.assessmentId)
				days_passed =  today - assessment.dueDate
				days_passed = days_passed.days
				assessmentDict = {'assessment_name':assessment.name, 'category':assessment.category, 'days_passed':days_passed, 'score':test.points_collected }
				assessmentDict_list.append(assessmentDict)
			except:
				pass
		user_verificationList = Verification.objects.filter(verifiedBy = user.userId)
		for ver in user_verificationList:
			try:
				if ver.projectId:
					verification_for = Project.objects.get(projectId = ver.projectId)
				if ver.performanceId:
					verification_for = Performance.objects.get(performanceId = ver.performanceId)
				if ver.skillId:
					verification_for = Skill.objects.get(skillId = ver.skillId)
				if ver.certificationId:
					verification_for = Membership.objects.get(membershipId = ver.certificationId)
				if ver.academicId:
					verification_for = Academic.objects.get(academicId = ver.academicId)
				if ver.honorId:
					verification_for = Honor.objects.get(honorId = ver.honorId)
				if ver.languageId:
					verification_for = Language.objects.get(languageId = ver.languageId)
				if ver.volunteerId:
					verification_for = Volunteer.objects.get(volunteerId = ver.volunteerId)
			except:
				verification_for = None
			verifier = User.objects.get(userId = ver.verifiedBy)
			days_passed =  datetime.now() - ver.verifiedDate 
			days_passed = days_passed.days
			verificationDict = {'verification_for':verification_for, 'verified_by':verifier, 'days_passed':days_passed}
			verificationDict_list.append(verificationDict)
		return render(request,'grinder-view.html',locals())
	if registered_user.type =="Enterprise":
		request.session['validate_user'] = registered_user
		enterprise = Enterprise.objects.get(userId = user.userId)
		request.session['displayName'] = enterprise.name
		get_projectList = Project.objects.filter(userId = enterprise.userId)
		try:
			project1 = get_projectList[0]
		except:
			pass
		try:
			project2 = get_projectList[1]
		except:
			pass
		try:
			project3 = get_projectList[2]
		except:
			pass
		try:
			project4 = get_projectList[3]
		except:
			pass
		try:
			project5 = get_projectList[4]
		except:
			pass
		try:
			project6 = get_projectList[5]
		except:
			pass
		try:
			project7 = get_projectList[6]
		except:
			pass
		try:
			project8 = get_projectList[7]
		except:
			pass
		return render(request,'enterprise-view.html', locals())	
	return redirect('/')
	
def add_project(request):
	user = request.session['validate_user']
	ent_id = request.GET.get('ent_id')
	form = ProjectForm()
	if request.method=='POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid:
			
			formObj = form.save(commit = False)
			formObj.userId = ent_id
			deadline = request.POST.get('project_deadline')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			formObj.project_deadline = project_deadline
			formObj.save()
		else:
			return render(request, 'add-view.html', locals())
		return redirect('/landing_page/')
	return render(request, 'add-view.html', locals())
	
	
def view_project(request):
	user = request.session['validate_user']
	project_id = request.GET.get('pro_id')
	project = Project.objects.get(projectId=project_id)
	form = ProjectForm(instance = project)
	return render(request, 'view-project.html',locals())
	
	
def edit_project(request):
	user = request.session['validate_user']
	project_id = request.GET.get('pro_id')
	
	project = Project.objects.get(projectId=project_id)
	form = ProjectForm(instance = project)
	if request.method=='POST':
		form = ProjectForm(request.POST, request.FILES, instance = project)
		if form.is_valid:
			
			formObj = form.save(commit = False)
			formObj.userId = project.userId
			deadline = request.POST.get('project_deadline')
			try:
				conv = time.strptime(deadline,'%m-%d-%Y')
				project_deadline = time.strftime('%Y-%m-%d',conv)
				formObj.project_deadline = project_deadline
			except:
				pass
			formObj.save()
		else:
			return render(request, 'view-project.html', locals())
		return redirect('/landing_page/')
	return render(request, 'view-project.html', locals())


def delete_project(request):
	project_id=request.GET.get('pro_id')
	project = Project.objects.get(projectId = project_id)
	project.delete()
	return redirect('/landing_page/')
	
	
def upload_EnterpriseLogo(request):
	ct_id = request.POST.get('ct_id')
	image_file = request.FILES['img']
	enterprise = Enterprise.objects.get(userId = ct_id)
	
	enterprise.image = image_file
	enterprise.save()
	return redirect('/landing_page/')
	
def upload_StudentPhoto(request):
	ct_id = request.POST.get('ct_id')
	image_file = request.FILES['img']
	student = Student.objects.get(userId = ct_id)
	
	student.image = image_file
	student.save()
	return redirect('/landing_page/')
	
def submit_project(request):
	user = request.session['validate_user']
	pro_id = request.GET.get('project_id')

	try:
		submission_detail = Submission.objects.get(projectId = pro_id, userId = user.userId)
		submission_id = submission_detail.submissionId
	except:
		submission_detail = ''
		submission_id = ''
	if request.method == "POST":
		description = request.POST.get('description')
		url = request.POST.get('url')
		if submission_detail:
			submission_detail.solutionDetails = description
			submission_detail.projectUrl = url
			submission_detail.save()
		else:
			project_response = Submission(projectId = pro_id, userId = user.userId, solutionDetails = description, projectUrl = url)
			project_response.save()
		for fileObj in request.FILES.getlist('myfiles'):
			submission_file = Documents(submissionId = project_response.submissionId, file = fileObj)
			submission_file.save()
		return redirect('/challenge/')
	else:
		return render(request,'submit_project.html',locals())
	return render(request,'submit_project.html',locals())



		
def add_performance(request):
	user = request.session['validate_user']
	form = PerformanceForm()
	if request.method == "POST":
		form = PerformanceForm(request.POST, request.FILES)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
			conv1 = time.strptime(start_date,'%m-%d-%Y')
			startDate = time.strftime('%Y-%m-%d',conv1)
			formObj.start_date = startDate
			conv2 = time.strptime(end_date,'%m-%d-%Y')
			endDate = time.strftime('%Y-%m-%d',conv2)
			formObj.end_date = endDate
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-performance.html',locals())
	else:
		return render(request,'add-performance.html',locals())
		
	
	
def edit_performance(request):
	user = request.session['validate_user']
	perf_id = request.GET.get('perf_id')
	instance = Performance.objects.get(performanceId = perf_id)
	form = PerformanceForm(instance = instance)
	if request.method == "POST":
		form = PerformanceForm(request.POST, request.FILES,instance = instance)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
			conv1 = time.strptime(start_date,'%m-%d-%Y')
			startDate = time.strftime('%Y-%m-%d',conv1)
			formObj.start_date = startDate
			conv2 = time.strptime(end_date,'%m-%d-%Y')
			endDate = time.strftime('%Y-%m-%d',conv2)
			formObj.end_date = endDate
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'edit-performance.html',locals())
	else:
		return render(request,'edit-performance.html',locals())
			
	
	
	
def verify_project(request):
	user = request.session['validate_user']
	pro_id = request.GET.get('pro_id')
	form = VerifyForm()
	today = date.today()
	mail_from = user.emailId
	new_user = ''
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			formObj.status = 'Requested'
			pro_id = request.POST.get('pro_id')
			formObj.projectId = pro_id
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			formObj.when = project_deadline
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

		
def add_assessment(request):
	user = request.session['validate_user']
	perf_id = request.GET.get('perf_id')
	pro_id = request.GET.get('pro_id')
	instance = ''
	if perf_id:
		try:
			instance = Assessment.objects.get(performanceId = perf_id)
		except:
			pass
	else:
		try:
			instance = Assessment.objects.get(projectId = pro_id)
		except:
			pass
	if instance:
		form = AssessForm(instance = instance)
	else:
		form = AssessForm()
	if request.method == "POST":
		if instance:
			form = AssessForm(request.POST, instance = instance)
		else:	
			form = AssessForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			if perf_id:
				formObj.performanceId = perf_id
			if pro_id:
				formObj.projectId = pro_id
			challenge1Date = request.POST.get('challenge1Date')
			challenge2Date = request.POST.get('challenge2Date')
			conv1 = time.strptime(challenge1Date,'%m-%d-%Y')
			challenge1Date = time.strftime('%Y-%m-%d',conv1)
			formObj.challenge1Date = challenge1Date
			conv2 = time.strptime(challenge2Date,'%m-%d-%Y')
			challenge2Date = time.strftime('%Y-%m-%d',conv2)
			formObj.challenge2Date = challenge2Date
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add_assessment.html',locals())
	else:
		return render(request,'add_assessment.html',locals())

		
def edit_assessment(request):
	user = request.session['validate_user']
	perf_id = request.GET.get('perf_id')
	pro_id = request.GET.get('pro_id')
	if perf_id:
		instance = Assessment.objects.get(performanceId = perf_id)
	else:
		instance = Assessment.objects.get(projectId = pro_id)
	form = AssessForm(instance = instance)
	if request.method == "POST":
		form = AssessForm(request.POST, instance = instance)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			if perf_id:
				formObj.performanceId = perf_id
			if pro_id:
				formObj.projectId = pro_id
			challenge1Date = request.POST.get('challenge1Date')
			challenge2Date = request.POST.get('challenge2Date')
			conv1 = time.strptime(challenge1Date,'%m-%d-%Y')
			challenge1Date = time.strftime('%Y-%m-%d',conv1)
			formObj.challenge1Date = challenge1Date
			conv2 = time.strptime(challenge2Date,'%m-%d-%Y')
			challenge2Date = time.strftime('%Y-%m-%d',conv2)
			formObj.challenge2Date = challenge2Date
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'edit_assessment.html',locals())
	else:
		return render(request,'edit_assessment.html',locals())


def verify_performance(request):
	user = request.session['validate_user']
	pro_id = request.GET.get('pro_id')
	form = VerifyForm()
	mail_from = user.emailId
	today = date.today()
	new_user = ''
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			pro_id = request.POST.get('pro_id')
			formObj.performanceId = pro_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			formObj.when = project_deadline
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())
		
def add_skill(request):
	user = request.session['validate_user']
	form = SkillForm()
	skill_id = request.GET.get('skill_id')
	skill_name = request.GET.get('field1')
	try:
		skill = Skill.objects.get(skillId = skill_id)
		skill.description = skill_name
		skill.save()
	except:
		pass
	if request.method == "POST":
		form = SkillForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-skill.html',locals())
	else:
		return render(request,'add-skill.html',locals())

		
def verify_skill(request):
	user = request.session['validate_user']
	skill_id = request.GET.get('skill_id')
	form = VerifyForm()
	mail_from = user.emailId
	today = date.today()
	new_user = ''
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			skill_id = request.POST.get('skill_id')
			formObj.skillId = skill_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

def delete_skill(request):
	skill_id=request.GET.get('skill_id')
	skill = Skill.objects.get(skillId = skill_id)
	skill.delete()
	return redirect('/landing_page/')
		
def add_academics(request):
	user = request.session['validate_user']
	ace_id = request.GET.get('ace_id')
	degree_name = request.GET.get('field1')
	try:
		academic = Academic.objects.get(academicId = ace_id)
		academic.degree = degree_name
		academic.save()
	except:
		pass
	form = AcademicForm()
	if request.method == "POST":
		form = AcademicForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			formObj.institutionId = 1
			formObj.save()

			return redirect('/landing_page/')
		else:
			return render(request,'add-academic.html',locals())
	else:
		return render(request,'add-academic.html',locals())
		
		
def verify_academic(request):
	user = request.session['validate_user']
	ace_id = request.GET.get('ace_id')
	form = VerifyForm()
	mail_from = user.emailId
	new_user = ''
	today = date.today()
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			ace_id = request.POST.get('ace_id')
			formObj.academicId = ace_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

def delete_academic(request):
	adm_id=request.GET.get('adm_id')
	academic = Academic.objects.get(academicId = adm_id)
	academic.delete()		
	return redirect('/landing_page/')

	
def add_certification(request):
	user = request.session['validate_user']
	cert_id = request.GET.get('cert_id')
	certification_name = request.GET.get('field1')
	try:
		membership = Membership.objects.get(membershipId = cert_id)
		membership.description = certification_name
		membership.save()
	except:
		pass
	form = MembershipForm()
	if request.method == "POST":
		form = MembershipForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-certification.html',locals())
	else:
		return render(request,'add-certification.html',locals())

def verify_certification(request):
	user = request.session['validate_user']
	cert_id = request.GET.get('cert_id')
	form = VerifyForm()
	mail_from = user.emailId
	new_user = ''
	today = date.today()
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			cert_id = request.POST.get('cert_id')
			formObj.certificationId = cert_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

def delete_certification(request):
	cert_id=request.GET.get('cert_id')
	membership = Membership.objects.get(membershipId = cert_id)
	membership.delete()			
	return redirect('/landing_page/')


	
def add_volunteer(request):
	user = request.session['validate_user']
	vol_id = request.GET.get('vol_id')
	volunteer_name = request.GET.get('field1')
	try:
		voluteer = Volunteer.objects.get(volunteerId = vol_id)
		volunteer.name = volunteer_name
		volunteer.save()
	except:
		pass
	form = VolunteerForm()
	if request.method == "POST":
		form = VolunteerForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-volunteer.html',locals())
	else:
		return render(request,'add-volunteer.html',locals())

def verify_volunteer(request):
	user = request.session['validate_user']
	vol_id = request.GET.get('vol_id')
	form = VerifyForm()
	mail_from = user.emailId
	new_user = ''
	today = date.today()
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			vol_id = request.POST.get('vol_id')
			formObj.volunteerId = vol_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

def delete_volunteer(request):
	vol_id=request.GET.get('vol_id')
	volunteer = Volunteer.objects.get(volunteerId = vol_id)
	volunteer.delete()		
	return redirect('/landing_page/')

	
def add_language(request):
	user = request.session['validate_user']
	lang_id = request.GET.get('lang_id')
	lang_name = request.GET.get('field1')
	try:
		language = Language.objects.get(languageId = lang_id)
		language.name = lang_name
		language.save()
	except:
		pass
	form = LanguageForm()
	if request.method == "POST":
		form = LanguageForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-language.html',locals())
	else:
		return render(request,'add-language.html',locals())
	
def verify_language(request):
	user = request.session['validate_user']
	lang_id = request.GET.get('lang_id')
	form = VerifyForm()
	mail_from = user.emailId
	new_user = ''
	today = date.today()
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			lang_id = request.POST.get('lang_id')
			formObj.languageId = lang_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())
	
	
def delete_language(request):
	lang_id=request.GET.get('lang_id')
	language = Language.objects.get(languageId = lang_id)
	language.delete()
	return redirect('/landing_page/')
	
	
def add_honor(request):
	user = request.session['validate_user']
	hon_id = request.GET.get('hon_id')
	honor_name = request.GET.get('field1')
	try:
		honorObj = Honor.objects.get(honorId = hon_id)
		honorObj.honor = honor_name
		honorObj.save()
	except:
		pass
	form = HonorForm()
	if request.method == "POST":
		form = HonorForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.userId = user.userId
			
			formObj.save()
			return redirect('/landing_page/')
		else:
			return render(request,'add-honor.html',locals())
	else:
		return render(request,'add-honor.html',locals())

		
def verify_honor(request):
	user = request.session['validate_user']
	hon_id = request.GET.get('hon_id')
	form = VerifyForm()
	today = date.today()
	mail_from = user.emailId
	new_user = ''
	template_html = "email.html"
	if request.method == "POST":
		form = VerifyForm(request.POST)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.verifiedFor = user.userId
			hon_id = request.POST.get('hon_id')
			formObj.honorId = hon_id
			formObj.status = 'Requested'
			deadline = request.POST.get('when')
			conv = time.strptime(deadline,'%m-%d-%Y')
			project_deadline = time.strftime('%Y-%m-%d',conv)
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			try:
				verifier_user = User.objects.get(emailId__iexact = email)
			except:
				new_user = User(fName=first_name, lName=last_name, emailId=email, type="Candidate", password='12345', createDate=today)
				new_user.save()
				candidate = Student(userId=new_user.userId,candidate = True)
				candidate.save()
				verifier_user = new_user
			if new_user:
				new_userEmail = new_user.emailId
				new_userPwd = new_user.password
			else:
				new_userEmail = ''
				new_userPwd = ''
				
			formObj.verifiedBy = verifier_user.userId
			formObj.save()
			verificationId = formObj.verificationId
			mail_to = ['requests@talentomi.com']
			user_name = str(user.fName) + str(user.lName)
			subject = "Request for Verification from " + str(user_name)
			html_content = render_to_string(template_html, {'user':user,'verificationId':verificationId, 'first_name':first_name,'last_name':last_name,'new_userEmail':new_userEmail,'new_userPwd':new_userPwd})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/landing_page/')
		else:
			return render(request,'verify-view.html',locals())
	else:
		return render(request,'verify-view.html',locals())

def delete_honor(request):
	hon_id=request.GET.get('hon_id')
	honor = Honor.objects.get(honorId = hon_id)
	honor.delete()
	return redirect('/landing_page/')
	
def challenge(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	status = request.GET.get('status')
	if status:
		msg = "You have already Submitted your Challenge for this Project."
	else:
		msg = ''
	pro_details = {}
	today = date.today()

	projectList = Project.objects.filter(project_deadline__gte = today)[:9]
	for pro in projectList:
		submission_list = Submission.objects.filter(projectId = pro.projectId)
		submission_count = len(submission_list)
		project_diff = pro.project_deadline - today
		project_diff = project_diff.days
		project_detail = {'submission_count':submission_count, 'diff':project_diff}
		pro_details[pro] = project_detail
	if user:
		performance_list = Performance.objects.filter(userId = user.userId)
		certification_list = Membership.objects.filter(userId = user.userId)
		academic_list = Academic.objects.filter(userId = user.userId)
		skill_list = Skill.objects.filter(userId = user.userId)
		volunteer_list = Volunteer.objects.filter(userId = user.userId)
		language_list = Language.objects.filter(userId = user.userId)
		honor_list = Honor.objects.filter(userId = user.userId)
	return render(request, 'challenge.html',locals())

def talentomi(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	return render(request, 'why-talentomi.html',locals())

def howitworks(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	return render(request, 'howitwork.html',locals())


def verifyview(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		ver_id = request.GET.get('ver_id')
		verification = ''
		completed_verificationDict = {}
		pending_verificationDict = {}
		if ver_id:
			verificationObj = Verification.objects.get(verificationId = ver_id)
			verified_for = User.objects.get(userId = verificationObj.verifiedFor) 
			verification = {'verification':verificationObj, 'verified_for':verified_for}
		completed_verifications = Verification.objects.filter(status__iexact = 'Completed', verifiedBy = user.userId)
		for ver in completed_verifications:
			verified_for = ver.verifiedFor
			try:
				verified_for = User.objects.get(userId = verified_for)
			except:
				verified_for = ''
				
			verified_by = ver.verifiedBy
			try:
				verified_by = User.objects.get(userId = verified_by)
			except:
				verified_by = ''
			completed_verificationDict[ver] = {'verified_for':verified_for, 'verified_by':verified_by}
		pending_verifications = Verification.objects.filter(Q(status__iexact = 'Requested')|Q( status__iexact = 'Accepted'),Q(verifiedBy = user.userId)|Q(verifiedFor = user.userId))
		for ver in pending_verifications:
			verified_for = ver.verifiedFor
			try:
				verified_for = User.objects.get(userId = verified_for)
			except:
				verified_for = ''
				
			verified_by = ver.verifiedBy
			try:
				verified_by = User.objects.get(userId = verified_by)
			except:
				verified_by = ''
			pending_verificationDict[ver] = {'verified_for':verified_for, 'verified_by':verified_by}
		try:
			verification_id = int(ver_id)
		except:
			pass
		return render(request, 'varification.html',locals())
	else:
		return redirect('/')
		
		
def save_verification(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	ver_id = request.GET.get('ver_id')
	
	verificationObj = Verification.objects.get(verificationId = ver_id)
	if user:
		if request.method =="POST":
			status = request.POST.get('status')
			rate_quality = request.POST.get('rate_quality')
			rate_communication = request.POST.get('rate_communication')
			rate_expertise = request.POST.get('rate_expertise')
			rate_ontime = request.POST.get('rate_ontime')
			rate_responsive = request.POST.get('rate_responsive')
			rate_budget = request.POST.get('rate_budget')
			rate_ownership = request.POST.get('rate_ownership')
			rate_professionalism = request.POST.get('rate_professionalism')
			rate_hire = request.POST.get('rate_hire')
			comments = request.POST.get('additional_comments')
			verificationObj.status = 'Completed'
			verificationObj.workQuality = rate_quality
			verificationObj.communication = rate_communication
			verificationObj.expertise = rate_expertise
			verificationObj.onTime = rate_ontime
			verificationObj.responsiveness = rate_responsive
			verificationObj.withinBudget = rate_budget
			verificationObj.ownerShip = rate_ownership
			verificationObj.professionalism = rate_professionalism
			verificationObj.wouldHireAgain = rate_hire
			verificationObj.comments = comments
			verificationObj.verifiedBy = user.userId
			verificationObj.save()
			return redirect('/verify-view/')
		else:
			return redirect('/verify-view/?ver_id='+str(ver_id))
	else:
		return redirect('/')

def assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
		
	return render(request, 'assessment.html',locals())
## View being used for displaying assessment home page and the list upon it.	
def assessmentview(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	
	assess_id = request.GET.get('assess_id')
	key = request.GET.get('key')
	pending_assessmentList = []
	completed_assessmentList = []
	pending_assessmentDict = {}
	completed_assessmentDict = {}
	completed_assessment = ''
	exclude_assessment = []
	try:
		assessObj = Test.objects.get(testId = assess_id)
	except:
		assessObj = ''
	if user:
		if user.type == "Enterprise":
			completed_assessmentList = Test.objects.filter(status__iexact = 'Closed', assessmentBy = user.userId)
		if user.type =="Student" or user.type =="Candidate":
			student_completedList = UserAssessment.objects.filter(assessmentBy = user.userId, status = "Closed")
			for assess in student_completedList:
				try:
					completed_assessmentObj = Test.objects.get(testId = assess.assessmentId)
					completed_assessmentList.append(completed_assessmentObj)
				except:
					pass
		for ver in completed_assessmentList:
			assessment_for = ver.assessmentFor
			try:
				assessment_for = User.objects.get(userId = verified_for)
			except:
				asessment_for = ''
			
			completed_assessmentDict[ver] = {'assessment_for':assessment_for}
		if user.type == "Enterprise":
			pending_assessmentList = Test.objects.filter(status__iexact = 'Open', assessmentBy = user.userId)
		if user.type =="Student" or user.type =="Candidate":
			student_completedList = UserAssessment.objects.filter(assessmentBy = user.userId)
			
			for assess in student_completedList:
				exclude_assessment.append(assess.assessmentId)
		pending_assessmentList = Test.objects.filter(status__iexact = 'Open').exclude(testId__in = exclude_assessment)
		for ver in pending_assessmentList:
			assessed_for = ver.assessmentFor
			try:
				assessed_for = User.objects.get(userId = assessed_for)
			except:
				assessed_for = ''
				
			
			pending_assessmentDict[ver] = {'assessed_for':assessed_for}
		try:
			assess_id = int(assess_id)
		except:
			assess_id = ''
		try:
			completed_assessment = UserAssessment.objects.get(assessmentId = assess_id,assessmentBy = user.userId)
		except:
			pass
		return render(request, 'assessmentview.html',locals())
	else:
		return redirect('/')
		

	
## View used for creating new Assessment
def create_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		form = AssessmentForm()
		if request.method == "POST":
			form = AssessmentForm(request.POST)
			if form.is_valid():
				formObj = form.save(commit = False)
				formObj.assessmentBy = user.userId
				formObj.status = "Open"
				due_Date = request.POST.get('dueDate')
				conv1 = time.strptime(due_Date,'%m-%d-%Y')
				due_Date = time.strftime('%Y-%m-%d',conv1)
				formObj.dueDate = due_Date
				formObj.save()
				return redirect('/assessment-view/')
			else:
				return render(request,'create_assessment.html',locals())
		else:
			return render(request,'create_assessment.html',locals())
	
		return render(request,'create_assessment.html',locals())
	else:
		return redirect('/')
		
## View for Editing Assessment
def update_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	assess_id = request.GET.get('assess_id')
	instance = Test.objects.get(testId = assess_id)
	form = AssessmentForm(instance = instance)
	if request.method == "POST":
		form = AssessmentForm(request.POST, instance = instance)
		if form.is_valid():
			formObj = form.save(commit = False)
			formObj.assessmentBy = user.userId
			formObj.status = "Open"
			due_Date = request.POST.get('dueDate')
			conv1 = time.strptime(due_Date,'%m-%d-%Y')
			due_Date = time.strftime('%Y-%m-%d',conv1)
			formObj.dueDate = due_Date
			formObj.save()
			return redirect('/assessment-view/')
		else:
			return render('update_assessment.html')
		
	return render(request,'update_assessment.html')


### View for deleting Assessment	
def delete_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	assess_id = request.GET.get('assess_id')
	if user.type == "Enterprise":
		
		testObj = Test.objects.get(testId = assess_id)
		testObj.delete()
		return redirect('/assessment-view/')
	else:
		return redirect('/')

def view_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		assess_id = request.GET.get('assess_id')	
		questAnswerDict = {}
		
		assessmentObj = Test.objects.get(testId = assess_id)
		QuestionList = Question.objects.filter(assessmentId = assess_id)
		for quest in QuestionList:
			answerList = Answer.objects.filter(questionId = quest.questionId)
			questAnswerDict[quest] = answerList
		return render(request,'view-AssessmentDetail.html', locals())
	else:
		return redirect('/')

def import_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		assess_id = request.GET.get('assess_id')
		assessObj = Test.objects.get(testId = assess_id)
		if request.method =="POST":
			excel_file = request.FILES['excel_file']
			myexcel = xlrd.open_workbook(file_contents=excel_file.read())
			sheet = myexcel.sheet_by_index(0)

			for row_index in range(0,sheet.nrows):
				question = sheet.cell(row_index,0).value
				weightage = sheet.cell(row_index,1).value
				points = sheet.cell(row_index,2).value
				type = sheet.cell(row_index,3).value
				answer1 = sheet.cell(row_index,4).value
				answer2 = sheet.cell(row_index,5).value
				answer3 = sheet.cell(row_index,6).value
				answer4 = sheet.cell(row_index,7).value
				answer5 = sheet.cell(row_index,8).value
				correct_answer = sheet.cell(row_index,9).value
				questionObj = Question(assessmentId = assess_id,detail = question, weightage = weightage, points = points,type=type,category = assessObj.category)
				questionObj.save()
				if type == 'Descriptive':
					answerObj = Answer(detail = answer1, questionId = questionObj.questionId)
				else:
					answerObj1 = Answer(detail = answer1, questionId = questionObj.questionId)
					answerObj1.save()
					answerObj2 = Answer(detail = answer2, questionId = questionObj.questionId)
					answerObj2.save()
					answerObj3 = Answer(detail = answer3, questionId = questionObj.questionId)
					answerObj3.save()
					answerObj4 = Answer(detail = answer4, questionId = questionObj.questionId)
					answerObj4.save()
					answerObj5 = Answer(detail = answer5, questionId = questionObj.questionId)
					answerObj5.save()
				try:
					correctAnswer = Answer.objects.get(detail__iexact = correct_answer)
					questionObj.answerId = correctAnswer.answerId
					questionObj.save()
				except:
					pass
					
			return redirect('/assessment-view/?key=Create&assess_id='+str(assess_id))
		return render(request,'import_assessment.html',locals())
	else:
		return redirect('/')
	
def add_question(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	assess_id = request.GET.get('assess_id')
	assessObj = Test.objects.get(testId = assess_id)
	if request.method == "POST":
		question = request.POST.get('detail')
		weightage = request.POST.get('weightage')
		points = request.POST.get('points')
		type = request.POST.get('type')
		category = request.POST.get('category')
		correct_answer = request.POST.get('correct_answer')
		Quest = Question(assessmentId = assess_id, detail = question, weightage = weightage, points = points, type = type, category = assessObj.category)
		Quest.save()
		for i in range(1,5):
			answer = request.POST.get('answer'+str(i))
			answerObj = Answer(detail = answer, questionId = Quest.questionId)
			answerObj.save()
		try:
			correctAnswer = Answer.objects.get(detail__iexact = correct_answer)
			Quest.answerId = correctAnswer.answerId
			Quest.save()
		except:
			pass
		return redirect('/assessment-view/')
	else:
		return render(request,'add_Assess_question.html',locals())

def add_answer(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if request.method == "POST":
		answer = request.POST.get('answer')
		return redirect('/asessment-view/')
	else:
		return render('add_question.html')

def save_userResponse(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	assess_id = request.GET.get('assess_id')
	if request.method == "POST":
		question_list = request.POST.getlist('question')
		points_aquired = 0
		for quest in question_list:
			questObj = Question.objects.get(questionId = quest)
			if questObj.type == "Descriptive":
				user_response = request.POST.get('answer' + str(quest))
			else:
				user_response = request.POST.get('answer' + str(quest))
				user_response = int(user_response)
			#questObj = Question.objects.get(questionId = quest)
			if questObj.answerId == user_response:
				points_aquired = points_aquired + questObj.points
		userResponseObj = UserAssessment(assessmentId = assess_id, assessmentBy = user.userId, points_collected = points_aquired, status = "Closed")
		userResponseObj.save()
		return redirect('/assessment-view/')
	return redirect('/assessment-view/?key=Create&assess_id=' + str(assess_id))

	
def delete_assessment(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		assess_id = request.GET.get('assess_id')
		error = ''
		try:
			assessmentObj = Test.objects.get(testId = assess_id)
			questionList = Question.objects.filter(assessmentId = assessmentObj.testId)
			for quest in questionList:
				answer_list = Answer.objects.filter(questionId = quest.questionId)
				for ans in answer_list:
					ans.delete()
				quest.delete()
			assessmentObj.delete()
		except:
			error = "Could not delete !"
		
		return redirect('/assessment-view/')
	else:
		return redirect('/')

def delete_question(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if user:
		assess_id = request.GET.get('assess_id')
		quest_id = request.GET.get('quest_id')
		try:
			questObj = Question.objects.get(questionId = quest_id)
			answer_list = Answer.objects.filter(questionId = questObj.questionId)
			for ans in answer_list:
				ans.delete()
			questObj.delete()
		
		except:
			error = "Could not delete !"
		
		return redirect('/assessment-view/')
	else:
		return redirect('/')
	
def assessmenthome(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
		
	return render(request, 'assessmenthome.html',locals())
	
	
##Code for LinkedIn integration
def done(request):
    
	details = request.user.social_auth.get().extra_data
	try:
		userPresent = User.objects.get(emailId = details['email_address'])
		request.session['registered_user'] = userPresent
		request.session['userDetails'] = details
	except:
		userPresent = ''
	if not userPresent:
		userData = User(fName = details['first_name'], lName = details['last_name'], type = 'Student', emailId = details['email_address'], password = 'linkedIn', createDate = datetime.today())
		userData.save()
		student = Student(userId=userData.userId, collegeName=details['educations']['education']['school-name'],candidate = False)
		student.save()
		user_jobs = details['positions']['position']
		try:
			if user_jobs[0]:
				company1_name = user_jobs[0]['company']['name']
				if user_jobs[0]['is_current'] == True:
					end_date1 = ''
				else:
					end_date1 = user_jobs[0]['company']['name']
		except:
			pass
		request.session['registered_user'] = userData
	return HttpResponseRedirect('/landing_page/')


def login_success(request):
    
    return HttpResponseRedirect('/landing_page/')
    
def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('base.html', {'messages': messages},
                              RequestContext(request))

def assessment_home_enterprise(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	student_key = request.POST.get('searchStudent')
	assess_key = request.POST.get('searchAssessment')
	if student_key:
		searched_studentList = User.objects.filter(Q(fName__icontains = student_key)|Q(lName__icontains = student_key), type = "Student")
	if assess_key:
		searched_assessmentList = Test.objects.filter(name__icontains = assess_key)
	all_assessmentList = Test.objects.filter(status = "Open")
	all_userList = User.objects.filter(type = "Student")
	assessment_list = request.POST.getlist('assessment')
	student_list = request.POST.getlist('assessment_assign')
	if assessment_list and student_list:
		for assess in assessment_list:
			for student in student_list:
				try:
					assigned_assessmentObj = AssignedAssessment.objects.get(assessmentId = assess, assessmentFor = student)
				except:
					assigned_assessmentObj = ''
				if not assigned_assessmentObj:
					userResponseObj = AssignedAssessment(assessmentId = assess, assessmentFor = student)
					userResponseObj.save()

	return render(request, 'assessmenthomeenterprise.html',locals())	
	

	
def assessment_home_candidate(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	user_assessment = []
	searched_assessment = []
	search_key = request.POST.get('searchkeyword')
	if search_key:
		searched_assessment = Test.objects.filter(name__icontains = search_key)
	assessmentList  = Test.objects.filter(status = "Open" )	
	assigned_assessment = AssignedAssessment.objects.filter(assessmentFor = user.userId)
	for assessment in assigned_assessment:
		if Test.objects.filter(testId = assessment.assessmentId).exists():
			assessmentObj = Test.objects.get(testId = assessment.assessmentId)
			user_assessment.append(assessmentObj)
	return render(request, 'assessmenthomecandidate.html',locals())	
	

def assessmenthomeadmin(request):
	search_key = request.GET.get('searchkeyword')
	try:
		user = request.session['validate_user']
		
		if user.type == "Admin":
			today = datetime.now()
			requested_verification_list = Verification.objects.filter(status = "Requested").distinct()
			from datetime import *
			this_week_rv = requested_verification_list.filter(verifiedDate__gte = today + timedelta(-7)).distinct()
			last_week_rv = requested_verification_list.filter(verifiedDate__lte = today + timedelta(-7),
								                              verifiedDate__gte = today + timedelta(-14)).distinct()
			beyond_rv = requested_verification_list.filter(verifiedDate__lte = today + timedelta(-14)).distinct()
	except:
		user = ''
	if search_key:
		searched_verification_list = Verification.objects.filter(status = "Requested", verificationDescription__icontains = search_key)
	return render(request, 'assessmenthomeadmin.html',locals())	
	
	
def get_assessmentData(request):
	get_user = request.GET.get('field1')
	get_assessment = request.GET.get('field1')
	user_assessmentList = []
	assess_userList = []
	if get_user:
		try:
			assess_list = AssignedAssessment.objects.filter(assessmentFor = get_user)
			for assess in assess_list:
				assessObj = Test.objects.get(testId = assess.assessmentId)
				user_assessmentList.append(assessObj)
		except:
			pass
	if get_assessment:
		try:
			assess_list = AssignedAssessment.objects.filter(assessmentId = get_assessment)
			for assess in assess_list:
				userObj = User.objects.get(userId = assess.assessmentFor)
				assess_userList.append(userObj)
		except:
			pass
	return render(request, 'assessment-data.html', locals())



def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k.startswith(s)}


import simplejson as json
def authorize_verifications(request):
	
	user = request.session.get('validate_user')
	res = {}
	success = False
	if user is not None:
		if user.type == "Admin":
			if request.method == "POST":
				data = dict(request.POST.items())
				if "csrfmiddlewaretoken" in data.keys():
					del data['csrfmiddlewaretoken']
				ver_dict = slicedict(data, 'verification_')
				
				for k,v in ver_dict.items():
					ver = v
					vnum = k.split('verification')[1]
					ver_notes = data.get('ver_notes'+vnum)
					try:
						verification = Verification.objects.get(verificationId = int(ver))
						if data.get('action') == "Rejection":
							verification.authorized = False
						elif data.get('action') == "Authorization":
							verification.authorized = True
						verification.authorize_notes = ver_notes
						verification.authorize_action = True
						verification.authorize_action_by = user.userId
						verification.save()
						success = True
					except:
						success = False
						break
						

				res['success'] = success
	return HttpResponse(json.dumps(res), mimetype = "application/json")
	
def contact_us(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		msg = request.POST.get('message')
		send_mail(subject,msg,email,['admin@talentomi.com'], fail_silently=False)
		return redirect('/')
	return render(request, 'contact-us.html',locals())			
		
		
def forgot_password(request):
	template_html = "forget-passwordMail.html"
	if request.method == "POST":
		email = request.POST.get('emailid_recovery')
		try:
			userObj = User.objects.get(emailId__iexact = email)
		except:
			userObj = ''
			
		if userObj:
			new_pass = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
			userObj.password = new_pass
			userObj.save()
			mail_from = 'admin@talentomi.co'
			mail_to = [email]
			
			subject = "Request for Reset Password "
			html_content = render_to_string(template_html, {'user':userObj,'new_pass':new_pass, 'date_today':datetime.today()})
			msg = EmailMessage(subject, html_content, mail_from, mail_to)
			msg.content_subtype = "html"
			try:
				msg.send()
				logger.debug('Mail Sent')
			except:
				logger.debug('Mail Sending Failed')
				pass
			return redirect('/')
				
	return render(request,'index.html', locals())
	
	
def reset_password(request):
	try:
		user = request.session['validate_user']
	except:
		user = ''
	if request.method =="POST":
		old_pwd = request.POST.get('curr_pwd')
		new_pwd = request.POST.get('new_pwd')
		try:
			userObj = User.objects.get(password__exact = old_pwd, emailId = user.emailId )
			pass_status = 'PASS'
		except:
			userObj = ''
			pass_status = 'FAIL'
		if userObj:
			userObj.password = new_pwd
			userObj.save()
			
			return redirect('/landing_page/?pass_status=' + pass_status)
			
	
	return redirect('/landing_page/?pass_status=' + pass_status)