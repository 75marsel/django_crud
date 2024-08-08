from django import forms
from .models import Student

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = Student
        
        fields = [
            "first_name",
            "last_name",
            "age",
            "course",
            "email",
            "cover_letter",    
        ]