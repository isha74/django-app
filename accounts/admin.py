#used to make a model appear in the Django Admin panel.
# connects profile database model to django admin interface.

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
