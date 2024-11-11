from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from rest_framework import authentication,permissions

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import action

from api.models import Expense,Income

from api.serializers import ExpenseSerializer,UserSerializer,IncomeSerializer



class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):

        serializer_instance=UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
class ExpenseViewSetView(viewsets.ModelViewSet):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    def list(self,request,*args,**kwargs):

        qs=Expense.objects.filter(user_object=request.user)

        serializer_instance=ExpenseSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def perform_create(self,serializer):
        
        serializer.save(user_object=self.request.user)
    


class CategoryListView(APIView):

    def get(self,request,*args,**kwargs):

        categories = [category[0] for category in Expense.expense_categories]

        return Response(data=categories)



class IncomeViewSetView(viewsets.ModelViewSet):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=IncomeSerializer

    queryset=Income.objects.all()

    def list(self,request,*args,**kwargs):

        qs=Income.objects.filter(user_object=request.user)

        serializer_instance=IncomeSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def perform_create(self,serializer):

        serializer.save(user_object=self.request.user)





