from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class EmailCampaign(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CampaignLog(models.Model):
    campaign = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE, related_name='logs')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='logs')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('SENT', 'Sent'), ('FAILED', 'Failed')])

    def __str__(self):
        return f"{self.campaign.title} - {self.subscriber.email} - {self.status}"