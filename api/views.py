from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from api.services import delete_objects,update_object,count_objects,search_objects,search_range_objects,delete_range_objects,create_object
from api.serializers import JsonSearchSerializer, IdentifierRangeSerializer , UpdateSerializer
from rest_framework import status
from drf_yasg import openapi

class ShowEntityCount(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                   description="field you want to order by to",
                                   required=False,
                                   type=openapi.TYPE_STRING)
    @swagger_auto_schema(request_body=JsonSearchSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = JsonSearchSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch",False) == "false":
            counts = count_objects(query=data_query.validated_data,exact=False)
        else:
            counts = count_objects(query=data_query.validated_data)
        return Response({"total_count":counts}, status=status.HTTP_200_OK)

class ShowEntityJsonSearch(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                 description="field you want to order by to",
                                 type=openapi.TYPE_STRING)
    @swagger_auto_schema( request_body=JsonSearchSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = JsonSearchSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch",False) == "false":
            objects = search_objects(query=data_query.validated_data,exact=False)
        else:
            objects = search_objects(query=data_query.validated_data)
        return Response(objects, status=status.HTTP_200_OK)

class ShowEntityRangeSearch(APIView):
    @swagger_auto_schema(request_body=IdentifierRangeSerializer)
    def post(self,request):
        try:
            data_query = IdentifierRangeSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        objects = search_range_objects(data_query.validated_data)
        return Response(objects,status.HTTP_200_OK)

class DeleteEntityJsonDelete(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                 description="field you want to order by to",
                                 type=openapi.TYPE_STRING)
    @swagger_auto_schema( request_body=JsonSearchSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = JsonSearchSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch",False) == "false":
            object = delete_objects(query=data_query.validated_data, exact=False)
        else:
            object = delete_objects(query=data_query.validated_data)
        return Response(object, status=status.HTTP_200_OK)

class DeleteEntityRangeDelete(APIView):
    @swagger_auto_schema(request_body=IdentifierRangeSerializer)
    def post(self,request):
        try:
            data_query = IdentifierRangeSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        objects = delete_range_objects(data_query.validated_data)
        return Response(objects,status.HTTP_200_OK)

class CreateEntity(APIView):
    @swagger_auto_schema(request_body=JsonSearchSerializer)
    def post(self,request):
        try:
            data_query = JsonSearchSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        docs = create_object(data_query.validated_data)
        if docs == False:
            return Response("the object has not created because it does not have required field in json")
        return Response(docs,status.HTTP_200_OK)

class UpdateEntity(APIView):
    exactmatch = openapi.Parameter('exactmatch', openapi.IN_QUERY,
                                 description="field you want to order by to",
                                 type=openapi.TYPE_STRING)
    @swagger_auto_schema(request_body=UpdateSerializer,manual_parameters=[exactmatch])
    def post(self,request):
        try:
            data_query = UpdateSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.query_params.get("exactmatch", False) == "false":
            docs = update_object(query=data_query.validated_data, exact=False)
        else:
            docs = update_object(query=data_query.validated_data)
        return Response(docs,status.HTTP_200_OK)




# class UploadEntity(APIView):
#     parser_classes = (MultiPartParser,FileUploadParser)
#     ...
#     collectionName = openapi.Parameter('collectionName', openapi.IN_QUERY,
#                                  description="field you want to order by to",
#                                  type=openapi.TYPE_STRING)
#     @swagger_auto_schema(operation_description='Upload file...',request_body=JsonSearchSerializer,manual_parameters=[collectionName])
#     @action(detail=False, methods=['post'])
#     def post(self,request):
#         try:
#             data_query = JsonSearchSerializer(data=request.data)
#             data_query.is_valid(raise_exception=True)
#         except:
#             return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#         if request.query_params.get("exactmatch",False) == "false":
#             objects = search_objects(query=data_query.validated_data,exact=False)
#         else:
#             objects = search_objects(query=data_query.validated_data)
#         return Response(objects, status=status.HTTP_200_OK)
