from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CustomUser
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework import filters, pagination
from .pagination import CustomUserLimitOffsetPagination

'''
This view is used for GET and POST operations 

url endpoint looks like (/api/users/)
'''


# class CustomUserPagination(pagination.LimitOffsetPagination):
# 	default_limit = 5

class CustomUserPagination(pagination.PageNumberPagination):
	page_size = 5
	page_size_query_param = 'limit'


class UserList(ListCreateAPIView):

	queryset = CustomUser.objects.all()
	
	serializer_class = CustomUserSerializer			# CustomUser model's Serializer

	filter_backends = [filters.SearchFilter, filters.OrderingFilter]		#these are query filtering backend
	
	search_fields = ['first_name', 'last_name']		#this is used for searching first and last name /?name=keshav (this is case insensitive)
	
	ordering_fields = '__all__'			# this is used for ordering the search result on basis of id, zip, name etc (i am using all the field to give varity to the end user)
	
	pagination_class = CustomUserPagination


	'''
	this commented text is my implementation of limiting as well as paging the search result
	'''
	
	# def get_queryset(self):
	# 	limit = self.request.query_params.get('limit')
	# 	if limit is not None:
	# 		queryset = CustomUser.objects.all()
	# 		CustomUserPagination.page_size = int(limit)
			
	# 	else:
	# 		queryset = CustomUser.objects.all()
	# 		pagination_class = CustomUserPagination
	# 	return queryset





'''
This view is user for GET, PUT, DELETE operations for specific user 

url endpoint looks like (/api/users/<id>)
'''


class UserDetail(APIView):

	# queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

	def get_user(self, pk):
		try:
			return CustomUser.objects.get(id=pk)
		except:
			return False

	def get(self, request, pk):
		user = self.get_user(pk)
		if user:
			serializer = CustomUserSerializer(user)
			return Response(serializer.data)
		else:
			return Response('User not Found', status=404)


	def put(self, request, pk):
		user = self.get_user(pk)
		if user:
			data = JSONRenderer().render(request.data)
			serializer = CustomUserSerializer(instance=user, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=200)
			return Response(serializer.errors, status=400)
		

	def delete(self, request, pk):
		user = self.get_user(pk)
		if user:
			user.delete()
			return Response(status=200)
		