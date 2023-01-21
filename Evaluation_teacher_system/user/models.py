from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from Evaluation_teacher_system.college.models import College


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, collage_id=None):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        college = College.objects.get(id=collage_id)
        user = self.model(username=username, email=self.normalize_email(email), college=college)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = 'user'
