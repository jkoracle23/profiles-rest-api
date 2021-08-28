from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name) # it creates a new model that the user manager is representing so by default self dot model is set to the model that the manager is for and then it will create a new model object and set the email and the name
        user.set_password(password)#we can't just pass the password in here as a clear text value we need to use the set password function that comes with our user model so it's part of the abstract base user and we set this by doing user dot set password password and pass it in like that the reason we do that is so the password is encrypted we want to make sure the password is converted to a hash and never stored as plain text in the database because this way if somebody should manage to hack the database and retrieve all the users they would only be able to see the hashed passwords which means they wouldn't be able to convert that password to a clear text password and then potentially use that to log into the users other services if they used the same password for Facebook or another website for example They could technically reverse-engineer it eventually if they'd given it enough time so it doesn't mean you don't have to protect your database but it's the best practice for storing any sensitive data in the database is to encrypt it and by default Django does this with the set password function
        user.save(using=self._db)#specify the db that you want to use. django supports mulitple db
        return user #returns the created users


    def create_superuser(self, email,name,password):
        """create and save new super user with given details """
        user=self.create_user(email, name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):# note s in PermissionsMixin
    """Database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email' #we need to specify a username field and this is because we're overriding the default username field which is normally called user name and we're replacing it
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return represenation of our user"""
        return self.email
