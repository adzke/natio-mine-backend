from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
import time
from rest_framework.views import APIView

class GainExperience(APIView):

        
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=request.user.profile.id)
        print("here is experience")
        data = {"experience": profile.experience + 20}
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


