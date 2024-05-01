from django.urls import path
from .import views


urlpatterns = [
    # auth
    path("m/login", views.member_login, name="mlogin"),
    path("l/login", views.leader_login, name="llogin"),
    path("m/register", views.member_register, name="mregister"),
    path("l/register", views.leader_register, name="lregister"),
    path('logout', views.logout_view, name='logout'),
    #  profiles
    path('member/profile', views.member_profile, name='member_profile'),
    path('leader/profile', views.leader_profile, name='leader_profile'),
    # create
    path('create/club/', views.create_club, name='create_club'),
    path('create/event/<int:club_id>/', views.create_event, name='create_event'),
    path('create/announcement/<int:club_id>/', views.create_announcement, name='create_announcement'),
    path('create/discussion/<int:club_id>/', views.create_discussion, name='create_discussion'),
    path('create/topic/<int:discussion_id>/', views.create_topic, name='create_topic'),
    path('create/comment/<int:topic_id>/', views.create_comment, name='create_comment'),
    # edit
    path('edit/club/<int:club_id>/', views.edit_club, name='edit_club'),
    path('edit/event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('edit/announcement/<int:announcement_id>/', views.edit_announcement, name='edit_announcement'),
    path('edit/topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    path('edit/comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    # delete
    path('delete/club/', views.delete_club, name='delete_club'),
    path('delete/event/', views.delete_event, name='delete_event'),
    path('delete/announcement/', views.delete_announcement, name='delete_announcement'),
    path('delete/discussion/', views.delete_discussion, name='delete_discussion'),
    path('delete/topic/', views.delete_topic, name='delete_topic'),
    path('delete/comment/', views.delete_comment, name='delete_comment'),
    # list
    path('list/clubs/', views.list_clubs, name='list_clubs'),
    path('list/events/<int:club_id>/', views.list_events, name='list_events'),
    path('list/announcements/<int:club_id>/', views.list_announcements, name='list_announcements'),
    path('list/discussions/<int:club_id>/', views.list_discussions, name='list_discussions'),
    path('list/topics/<int:discussion_id>/', views.list_topics, name='list_topics'),
    path('list/comments/<int:topic_id>/', views.list_comments, name='list_comments'),
    # detail
    path('detail/club/<int:club_id>/', views.detail_club, name='detail_club'),
    path('detail/event/<int:event_id>/', views.detail_event, name='detail_event'),
    path('detail/announcement/<int:announcement_id>/', views.detail_announcement, name='detail_announcement'),
    path('detail/discussion/<int:discussion_id>/', views.detail_discussion, name='detail_discussion'),
    path('detail/topic/<int:topic_id>/', views.detail_topic, name='detail_topic'),
    path('detail/comment/<int:comment_id>/', views.detail_comment, name='detail_comment'),
    # success
    path('success/', views.success, name='success_url'),
    # error
    path('error/', views.error, name='error_url'),

    
]
