from client.models import CustomUser
from django.db import models


class Task(models.Model):
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    done = models.BooleanField(default=False)

    def checked(self):
        self.done = True
        self.save()

#dfdsdfd
    def unchecked(self):
        self.done = False
        self.save()
