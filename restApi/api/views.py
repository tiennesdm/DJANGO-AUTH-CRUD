from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
# from django.db import models
# from django_matplotlib.fields import MatplotlibFigureField
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpResponse
from django.db import models
from django_matplotlib.fields import MatplotlibFigureField




# Create your views here.
from .models import Book
from .serializers import BookSerializer
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class DetailView(generics.RetrieveAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class SQLRAWQUERY():
    @api_view(['GET', 'POST','DELETE'])
    def raw_SQL(request):

        """
        List all code snippets, or create a new snippet.
        """
        with connection.cursor() as cursor:
            # print('isAuth', IsAuthenticated)
            # permission_classes = (IsAuthenticated,)
            if request.method == 'GET':

                cursor.execute("SELECT * FROM api_book")
                data = cursor.fetchall()
                print(data)
                return JsonResponse(data, safe=False)
            elif request.method == 'POST':

                # print(request)
                #
                # print(request.data)
                # id = request.data['id']
                title = request.data['title']
                subtitle = request.data['subtitle']
                author = request.data['author']
                isbn = request.data['isbn']

                # print(id)
                # query= "INSERT INTO api_book (id, title, subtitle, author, isbn) VALUES ('{id}', '{title}','{subtitle}','{author}','{isbn}')"
                # query.format(id=id, title=title,subtitle=subtitle,author=author,isbn=isbn)
                format_str = """INSERT INTO api_book (title, subtitle, author, isbn)
                  VALUES ('{title}', '{subtitle}', '{author}', '{isbn}');"""
                sql_command = format_str.format(title=title, subtitle=subtitle, author=author, isbn=isbn)
                print(sql_command)
                data = cursor.execute(sql_command)
                userData = cursor.fetchall()
                print(userData)
                print(data)
                if (data == 1):
                    return Response(data={"data": "SuccessFully Updated", }, status=status.HTTP_201_CREATED)
                else:
                    return Response(data={"Error": "Something Missing"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            elif request.method == 'DELETE':
                format_str = """DELETE FROM api_book WHERE id = {id}"""
                sql_command = format_str.format(id = request.data['id'])
                print(sql_command)
                data = cursor.execute(sql_command)
                print(data)
                if(data==1):
                    return Response(data={"data": "SuccessFully Updated", }, status=status.HTTP_201_CREATED)
                else:
                    return Response(data={"Error": "Something Missing"}, status=status.HTTP_406_NOT_ACCEPTABLE)



                # print(request)
class MatPlotLib(models.Model):
    @api_view(['GET'])
    def pandaView(self):
        fig, ax = plt.subplots()

        # Load in data
        tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

        # Create violinplot
        ax.violinplot(tips["total_bill"], vert=False)
        # fig = MatplotlibFigureField(figure=plt., verbose_name='figure',
        #                             silent=True)

        # Show the plot
        # plt.show()
        # data = 'hello'
        # html = '<html><body>{plot}</body></html>'
        # html.format(plot=plt.show())
        return HttpResponse(plt.show())



# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)





