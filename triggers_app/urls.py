from django.urls import path, include

from triggers_app.views import TriggerView, TriggerDetailView

urlpatterns = [
    path("trigger/", TriggerView.as_view(), name="trigger"),
    path('trigger/<str:identifier>/', TriggerDetailView.as_view(), name="trigger_details"),
]
