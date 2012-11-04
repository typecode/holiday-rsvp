from django.db import models

# Create your models here.

class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_date = models.DateField('date published')

  def was_published_recently(self):
    import datetime
    from django.utils import timezone
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  def __unicode__(self):
    return self.question

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField()

  def __unicode__(self):
    return self.choice_text
