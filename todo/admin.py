from django.contrib import admin
from .models import Task  # Ensure the correct model name is imported

admin.site.register(Task)  # Register Task model in admin


