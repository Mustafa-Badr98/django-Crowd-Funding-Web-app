from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^01[0-9]{9}$',
    message='Phone number must start with 01 and consist of 11 digits.',
)
