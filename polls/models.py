from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# polls
class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

# Choice 
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='Choices')
    choice_text = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.choice_text
    pass

# Vote 
class Vote(models.Model):
    Choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='Votes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")
    
