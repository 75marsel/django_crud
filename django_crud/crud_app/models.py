from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(
        validators=[
            MinValueValidator(17),
            MaxValueValidator(25)
        ]
    )
    course = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cover_letter = models.TextField(
        max_length=200,
        validators=[
            MinLengthValidator(100),
        ]
    )
    
    def __str__(self):
        return f"""
        Firt Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        course: {self.course}
        Email: {self.email}
        Cover Letter: {self.cover_letter}
        """