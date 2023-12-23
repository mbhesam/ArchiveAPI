from django.http import FileResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from download import utils


# Create your views here.
class File(APIView):
    def get(self, request, file_path):
        filename = utils.get_file_name(file_path)
        compressed, zip_path, inner_file_path = utils.is_in_compressed(file_path)
        if compressed:
            _file = utils.get_file_from_zip(zip_path, inner_file_path)
            if _file:
                return FileResponse(_file, as_attachment=True, filename=filename)
            else:
                return Response(
                    {
                        'detail': 'File not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            _file = utils.get_file_or_none(file_path)
            if _file:
                return FileResponse(_file, as_attachment=True, filename=filename)
            else:
                utils.create_single_image(image_path=file_path)
                _file = utils.get_file_or_none(file_path)
                if _file:
                    return FileResponse(_file, as_attachment=True, filename=filename)
                return Response(
                    {
                        'detail': 'File not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

