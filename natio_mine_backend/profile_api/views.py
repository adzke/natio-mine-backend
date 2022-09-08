from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .miner import Miner


           

class GainExperience(APIView):
    
    def post(self, request, *args, **kwargs):
        miner = Miner()
        user_profile = request.user.profile
        profile = Profile.objects.get(id=user_profile.id)
        if(user_profile.operation_in_progress == False):
            operation_data = {"operation_in_progress": True, "experience": user_profile.experience}
            serializer = ProfileSerializer(profile, data=operation_data)
            if serializer.is_valid():
               serializer.save()
            data = {"operation_in_progress": False, "experience": miner.calculate_experience(profile)}
            serializer = ProfileSerializer(profile, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(data={"Operation in Progress"}, status=status.HTTP_400_BAD_REQUEST)
        




