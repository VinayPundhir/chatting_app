from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("all_users/", views.all_users, name="all_users"),
    path("friends/", views.friends, name="friends"),
    path("requests/", views.requests, name="requests"),
    path("accept_request/<str:name>/", views.accept_request, name="accept_request"),
    path("decline_request/<str:name>/", views.decline_request, name="decline_request"),
    path("", views.start, name="start"),
    path("chat_size/<str:name>/", views.chat_size, name="chat_size"),
    path("video_call/<str:name>/", views.video_call, name="video_call"),
    path(
        "public/",
        TemplateView.as_view(template_name="public_profile.html"),
        name="public_profile",
    ),
    path("logout/", views.logout, name="logout"),
    path("json/<str:name>/", views.json, name="json"),
    path("sinup/", TemplateView.as_view(template_name="sinup.html"), name="sinup"),
    path("sinup_process/", views.sinup_process, name="sinup_process"),
    path("process/", views.process, name="process"),
    path("process_recieved/", views.process_recieved, name="process_recieved"),
    path("login_process/", views.login_process, name="login_process"),
    path("send_request/<str:name>/", views.send_request, name="send_request"),
    path("chatting/<str:name>/", views.chatting, name="chatting"),
    path(
        "chatting_process/<str:name>",
        views.chatting_process,
        name="chatting_process",
    ),
]

# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
