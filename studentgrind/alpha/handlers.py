import re
from piston.handler import BaseHandler
from piston.utils import rc, throttle

from alpha.models import Academic, User, Accomplishment, Address, Alumni,\
    Campaign, Contribution, Enterprise, Institution, Payment, Performance, Membership, Project,\
    Score, Skill, Student, Subscription, UserAddress, Verification, Honor


import logging
from django.shortcuts import get_object_or_404

logger = logging.getLogger('alpha')
    
class BlogPostHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    fields = ('performanceId', 'userId','description', 'video','doc','verificationId', 'performanceScore')
    exclude = ('id', re.compile(r'^private_'))
    model = Performance

   

    def read(self, request, item_id):
        logger.debug('Good!')
        if item_id =='all':
            return Performance.objects.all()
        else:
            return Performance.objects.get(pk=item_id)

    
    def update(self, request, item_id):
        logger.debug('Something went wrong!')
        post = Performance.objects.get(pk=item_id)

        post.name = request.PUT.get('name')
        post.save()

        return post
    
    def create(self, request, performanceId):
        logger.debug('Something went wrong2!')

    def delete(self, request, performanceId):
        logger.debug('Something went wrong2!')
         
        post = Performance.objects.get(pk=performanceId)

#        if not request.user == post.author:
#            return rc.FORBIDDEN # returns HTTP 401

        post.delete()

        return rc.DELETED # returns HTTP 204

class ArbitraryDataHandler(BaseHandler):
    methods_allowed = ('GET',)

    def read(self, request, username, data):
        user = 'test'

        return { 'user': user, 'data_length': len(data) }
           
class UserHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = User
    fields = ('userId','fName', 'lName', 'dob','type','contactPhone','emailId','password','gender','imageref','create_dt','facebook','linkedIn','github')
              
    def create(self, request):
        logger.debug('in UserHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = User(fName=attrs['fName'],lName=attrs['lName'],dob=attrs['dob'],emailId=attrs['emailId'],password=attrs['password'],gender=attrs['gender'],type=attrs['type'],contactPhone=attrs['contactPhone'],createDate=attrs['createDate'],facebook=attrs['facebook'],linkedIn=attrs['linkedIn'],github=attrs['github'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, userId):
        logger.debug('User update!')
        logger.debug(request.data)
        logger.debug(userId)

        post = User.objects.get(pk=userId)

        post.emailId = request.PUT.get('emailId')
        post.fName = request.PUT.get('fName')
        post.lName = request.PUT.get('lName')
        post.save()

        return post
                           
class PerformanceHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Performance
    fields = ('performanceId', 'userId','description', 'video', 'doc','verificationId','performanceScore')
              
    def create(self, request):
        logger.debug('in PerformanceHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Performance(userId=attrs['userId'],description=attrs['description'],video=attrs['video'],doc=attrs['doc'],verificationId=attrs['verificationId'],performanceScore=attrs['performanceScore'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, performanceId):
        logger.debug('Performance update!')
        logger.debug(request.data)
        logger.debug(performanceId)

        post = Performance.objects.get(pk=performanceId)

        post.video = request.PUT.get('video')
        post.description = request.PUT.get('description')
        post.doc = request.PUT.get('doc')
        post.save()

        return post

class AccomplishmentHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Accomplishment
    fields = ('accomplishmentId', 'userId','description')
              
    def create(self, request):
        logger.debug('in AccomplishmentHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Accomplishment(userId=attrs['userId'],description=attrs['description'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, accomplishmentId):
        logger.debug('Accomplishment update!')
        logger.debug(request.data)
        logger.debug(accomplishmentId)

        post = Accomplishment.objects.get(pk=accomplishmentId)

        post.description = request.PUT.get('description')
        post.save()

        return post

class MembershipHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Membership
    fields = ('membershipId', 'userId','description')
              
    def create(self, request):
        logger.debug('in MembershipHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Membership(userId=attrs['userId'],description=attrs['description'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, membershipId):
        logger.debug('Membership update!')
        logger.debug(request.data)
        logger.debug(membershipId)

        post = Membership.objects.get(pk=membershipId)

        post.description = request.PUT.get('description')
        post.save()

        return post

class PaymentHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Payment
    fields = ('paymentId', 'userId','createDate', 'sequence','paymentType','paymentNumber','expiration','cvv')
              
    def create(self, request):
        logger.debug('in PaymentHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Payment(userId=attrs['userId'],createDate=attrs['createDate'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, paymentId):
        logger.debug('createDate update!')
        logger.debug(request.data)
        logger.debug(paymentId)

        post = Payment.objects.get(pk=paymentId)

        post.createDate = request.PUT.get('createDate')
        post.save()

        return post

class PasswordHandler(BaseHandler):
    allowed_methods = ('GET')
    model = User
    fields = ('emailId','fName','lName','emailId','password')
              
    def read(self, request, emailId=None):
        print emailId
        logger.debug(emailId)
        user = get_object_or_404(User,emailId=emailId)
        print user.emailId
        return user
    
class AlumniHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Alumni
    fields = ('userId','mentorship')
              
    def create(self, request):
        logger.debug('in AlumniHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Alumni(mentorship=attrs['mentorship'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, userId):
        logger.debug('Alumni update!')
        logger.debug(request.data)
        logger.debug(userId)

        post = Alumni.objects.get(pk=userId)

        post.userId = request.PUT.get('userId')
        post.mentorship = request.PUT.get('mentorship')
        post.save()

        return post

class StudentHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Student
    fields = ('userId','collegeName', 'photo', 'video', 'goalStatement', 'salary', 'status')
              
    def create(self, request):
        logger.debug('in StudentHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Student(collegeName=attrs['collegeName'])
        post.save()
        post = Student(photo=attrs['photo'])
        post.save()
        post = Student(video=attrs['video'])
        post.save()
        post = Student(goalStatement=attrs['goalStatement'])
        post.save()
        post = Student(salary=attrs['salary'])
        post.save()
        post = Student(status=attrs['status'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, userId):
        logger.debug('Student update!')
        logger.debug(request.data)
        logger.debug(userId)

        post = Student.objects.get(pk=userId)

        post.userId = request.PUT.get('userId')
        post.collegeName = request.PUT.get('collegeName')
        post.save()
        post.video = request.PUT.get('video')
        post.save()
        post.photo = request.PUT.get('photo')
        post.save()
        post.goalStatement = request.PUT.get('goalStatement')
        post.save()
        post.salary = request.PUT.get('salary')
        post.save()
        post.status = request.PUT.get('status')
        post.save()

        return post

class VerificationHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Verification
    fields = ('verificationId', 'verifiedFor','verifiedBy','status','verifiedDate','verificationDescription')
              
    def create(self, request):
        logger.debug('in VerificationHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Verification(verificationId=attrs['verificationId'],verifiedDate=attrs['verifiedDate'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, verificationId):
        logger.debug('Verification update!')
        logger.debug(request.data)
        logger.debug(verificationId)

        post = Payment.objects.get(pk=verificationId)

        post.createDate = request.PUT.get('createDate')
        post.save()

        return post

class SkillHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Skill
    fields = ('skillId', 'userId','description', 'verificationId','skillScore')
              
    def create(self, request):
        logger.debug('in SkillHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Skill(userId=attrs['userId'],description=attrs['description'],verificationId=attrs['verificationId'],skillScore=attrs['skillScore'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, skillId):
        logger.debug('Skill update!')
        logger.debug(request.data)
        logger.debug(skillId)

        post = Skill.objects.get(pk=skillId)

        post.video = request.PUT.get('userId')
        post.description = request.PUT.get('description')
        post.doc = request.PUT.get('verificationId')
        post.doc = request.PUT.get('skillScore')
        post.save()

        return post

class AcademicHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Academic
    fields = ('academicId','institutionId','userId','degree','graduationScore','verifiedBy','verifiedDate','academicScore')
              
    def create(self, request):
        logger.debug('in AcademicHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Academic(userId=attrs['userId'],degree=attrs['degree'],institutionId=attrs['institutionId'],academicScore=attrs['academicScore'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, academicId):
        logger.debug('Academic update!')
        logger.debug(request.data)
        logger.debug(academicId)

        post = Academic.objects.get(pk=academicId)

        post.userId = request.PUT.get('userId')
        post.degree = request.PUT.get('degree')
        post.institutionId = request.PUT.get('institutionId')
        post.academicScore = request.PUT.get('academicScore')
        post.save()

        return post

class HonorHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Honor
    fields = ('honorId', 'userId','honor', 'honorType','honorLevel')
              
    def create(self, request):
        logger.debug('in HonorHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Honor(userId=attrs['userId'],honor=attrs['honor'],honorType=attrs['honorType'],honorLevel=attrs['honorLevel'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, honorId):
        logger.debug('Honor update!')
        logger.debug(request.data)
        logger.debug(honorId)

        post = Honor.objects.get(pk=honorId)

        post.userId = request.PUT.get('userId')
        post.honorType = request.PUT.get('honorType')
        post.honorLevel = request.PUT.get('honorLevel')
        post.honor = request.PUT.get('honor')
        post.save()

        return post

class ContributionHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT', 'DELETE')
    model = Contribution
    fields = ('contributionId', 'userId','institutionId', 'amount', 'memo', 'paymentId')
              
    def create(self, request):
        logger.debug('in ContributionHandler create');
        print request
     
        logger.debug(request.data)
        attrs = self.flatten_dict(request.data)
        print(attrs)
        print(attrs['password'])
     
        post = Contribution(userId=attrs['userId'],institutionId=attrs['institutionId'],amount=attrs['amount'],memo=attrs['memo'], paymentId=attrs['paymentId'])
        post.save()
        logger.debug('saved')
        return post

    def update(self, request, contributionId):
        logger.debug('Contribution update!')
        logger.debug(request.data)
        logger.debug(contributionId)

        post = Contribution.objects.get(pk=contributionId)

        post.userId = request.PUT.get('userId')
        post.institutionId = request.PUT.get('institutionId')
        post.amount = request.PUT.get('amount')
        post.memo = request.PUT.get('memo')
        post.paymentId = request.PUT.get('paymentId')
        post.save()

        return post

