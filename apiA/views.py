from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from apiA.serailizers import StudentSerializer, DepartmentSerializer
from rest_framework.response import Response
from apiA.models import Student, Department
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Way1 : Using APIView
class ViewAllStudents(APIView):

    def post(self, request, *args, **kwargs):
        serailizer = StudentSerializer(data = request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'data': serailizer.data})
        else:
            return Response({'errors':serailizer.errors},status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serailizer = StudentSerializer(students, many=True)
        return Response({'data':serailizer.data})


class StudentsDetails(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            student = Student.objects.get(studentId=pk)
            serailizer = StudentSerializer(student)
            return Response({'data':serailizer.data})
        except Student.DoesNotExist:
            return Response({'data': 'not found'})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            student = Student.objects.get(studentId=pk)
            serailizer = StudentSerializer(instance=student, data=request.data)
            if serailizer.is_valid():
                serailizer.save()
                return Response({'data': serailizer.data})
            else:
                return Response({'errors':serailizer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'data': 'not found'})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            student = Student.objects.get(studentId=pk)
            student.delete()
            return Response({'data': 'deleted'})
        except Student.DoesNotExist:
            return Response({'data': 'not found'})



# Way2 : Using CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
# You cannot Change the Primary Key Here

# class ViewAllDepartment(CreateAPIView, ListAPIView):
#     serializer_class = DepartmentSerializer   # variable name have to be 'serializer_class'
#     queryset = Department.objects.all()    # variable name have to be 'queryset'
#
# class ViewDepartmentDetails(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     serializer_class = DepartmentSerializer  # variable name have to be 'serializer_class'
#     queryset = Department.objects.all()  # variable name have to be 'queryset'



# Way 3: Using ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ViewAllDepartment(ListCreateAPIView):
    serializer_class = DepartmentSerializer   # variable name have to be 'serializer_class'
    queryset = Department.objects.all()    # variable name have to be 'queryset'

class ViewDepartmentDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer  # variable name have to be 'serializer_class'
    queryset = Department.objects.all()  # variable name have to be 'queryset'


