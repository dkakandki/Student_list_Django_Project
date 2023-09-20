from django import forms
from .models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
    # name = forms.CharField(max_length=100)
    # roll_num = forms.IntegerField()
    # city = forms.CharField(max_length=100)
    # marks = forms.IntegerField(