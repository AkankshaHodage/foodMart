from django.db import models
from accounts.models import User,UserProfile

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User,related_name='user', on_delete=models.CASCADE)#The major benefit from using the cascade control is that disturbances arising within the secondary loop are corrected by the secondary controller before affecting the value of the primary controlled output.
    user_profile = models.OneToOneField(UserProfile,related_name='userprofile',on_delete=models.CASCADE)# it's use for when user is deleted the user profile have to deleted for that this "OneToOneField " is used
    restaurant_name =models.CharField(max_length=50)
    restaurant_license=models.ImageField(upload_to ='media/restaurant/license')
    is_approved= models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.restaurant_name