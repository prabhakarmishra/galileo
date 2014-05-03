from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from alpha.handlers import BlogPostHandler, UserHandler, PerformanceHandler, \
AccomplishmentHandler, MembershipHandler, PaymentHandler, VerificationHandler, SkillHandler, \
AcademicHandler, HonorHandler, ContributionHandler 
#, OrderHandler, OrderItemHandler, PasswordHandler, OrderItemAnalyticsHandler,\
 #   PairingsHandler, FavoritesHandler
#from studentgrind.alpha.handlers import CommentHandler,OrderViewHandler
from piston.emitters import Emitter, JSONEmitter
from alpha import views
from django.conf.urls import patterns, include, url
import social_auth


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
blogpost_resource = Resource(handler=BlogPostHandler)
user_resource = Resource(handler=UserHandler)
performance_resource = Resource(handler=PerformanceHandler)
accomplishment_resource = Resource(handler=AccomplishmentHandler)
membership_resource = Resource(handler=MembershipHandler)
payment_resource = Resource(handler=PaymentHandler)
verification_resource = Resource(handler=VerificationHandler)
skill_resource = Resource(handler=SkillHandler)
academic_resource = Resource(handler=AcademicHandler)
honor_resource = Resource(handler=HonorHandler)
contribution_resource = Resource(handler=ContributionHandler)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'alpha.views.home', name='home'),
    # url(r'^Xploora/', include('Xploora.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
   url(r'^performances/(?P<performanceId>[^/]+)/create/$', 'alpha.views.create_performance'),
   url(r'^performances/(?P<performanceId>[^/]+)/update/$', 'alpha.views.update_performance'),
   url(r'^performances/(?P<performanceId>[^/]+)/$', performance_resource),
   url(r'^accomplishments/(?P<accomplishmentId>[^/]+)/create/$', 'alpha.views.create_accomplishment'),
   url(r'^accomplishments/(?P<accomplishmentId>[^/]+)/update/$', 'alpha.views.update_accomplishment'),
   url(r'^accomplishments/(?P<accomplishmentId>[^/]+)/$', accomplishment_resource),
   url(r'^memberships/(?P<membershipId>[^/]+)/create/$', 'alpha.views.create_membership'),
   url(r'^memberships/(?P<membershipId>[^/]+)/update/$', 'alpha.views.update_membership'),
   url(r'^memberships/(?P<membershipId>[^/]+)/$', membership_resource),
   url(r'^memberships/(?P<membershipId>[^/]+)/delete/$', 'alpha.views.delete_membership'),
   url(r'^payments/(?P<paymentId>[^/]+)/create/$', 'alpha.views.create_payment'),
   url(r'^payments/(?P<paymentId>[^/]+)/update/$', 'alpha.views.update_payment'),
   url(r'^payments/(?P<paymentId>[^/]+)/$', payment_resource),
   url(r'^studentgrind/(?P<userId>[^/]+)/edit/$', 'alpha.views.edit_page'),
   url(r'^studentgrind/(?P<userId>[^/]+)/save/$', 'alpha.views.save_page'),
   url(r'^studentgrind/(?P<userId>[^/]+)/$', 'alpha.views.view_page'),
   url(r'^studentgrind/(?P<performanceId>[^/]+)/get/$', blogpost_resource),
   url(r'^users/(?P<emailId>[^/]+)/$', user_resource),
   #url(r'^users/(?P<emailId>[^/]+)/create/$', 'studentgrind.alpha.views.create_user'),
   (r'^users/(?P<userId>\d+)/create/$', 'alpha.views.create_user'),
   url(r'^users/(?P<userId>[^/]+)/update/$', 'alpha.views.update_user'),
   url(r'^users/$', user_resource, { 'emitter_format': 'json' }),
   url(r'^verification/(?P<verificationId>[^/]+)/create/$', 'alpha.views.request_verification'),
   url(r'^verification/(?P<performanceId>[^/]+)/update/$', 'alpha.views.update_verification'),
   url(r'^verification/(?P<verificationId>[^/]+)/$', verification_resource),
   url(r'^skills/(?P<skillId>[^/]+)/create/$', 'alpha.views.create_skill'),
   url(r'^skills/(?P<skillId>[^/]+)/update/$', 'alpha.views.update_skill'),
   url(r'^skills/(?P<skillId>[^/]+)/$', skill_resource),
   url(r'^academics/(?P<academicId>[^/]+)/create/$', 'alpha.views.create_academic'),
   url(r'^academics/(?P<academicId>[^/]+)/update/$', 'alpha.views.update_academic'),
   url(r'^academics/(?P<academicId>[^/]+)/delete/$', 'alpha.views.delete_academic'),
   url(r'^academics/(?P<academicId>[^/]+)/$', academic_resource),
   url(r'^honors/(?P<honorId>[^/]+)/create/$', 'alpha.views.create_honor'),
   url(r'^honors/(?P<honorId>[^/]+)/update/$', 'alpha.views.update_honor'),
   url(r'^honors/(?P<honorId>[^/]+)/delete/$', 'alpha.views.delete_honor'),
   url(r'^honors/(?P<honorId>[^/]+)/$', honor_resource),
   url(r'^contributions/(?P<contributionId>[^/]+)/create/$', 'alpha.views.contribute_to_institution'),
   url(r'^contributions/(?P<contributionId>[^/]+)/$', contribution_resource),
   #### Views for demo purpose
   url(r'^join_studentgrind/$' , 'alpha.views.join_studentgrind'),
   url(r'^user_registration/$' , 'alpha.views.create_user'),
   url(r'^user_login/$', 'alpha.views.user_login'),
   url(r'^about_us/$', 'alpha.views.about_us'),
   url(r'^landing_page/$', 'alpha.views.landing_view'),
   url(r'^pre_landing/$','alpha.views.pre_landing'),
   url(r'^user_logout/$','alpha.views.user_logout'),
   url(r'^enterprise/add_project/$','alpha.views.add_project'),
   url(r'^enterprise/view-project/$','alpha.views.view_project'),
   url(r'^enterprise/edit-project/$','alpha.views.edit_project'),
   url(r'^enterprise/delete-project/$','alpha.views.delete_project'),
   url(r'^enterprise/upload-image/','alpha.views.upload_EnterpriseLogo'),
   url(r'^student/upload-image/','alpha.views.upload_StudentPhoto'),
   url(r'^student/submit-project/','alpha.views.submit_project'),
   url(r'^student/add_performance/','alpha.views.add_performance'),
   url(r'^student/edit_performance/','alpha.views.edit_performance'),
   url(r'^student/project/verify/','alpha.views.verify_project'),
   url(r'^student/project/assess/','alpha.views.add_assessment'),
   #url(r'^student/project/edit_assess/','alpha.views.edit_assessment'),
   url(r'^student/performance/assess/','alpha.views.add_assessment'),
   
   url(r'^student/performance/verify/','alpha.views.verify_performance'),
   url(r'^student/skill/add/','alpha.views.add_skill'),
   url(r'^student/skill/update/','alpha.views.add_skill'),
   url(r'^student/skill/verify/','alpha.views.verify_skill'),
   url(r'^student/skill/delete/','alpha.views.delete_skill'),
   url(r'^student/certification/add/','alpha.views.add_certification'),
   url(r'^student/certification/update/','alpha.views.add_certification'),
   url(r'^student/certification/verify/','alpha.views.verify_certification'),
   url(r'^student/certification/delete/','alpha.views.delete_certification'),
   url(r'^student/academic/add/','alpha.views.add_academics'),
   url(r'^student/academic/update/','alpha.views.add_academics'),
   url(r'^student/academic/verify/','alpha.views.verify_academic'),
   url(r'^student/academic/delete/','alpha.views.delete_academic'),
   url(r'^student/language/add/','alpha.views.add_language'),
   url(r'^student/language/update/','alpha.views.add_language'),
   url(r'^student/language/verify/','alpha.views.verify_language'),
   url(r'^student/language/delete/','alpha.views.delete_language'),
   url(r'^student/honor/add/','alpha.views.add_honor'),
   url(r'^student/honor/add/','alpha.views.add_honor'),
   url(r'^student/honor/verify/','alpha.views.verify_honor'),
   url(r'^student/honor/delete/','alpha.views.delete_honor'),
   url(r'^student/volunteer/add/','alpha.views.add_volunteer'),
   url(r'^student/volunteer/update/','alpha.views.add_volunteer'),
   url(r'^student/volunteer/delete/','alpha.views.delete_volunteer'),
   url(r'^student/volunteer/verify/','alpha.views.verify_volunteer'),
   url(r'^challenge/','alpha.views.challenge'),
   url(r'^talentomi/','alpha.views.talentomi'),
   url(r'^verify-view/','alpha.views.verifyview'),
   url(r'^student/save-verification/','alpha.views.save_verification'),
   url(r'^assessment/','alpha.views.assessment'),
   url(r'^assessment-view/','alpha.views.assessmentview'),
   url(r'^assessment-home/','alpha.views.assessmenthome'),
   url(r'^enterprise/create_assessment/','alpha.views.create_assessment'),
   url(r'^enterprise/edit_assessment/','alpha.views.update_assessment'),
   url(r'^enterprise/delete_assessment/','alpha.views.delete_assessment'),
   url(r'^enterprise/add_question/','alpha.views.add_question'),
   url(r'^enterprise/assessment-view/','alpha.views.view_assessment'),
   url(r'^student/assessment-view/','alpha.views.view_assessment'),
   url(r'^enterprise/import_assessment/','alpha.views.import_assessment'),
   url(r'^student/save_response/','alpha.views.save_userResponse'),
   url(r'^enterprise/delete_assessment/','alpha.views.delete_assessment'),
   url(r'^enterprise/delete_question/','alpha.views.delete_question'),
   url(r'', include('social_auth.urls')),
   url(r'^error/$', 'alpha.views.error'),
   url(r'^talent/new/$', 'alpha.views.done'),
   url(r'^accounts/profile/$', 'alpha.views.landing_view'),
   url(r'^assessment-assign-enterprise/','alpha.views.assessment_home_enterprise'),
   url(r'^assessment-assign-candidate/','alpha.views.assessment_home_candidate'),
   url(r'^assessment-assign-admin/','alpha.views.assessmenthomeadmin'),
   url(r'^get-assessment-data/','alpha.views.get_assessmentData'),
   url(r'^authorize_action/','alpha.views.authorize_verifications'),
   url(r'^howitworks/','alpha.views.howitworks'),
   url(r'^home/', 'alpha.views.home_redirect'),
   url(r'^contact-us/', 'alpha.views.contact_us'),
   url(r'^forgot-password/', 'alpha.views.forgot_password'),
   url(r'^reset-password/', 'alpha.views.reset_password'),
   #url(r'^$','linkedin.views.home'),

#url(r'^instAlumni/$', 'alpha.views.instAlumni'),
)
