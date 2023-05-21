from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import random

class CheckingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        r1 = random.randint(0, 1000)

        return Response({"data":r1})


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client