from django.core.exceptions import ValidationError

# Create your models here.
def validate_content(value):
	content=value
	if content=="abc":
		raise ValidationError("Contents cannot be abc")
	return value
def	validate_content1(value):
	content=value
	if content=="123":
		raise ValidationError("Contents cannot be 123")
	return value