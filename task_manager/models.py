import os
import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

URGENCY_CHOICES = (
    (0, "minor"),
    (1, "medium",),
    (2, "major",),
    (3, "critical")
)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    registration_number = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TypeOfWork(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, default="", )
    position = models.ForeignKey(
        "Position",
        on_delete=models.CASCADE,
        null=True,
    )
    avatar = models.ImageField(null=True)

    @property
    def completed_tasks(self):
        return self.tasks.filter(is_completed=True).count()

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, "url"):
            return self.avatar.url

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def get_absolute_url(self):
        return reverse("task_manager:employee-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    type_of_work = models.ForeignKey("TypeOfWork", on_delete=models.CASCADE)
    description = models.TextField()
    urgency = models.IntegerField(choices=URGENCY_CHOICES, default=1)
    price = models.FloatField()
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    employees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"Project: {self.project}, {self.type_of_work}"
