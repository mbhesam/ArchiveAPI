from django.urls import path ,include,re_path
from api.views import ShowEntityCount,UpdateEntity ,ShowEntityJsonSearch ,DeleteEntityRangeDelete ,ShowEntityRangeSearch,DeleteEntityJsonDelete,CreateEntity,Bookreader,ShowAttachmentsName
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="testing@api.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('show_entity/_count',ShowEntityCount.as_view()),
    path('show_entity/json/_search', ShowEntityJsonSearch.as_view()),
    path('show_entity/range/_search',ShowEntityRangeSearch.as_view()),
    path('delete_entity/json/_delete',DeleteEntityJsonDelete.as_view()),
    path('delete_entity/range/_delete', DeleteEntityRangeDelete.as_view()),
    path('create_entity/_create',CreateEntity.as_view()),
    path('update_entity/_update',UpdateEntity.as_view()),
    path('bookreader/<str:entity>/<str:pdf_name>',Bookreader.as_view()),
    path('show_attachments/<str:entity>/', ShowAttachmentsName.as_view()),
]

