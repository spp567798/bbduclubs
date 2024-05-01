from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MemberProfileForm, LeaderProfileForm
from .forms import ClubForm, EventForm, AnnouncementForm, DiscussionForm, TopicForm, CommentForm
from .models import Club, Event, Announcement, Discussion, Topic, Comment
from .models import MemberProfile, LeaderProfile
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def leader_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('llogin')
            else:
                # if user is a member
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    request.session['group'] = group
                    messages.success(request, 'Welcome, ' + user.username)
                    return redirect('leader_dashboard')
                else:
                    messages.error(request, 'You are not a leader')
                    return redirect('llogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/leader/login.html')

def member_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group') 
        print(group, username, password)
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('mlogin')
            else:
                # if member is a leader
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    request.session['group'] = group
                    return redirect('member_dashboard')
                else:
                    messages.error(request, 'You are a leader')
                    return redirect('mlogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/member/login.html')
    
def leader_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('lregister')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/leader/register.html')
def member_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('mregister')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/member/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def member_profile(request):
    form = MemberProfileForm()
    profile = MemberProfile.objects.filter(user=request.user).first()
    if profile:
        form = MemberProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = MemberProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('member_profile')
    ctx = {
        'form': form
    }
    return render(request, 'accounts/member/profile.html', ctx)

@login_required
def leader_profile(request):
    form = LeaderProfileForm()
    profile = LeaderProfile.objects.filter(user=request.user).first()
    if profile:
        form = LeaderProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = LeaderProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('leader_profile')
    ctx = {
        'form': form
    }
    return render(request, 'accounts/leader/profile.html', ctx)

@login_required
def create_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL
    else:
        form = ClubForm()
    return render(request, 'create_club.html', {'form': form})

@login_required
def create_event(request, club_id):
    club = Club.objects.get(id=club_id)
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            model =  form.save(commit=False)
            model.club = club
            model.save()
            messages.success(request, 'Event created successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form,
        'club': club
    }
    return render(request, 'create_event.html', ctx)

@login_required
def create_announcement(request, club_id):
    club = Club.objects.get(id=club_id)
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            model =  form.save(commit=False)
            model.club = club
            model.save()
            messages.success(request, 'Announcement created successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form,
        'club': club
    }
    return render(request, 'create_announcement.html', ctx)

@login_required
def create_discussion(request, club_id):
    club = Club.objects.get(id=club_id)
    form = DiscussionForm()
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            model =  form.save(commit=False)
            model.club = club
            model.save()
            messages.success(request, 'Discussion created successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form,
        'club': club
    }
    return render(request, 'create_discussion.html', ctx)

@login_required
def create_topic(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            model =  form.save(commit=False)
            model.discussion = discussion
            model.save()
            messages.success(request, 'Topic created successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form,
        'discussion': discussion
    }
    return render(request, 'create_topic.html', ctx)

@login_required
def create_comment(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            model =  form.save(commit=False)
            model.topic = topic
            model.save()
            messages.success(request, 'Comment created successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form,
        'topic': topic
    }
    return render(request, 'create_comment.html', ctx)

# edit views
@login_required
def edit_club(request, club_id):
    club = Club.objects.get(id=club_id)
    form = ClubForm(instance=club)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            messages.success(request, 'Club updated successfully')
            return redirect('success_url')  # Redirect to a success URL
    ctx = {
        'form': form
    }
    return render(request, 'edit_club.html', ctx)

@login_required
def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('success_url')
    ctx = {
        'form': form
    }
    return render(request, 'edit_event.html', ctx)

@login_required
def edit_announcement(request, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    form = AnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement updated successfully')
            return redirect('success_url')
    ctx = {
        'form': form
    }
    return render(request, 'edit_announcement.html', ctx)

@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Topic updated successfully')
            return redirect('success_url')
    ctx = {
        'form': form
    }
    return render(request, 'edit_topic.html', ctx)

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully')
            return redirect('success_url')
    ctx = {
        'form': form
    }
    return render(request, 'edit_comment.html', ctx)

# delete views
@login_required
def delete_club(request):
    if request.method == 'POST':
        club_id = request.POST.get('club_id')
        club = Club.objects.get(id=club_id)
        club.delete()
        messages.success(request, 'Club deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

@login_required
def delete_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(id=event_id)
        event.delete()
        messages.success(request, 'Event deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

@login_required
def delete_announcement(request):
    if request.method == 'POST':
        announcement_id = request.POST.get('announcement_id')
        announcement = Announcement.objects.get(id=announcement_id)
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

@login_required
def delete_discussion(request):
    if request.method == 'POST':
        discussion_id = request.POST.get('discussion_id')
        discussion = Discussion.objects.get(id=discussion_id)
        discussion.delete()
        messages.success(request, 'Discussion deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

@login_required
def delete_topic(request):
    if request.method == 'POST':
        topic_id = request.POST.get('topic_id')
        topic = Topic.objects.get(id=topic_id)
        topic.delete()
        messages.success(request, 'Topic deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

@login_required
def delete_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        messages.success(request, 'Comment deleted successfully')
        return redirect('success_url')
    return redirect('error_url')

# list views
@login_required
def list_clubs(request):
    clubs = Club.objects.all()
    ctx = {
        'clubs': clubs
    }
    return render(request, 'list_clubs.html', ctx)

@login_required
def list_events(request, club_id):
    club = Club.objects.get(id=club_id)
    events = Event.objects.filter(club=club)
    ctx = {
        'events': events,
        'club': club
    }
    return render(request, 'list_events.html', ctx)

@login_required
def list_announcements(request, club_id):
    club = Club.objects.get(id=club_id)
    announcements = Announcement.objects.filter(club=club)
    ctx = {
        'announcements': announcements,
        'club': club
    }
    return render(request, 'list_announcements.html', ctx)

@login_required
def list_discussions(request, club_id):
    club = Club.objects.get(id=club_id)
    discussions = Discussion.objects.filter(club=club)
    ctx = {
        'discussions': discussions,
        'club': club
    }
    return render(request, 'list_discussions.html', ctx)

@login_required
def list_topics(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    topics = Topic.objects.filter(discussion=discussion)
    ctx = {
        'topics': topics,
        'discussion': discussion
    }
    return render(request, 'list_topics.html', ctx)

@login_required
def list_comments(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = Comment.objects.filter(topic=topic)
    ctx = {
        'comments': comments,
        'topic': topic
    }
    return render(request, 'list_comments.html', ctx)

# detail views
@login_required
def detail_club(request, club_id):
    club = Club.objects.get(id=club_id)
    ctx = {
        'club': club
    }
    return render(request, 'detail_club.html', ctx)

@login_required
def detail_event(request, event_id):
    event = Event.objects.get(id=event_id)
    ctx = {
        'event': event
    }
    return render(request, 'detail_event.html', ctx)

@login_required
def detail_announcement(request, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    ctx = {
        'announcement': announcement
    }
    return render(request, 'detail_announcement.html', ctx)

@login_required
def detail_discussion(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    ctx = {
        'discussion': discussion
    }
    return render(request, 'detail_discussion.html', ctx)

@login_required
def detail_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    ctx = {
        'topic': topic
    }
    return render(request, 'detail_topic.html', ctx)

@login_required
def detail_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    ctx = {
        'comment': comment
    }
    return render(request, 'detail_comment.html', ctx)

# success and error views
def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')
