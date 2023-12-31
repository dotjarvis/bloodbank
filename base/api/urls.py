from django.urls import path

from .views import LoginAPIView, GoogleLogin, FacebookLogin, TwitterLogin, ResetUserPasswordView, HomePageAPIView, UserDetailsAPIView, DonorHomeAPIView, DonationCriteriaAPIView, QuestionsAPIView, DonationAgreement, HospitalAddresses, ProfileAPIView, RequestBloodAPIView, NotificationsAPIView

from knox import views as knox_views

urlpatterns = [

    path('auth/login/', LoginAPIView.as_view(), name='knox_login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(),
         name='knox_logoutall'),

    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),

    path('reset_password_confirm/<str:uid>/<str:token>/',
         ResetUserPasswordView.as_view(),
         name='reset_user_password'),

    path('home/', HomePageAPIView.as_view(), name='home'),

    path('profile-details/', UserDetailsAPIView.as_view(),
         name='user_details'),


    path('donor-home/', DonorHomeAPIView.as_view(), name='donor_home'),
    path('donation-criteria/', DonationCriteriaAPIView.as_view(),
         name='donation_criteria'),
    path('questions/', QuestionsAPIView.as_view(),
         name='criteria_quizes'),
    path('questions/<int:question_id>/', QuestionsAPIView.as_view(),
         name='criteria_quizes'),


    path('donation-agreement/', DonationAgreement.as_view(),
         name='donation_agreement'),
    path('hospital-address/', HospitalAddresses.as_view(),
         name='hospital_address'),


    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('request-blood/', RequestBloodAPIView.as_view(),
         name='request_blood'),

    path('notifications/', NotificationsAPIView.as_view(),
         name='notifications'),
]
