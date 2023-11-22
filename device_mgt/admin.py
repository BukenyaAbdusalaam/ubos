from django.contrib import admin
from .models import Gadget, AccessControl, AccessLog, User

admin.site.register(Gadget)
admin.site.register(AccessControl)
admin.site.register(AccessLog)
admin.site.register(User)
