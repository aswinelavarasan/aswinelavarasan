class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, mobile_number, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email   = self.normalize_email(email)
        mobile_number   = mobile_number
        user    = self.model(email=email, mobile_number= mobile_number **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, mobile_number, password, **extra_fields)

    def create_superuser(self, email, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, mobile_number, password, **extra_fields)
#123

class User(AbstractUser):
    username    = None
    email       = models.EmailField(_('email address'), unique=True, validators= [validate_email])
    mobile_number   = models.CharField(_("mobile number"), max_length=11, unique = True, validators= [validate_mobile_number])

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)