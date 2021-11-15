from .models import *


class DataMixin:
    def get_user_context(self, context):
        users = User.objects.all()
        context['users'] = users
        return context
