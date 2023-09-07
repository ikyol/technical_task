from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def _create(self, *, email: str, password: str, **extra_fields) -> AbstractBaseUser:
        if not email or not password:
            raise ValueError("Email or password cannot be empty")
        from loguru import logger
        logger.info(f"fields {extra_fields}")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, *, email: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields["is_active"] = False
        extra_fields["is_staff"] = False
        return self._create(email=email, password=password, **extra_fields)

    def create_superuser(self, *, email: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields["is_active"] = True
        extra_fields["is_staff"] = True
        return self._create(email=email, password=password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def has_module_perms(self, app_label) -> models.BooleanField:
        return self.is_staff

    def has_perm(self, obj) -> models.BooleanField:
        return self.is_staff

    class Meta:
        app_label = "account"
