from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore
import datetime
from django.core.mail import send_mail
from .models import Subscriber, EmailCampaign
from django.conf import settings

def my_scheduled_task():
    subscribers = Subscriber.objects.all()
    now = datetime.datetime.now()
    one_minute_ago = now - datetime.timedelta(minutes=1)
    campaigns = EmailCampaign.objects.filter(sent=False, scheduled_at__gte=one_minute_ago, scheduled_at__lt=now)

    for campaign in campaigns:
        for subscriber in subscribers:
            send_mail(
                subject=campaign.title,
                message=campaign.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )
        campaign.sent = True
        campaign.save()

    print(f"Emails sent at {datetime.datetime.now()}")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        my_scheduled_task,
        trigger=IntervalTrigger(seconds=1),  # Runs every 1
        id="my_task",
        replace_existing=True,
    )

    scheduler.start()
    print("Scheduler started...")
