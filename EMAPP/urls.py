from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('subscribers/', views.SubscriberListView.as_view(), name='subscriber_list'),
    path('subscriber/add/', views.SubscriberCreateView.as_view(), name='subscriber_add'),
    path('subscriber/<int:pk>/update/', views.SubscriberUpdateView.as_view(), name='subscriber_update'),
    path('subscriber/<int:pk>/delete/', views.SubscriberDeleteView.as_view(), name='subscriber_delete'),
    path('campaigns/', views.EmailCampaignListView.as_view(), name='campaign_list'),
    path('campaign/add/', views.EmailCampaignCreateView.as_view(), name='campaign_add'),
    path('campaign/<int:pk>/update/', views.EmailCampaignUpdateView.as_view(), name='campaign_update'),
    path('campaign/<int:pk>/delete/', views.EmailCampaignDeleteView.as_view(), name='campaign_delete'),
    # path('campaign/<int:pk>/send/', views.send_campaign, name='send_campaign'),
    # path('campaign/<int:pk>/logs/', views.CampaignLogListView.as_view(), name='campaign_logs'),
    path('dashboard/', views.dashboard, name='dashboard'),
]