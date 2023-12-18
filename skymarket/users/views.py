# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer, UserRegistrationSerializer
#
#
# class UserProfileView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user
#
#
# class UpdateUserProfileView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user
#
#     def perform_update(self, serializer):
#         serializer.save()
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class UserRegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegistrationSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             user = User(**serializer.validated_data)
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#
#             return Response({"user": user.email, "message": "User created successfully"},
#                             status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
