from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class CustomManager(BaseUserManager):

    use_in_migrations=True

    def create_user(self,email,password=None,**extra_fields):
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self.db)

        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)

        return self.create_user(email,password,**extra_fields)