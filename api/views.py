from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.services import count_objects
from api.serializers import DataSerializer
from rest_framework import status

class ShowEntityCount(APIView):
    @swagger_auto_schema(request_body=DataSerializer)
    def post(self,request):
        try:
            data_query = DataSerializer(data=request.data)
            data_query.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        counts = count_objects(query=data_query.validated_data)
        return Response({"total_count":counts}, status=status.HTTP_200_OK)