from django.urls import path
from .views import *

urlpatterns = [
    path('creation/', UserCreation, name='creation'),
    path('login/', UserLogin, name='login'),
    path('account/<int:id>/', UserAccount, name='account'),
    path('edit/', UserEdit, name='edit'),
    path('logout/', Custom_Logout, name='logout'),
    path('accounts/', UsersAccounts, name='usersaccounts'),
    path('person/<int:id>/', UserPerson, name='userperson'),
    path('message/<int:id>/', SendMessage, name='usermessage'),
    path('messagesin/<int:id>/', MessagesIn, name='messagesin'),
    path('dialogue/<int:id>/', Dialogue, name='dialogue'),
    path('searchinfo/<int:id>/', SearchInfo, name='searchinfo'),
    path('delete_image/<int:id>/', DeleteImage, name='delete_image'),
    path('delete_video/<int:id>/', DeleteVideo, name='delete_video'),
]
