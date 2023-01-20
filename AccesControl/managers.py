from django.contrib.auth.models import BaseUserManager

class UserPManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("El usuario debe tener Nombre")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields
            )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user =self.create_user(
            username, 
            email, 
            password, 
            **extra_fields
            )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user