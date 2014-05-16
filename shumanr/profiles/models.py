from django.db import models

class ProfileManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)
    
class Profile(models.Model):
    username = models.CharField(max_length=128)

    #last_login = models.DateTimeField(blank=True, null=True)
    objects = ProfileManager()

    def is_authenticated(self):
        return True
