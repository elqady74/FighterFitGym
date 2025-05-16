<<<<<<< HEAD
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect  # أضفنا ده عشان نعمل Redirect
from .models import GymUser, Trainer
from .serializers import UserSerializer, TrainerSerializer

class SignupView(APIView):
    def get(self, request):
        # لو حد دخل على /api/signup/ بطلب GET، هنعمل Redirect لصفحة التسجيل
        return HttpResponseRedirect('/signup/')

    def post(self, request):
        data = request.data
        role = data.get('role')
        
        # Create user
        user_data = {
            'fname': data.get('fname'),
            'lname': data.get('lname'),
            'email': data.get('email'),
            'password_hash': make_password(data.get('password')),
            'phone': data.get('phone'),
            'role': role,
            'height': data.get('height') if role == 'trainee' else None,
            'weight': data.get('weight') if role == 'trainee' else None,
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            
            # If trainer, create record in TRAINER table
            if role == 'trainer':
                trainer_data = {
                    'trainer_id': user.user_id,
                    'specialization': data.get('specialization'),
                    'certification': data.get('certification'),
                }
                trainer_serializer = TrainerSerializer(data=trainer_data)
                if trainer_serializer.is_valid():
                    trainer_serializer.save()
                else:
                    return Response(trainer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = GymUser.objects.get(email=email)
            if check_password(password, user.password_hash):
                return Response({
                    'message': 'Login successful',
                    'user_id': user.user_id,
                    'fname': user.fname,
                    'lname': user.lname,
                    'role': user.role
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except GymUser.DoesNotExist:
=======
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect  # أضفنا ده عشان نعمل Redirect
from .models import GymUser, Trainer
from .serializers import UserSerializer, TrainerSerializer

class SignupView(APIView):
    def get(self, request):
        # لو حد دخل على /api/signup/ بطلب GET، هنعمل Redirect لصفحة التسجيل
        return HttpResponseRedirect('/signup/')

    def post(self, request):
        data = request.data
        role = data.get('role')
        
        # Create user
        user_data = {
            'fname': data.get('fname'),
            'lname': data.get('lname'),
            'email': data.get('email'),
            'password_hash': make_password(data.get('password')),
            'phone': data.get('phone'),
            'role': role,
            'height': data.get('height') if role == 'trainee' else None,
            'weight': data.get('weight') if role == 'trainee' else None,
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            
            # If trainer, create record in TRAINER table
            if role == 'trainer':
                trainer_data = {
                    'trainer_id': user.user_id,
                    'specialization': data.get('specialization'),
                    'certification': data.get('certification'),
                }
                trainer_serializer = TrainerSerializer(data=trainer_data)
                if trainer_serializer.is_valid():
                    trainer_serializer.save()
                else:
                    return Response(trainer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = GymUser.objects.get(email=email)
            if check_password(password, user.password_hash):
                return Response({
                    'message': 'Login successful',
                    'user_id': user.user_id,
                    'fname': user.fname,
                    'lname': user.lname,
                    'role': user.role
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except GymUser.DoesNotExist:
>>>>>>> b60a3d5ebed84a802da2556ecaa12a22dfff3aea
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)