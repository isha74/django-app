# create app named as account . this app.py tells info about your app like name setting or what to do when it loads.

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
