from django.contrib import admin
from main.models import Interest, University, UserProfile
from main.models import Lunch, Feedback, TimeInterval, Message
                        
						
# Register your models here.

admin.site.register(Interest)
admin.site.register(University)
admin.site.register(UserProfile)
admin.site.register(Lunch)
admin.site.register(Feedback)
admin.site.register(TimeInterval)
admin.site.register(Message)