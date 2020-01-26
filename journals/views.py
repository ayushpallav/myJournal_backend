from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from journals.forms import UserForm,UserProfileInfoForm
from journals.serializers import ProfileSerializer, JournalEntrySerializer
from journals.models import Profile, Journal, Entry


class ProfileView(LoginRequiredMixin, ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__username=self.request.user)
        return qs


class JournalEntryView(LoginRequiredMixin, CreateAPIView):
    serializer_class = JournalEntrySerializer

    def get_serializer_context(self):
        return {'user': self.request.user.username}

    def post(self, request, **kwargs):
        super().post(request, kwargs)
        return HttpResponseRedirect(reverse('index'))


def index(request):
    journal = Journal.objects.filter(profile__user__username=request.user.username).first()
    entry = Entry.objects.filter(journal=journal, date=str(datetime.now().date())).first()
    return render(
        request,'index.html',
        {
            'entry': entry
        }
    )


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            # Create a new profile
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('profile pic present')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            # Create a new journal for the new registered user
            Journal.objects.create(profile=profile)
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
