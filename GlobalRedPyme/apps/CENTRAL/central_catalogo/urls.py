from django.urls import path,include
from apps.CENTRAL.central_catalogo.views import(
	catalogo_list,catalogo_create,catalogo_findOne,catalogo_update,catalogo_delete,
	estado_list, pais_list,tipo_list,catalogo_list_hijo,catalogo_list_hijoNombre,catalogo_list_hijos,
	catalogo_list_parametrosTipo, catalogo_listSinPaginacion,
	catalogo_filter_name

)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'catalogo'

urlpatterns = [
	#catalogo
	path('list/', catalogo_list, name="catalogo_list"),
	path('listSinPaginacion/', catalogo_listSinPaginacion, name="catalogo_listSinPaginacion"),
	path('create/', catalogo_create, name="catalogo_create"),
	path('listOne/<str:pk>', catalogo_findOne, name="catalogo_findOne"), 
	path('update/<str:pk>', catalogo_update, name="catalogo_update"), 
	path('delete/<str:pk>', catalogo_delete, name="catalogo_delete"), 
	#ESTADO
	path('list/estado/', estado_list, name="estado_list"), 
	#PAIS
	path('list/pais/', pais_list, name="pais_list"), 
	#TIPO PARAMETRIZACION/CATALOGO
	path('list/tipo/', tipo_list, name="tipo_list"), 
	#INFORMACION DEL PADRE
	path('list/tipo/hijo/<str:pk>', catalogo_list_hijo, name="tipohijo_list"), 
	#HIJOS DEL TIPO
	path('list/tipo/hijo/nombre/', catalogo_list_hijoNombre, name="tijohijonombre_list"), 
	#buscar todos los nombres que pertenecen al tipo enviado
	path('list/tipo/hijo/', catalogo_list_hijos, name="tipoPadre__list"), 
	#buscar todos LOS QUE TENGAN EL PARÁMETRO
	path('list/tipo/todos/', catalogo_list_parametrosTipo, name="catalogo_list_parametrosTipo"), 
	# FILTRO Y NOMBRE
	path('list/filtro/nombre', catalogo_filter_name, name="parametrizaciones_filter_name"),
]
