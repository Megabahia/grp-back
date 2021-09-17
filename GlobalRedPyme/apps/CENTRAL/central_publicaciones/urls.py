from django.urls import path,include
from apps.CENTRAL.central_publicaciones.views import(
	publicaciones_create,
	publicaciones_list,
	publicaciones_listOne,
	publicaciones_update,
	publicaciones_delete
)
app_name = 'central_publicaciones'

urlpatterns = [
	path('create/', publicaciones_create, name="publicaciones_create"),
	path('list/', publicaciones_list, name="publicaciones_list"),
	path('listOne/<str:pk>', publicaciones_listOne, name="publicaciones_listOne"),
	path('update/<str:pk>', publicaciones_update, name="publicaciones_update"),
	path('delete/<str:pk>', publicaciones_delete, name="publicaciones_delete"),
]

