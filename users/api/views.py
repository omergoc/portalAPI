from users.api.serializers import ChangePasswordSerializer
from users.models import Account
from rest_framework.generics import  get_object_or_404, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserSerializer,AccountUpdateSerializer
from rest_framework.views import APIView
from rest_framework import status


class AccountView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = Account.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id = self.request.user.id)
        return obj


class AccountUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountUpdateSerializer

    def put(self, request):
        serializer = AccountUpdateSerializer(self.request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePassowrdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            'old_password': request.data['old_password'],
            'new_password': request.data['new_password']
        }
        serializer = ChangePasswordSerializer(data = data)

        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({'old_password':'wrong_password'}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)