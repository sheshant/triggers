from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from triggers_app.models import Trigger
from triggers_app.serializer import TriggerDetailsSerializer


# Create your views here.

class TriggerView(ListCreateAPIView):
    serializer_class = TriggerDetailsSerializer
    queryset = Trigger.objects.all()
    permission_classes = IsAuthenticated,
    pagination_class = PageNumberPagination


class TriggerDetailView(RetrieveUpdateAPIView):
    serializer_class = TriggerDetailsSerializer
    lookup_field = "identifier"
    queryset = Trigger.objects.all()
    permission_classes = IsAuthenticated,
    pagination_class = PageNumberPagination

