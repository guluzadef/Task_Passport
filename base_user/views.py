from rest_framework.response import Response
from rest_framework import permissions, exceptions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from .serializer import *

User = get_user_model()


class UserRegistrationApi(CreateAPIView):  # POST
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            user_data = serializer.data.copy()
            team_data = user_data.pop('team')
            password = user_data.pop('password')
            team, _ = Team.objects.get_or_create(**team_data)
            user = User(**user_data)
            user.team = team
            try:
                user.set_password(password)
                user.is_task_manager = True
                user.save()
                response = self.get_serializer(instance=user)
                return Response(response.data, status=status.HTTP_201_CREATED)
            except:
                return Response({
                    "message": "Bele user artiq movcuddur"
                }, status=status.HTTP_409_CONFLICT)
        else:
            return Response({
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=200)
        return Response(status=401)


class UserListApi(APIView):  # GET
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        users = MyUser.objects.all()
        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


