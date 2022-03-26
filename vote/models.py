from django.db import models

# Create your models here.
class Vote(models.Model):
    question = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)


    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count



