# Basic Application of CRUD with DJANGO and SQLite3
Currently without styling for focusing on the implementations

## Notes:
--The form is inheriting forms.ModelForm for seamless integration with the currently selected model by declaring the:
class Meta:
	model = myModel

	fields = [
		"column_fields",
	] 

--Validators are also used for determining the minimum and maximum value or length of specific fields:
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

age = models.IntegerField(
        validators=[
            MinValueValidator(17),
            MaxValueValidator(25)
        ]
    )

