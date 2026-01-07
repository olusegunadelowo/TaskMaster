from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True , null=True)
    done = models.BooleanField(default=False)
    
    @property
    def is_expired(self):
        local_now = datetime.now().astimezone
        print(local_now,self.end_time)
        if self.end_time and self.end_time < local_now:
            return True
        return False