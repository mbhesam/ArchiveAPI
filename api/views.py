from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.services import count_objects,search_objects
from api.serializers import DataSerializer
from rest_framework import status
from drf_yasg import openapi

class ShowEntityCount(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                   description="field you want to order by to",
                                   required=False,
                                   type=openapi.TYPE_STRING)
    @swagger_auto_schema(request_body=DataSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = DataSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch",False) == "false":
            counts = count_objects(query=data_query.validated_data,exact=False)
        else:
            counts = count_objects(query=data_query.validated_data)
        return Response({"total_count":counts}, status=status.HTTP_200_OK)

class ShowEntitySearch(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                 description="field you want to order by to",
                                 type=openapi.TYPE_STRING)
    @swagger_auto_schema( request_body=DataSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = DataSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch",False) == "false":
            objects = search_objects(query=data_query.validated_data,exact=False)
        else:
            objects = search_objects(query=data_query.validated_data)
        return Response(objects, status=status.HTTP_200_OK)
