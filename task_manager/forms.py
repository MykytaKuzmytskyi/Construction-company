import os
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from task_manager.models import Employee, Task, Project


class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "position",
        )


class EmployeeUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(
        required=True,
        validators=[
            MaxLengthValidator(13),
            MinLengthValidator(13),
        ]
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if phone_number[0] != "+":
            raise ValidationError(
                "The number must start with '+' (+380) "
            )
        if not phone_number[1:].isdigit():
            raise ValidationError(
                "All characters except the first must be digits"
            )
        return phone_number

    class Meta:
        model = Employee
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "avatar",
        ]

    @receiver(pre_save)
    def pre_save_image(sender, instance, *args, **kwargs):
        """ instance old image file will delete from os """
        try:
            old_avatar = instance.__class__.objects.get(
                id=instance.id
            ).avatar.path
            try:
                new_avatar = instance.image.path
            except:
                new_avatar = None
            if new_avatar != old_avatar:
                if os.path.exists(old_avatar):
                    os.remove(old_avatar)
        except:
            pass


class EmployeesSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by last name"})
    )


class ProjectsCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "registration_number",
            "address",
        )


class ProjectsSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class TaskForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = (
            "project",
            "type_of_work",
            "description",
            "urgency",
            "price",
            "employees",
        )


class TaskSearchForm(forms.Form):
    project = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by project"})
    )
