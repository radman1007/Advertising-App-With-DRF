from django.shortcuts import render
from rest_framework.views import APIView
from .models import Ad


class AdListView(APIView):
    def get(self, request):
        queryset = Ad.objects.filter(is_publish=True)