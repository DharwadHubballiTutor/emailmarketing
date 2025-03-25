from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SubscriberForm, EmailCampaignForm, CampaignLogForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
        return render(request, 'dashboard.html')

def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return redirect('home')


class SubscriberListView(ListView):
            model = Subscriber
            template_name = 'subscriber_list.html'
            context_object_name = 'subscribers'


class SubscriberCreateView(CreateView):
            model = Subscriber
            form_class = SubscriberForm
            template_name = 'subscriber_form.html'
            success_url = reverse_lazy('subscriber_list')


class SubscriberUpdateView(UpdateView):
            model = Subscriber
            form_class = SubscriberForm
            template_name = 'subscriber_form.html'
            success_url = reverse_lazy('subscriber_list')


class SubscriberDeleteView(DeleteView):
            model = Subscriber
            template_name = 'subscriber_confirm_delete.html'
            success_url = reverse_lazy('subscriber_list')


class EmailCampaignListView(ListView):
            model = EmailCampaign
            template_name = 'emailcampaign_list.html'
            context_object_name = 'campaigns'


class EmailCampaignCreateView(CreateView):
            model = EmailCampaign
            form_class = EmailCampaignForm
            template_name = 'emailcampaign_form.html'
            success_url = reverse_lazy('campaign_list')


class EmailCampaignUpdateView(UpdateView):
            model = EmailCampaign
            form_class = EmailCampaignForm
            template_name = 'emailcampaign_form.html'
            success_url = reverse_lazy('emailcampaign_list')


class EmailCampaignDeleteView(DeleteView):
            model = EmailCampaign
            template_name = 'emailcampaign_confirm_delete.html'
            success_url = reverse_lazy('emailcampaign_list')


class CampaignLogListView(ListView):
            model = CampaignLog
            template_name = 'campaignlog_list.html'
            context_object_name = 'logs'


class CampaignLogCreateView(CreateView):
            model = CampaignLog
            form_class = CampaignLogForm
            template_name = 'campaignlog_form.html'
            success_url = reverse_lazy('campaignlog_list')


class CampaignLogUpdateView(UpdateView):
            model = CampaignLog
            form_class = CampaignLogForm
            template_name = 'campaignlog_form.html'
            success_url = reverse_lazy('campaignlog_list')


class CampaignLogDeleteView(DeleteView):
            model = CampaignLog
            template_name = 'campaignlog_confirm_delete.html'
            success_url = reverse_lazy('campaignlog_list')