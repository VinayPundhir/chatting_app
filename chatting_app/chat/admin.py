from chat.models import (
    Active,
    Channel,
    ChatData,
    Friend,
    FriendRequest,
    MessageTracker,
    UserData,
)
from django.contrib import admin

# Register your models here.

admin.site.register(UserData)
admin.site.register(FriendRequest)
admin.site.register(Friend)
admin.site.register(ChatData)
admin.site.register(MessageTracker)
admin.site.register(Active)
admin.site.register(Channel)
