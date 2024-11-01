from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']

from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']

# from django import forms
# from .models import Marks
from .models import Marks

class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields=['student','course','marks']

# faculty/forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }


