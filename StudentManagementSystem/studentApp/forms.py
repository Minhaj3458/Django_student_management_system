from django import forms
from .import models

class ahturregform(forms.ModelForm):
    class Meta:
        model = models.Authorregiss
        fields = "__all__"

class formstupage(forms.ModelForm):
    class Meta:
        model = models.Addstupage
        fields = "__all__"

class formregstu(forms.ModelForm):
    class Meta:
        model = models.Studentregi
        fields = "__all__"

class formregtea(forms.ModelForm):
    class Meta:
        model = models.Teacherreg
        fields = "__all__"

class Applyonline(forms.ModelForm):
    class Meta:
        model = models.Online_Apply
        fields = "__all__"

class AddTeachform(forms.ModelForm):
    class Meta:
        model = models.AddTeacherpage
        fields = "__all__"

class AddCourseform(forms.ModelForm):
    class Meta:
        model = models.AddCourse
        fields = "__all__"

class AddstuResultform(forms.ModelForm):
    class Meta:
        model = models.AddstuResult
        fields = "__all__"