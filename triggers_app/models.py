from django.db import models

from triggers_app.choices import StateChoices, EnvironmentChoices


class Trigger(models.Model):
    identifier = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=True, default=None)
    state = models.CharField(max_length=100, choices=StateChoices.choices, default=StateChoices.DISABLED)
    is_active = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_data = models.JSONField(null=True)
    environment = models.CharField(max_length=100, choices=EnvironmentChoices.choices, default=EnvironmentChoices.GLOBAL)
