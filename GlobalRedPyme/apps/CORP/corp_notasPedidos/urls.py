from django.urls import path,include
from apps.CORP.corp_notasPedidos.views import(
    factura_list, factura_create, factura_findOne, factura_list_latest, factura_update,
	factura_findOne_credito, factura_generar_codigos_envios,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'facturas'

urlpatterns = [
	#facturas
	path('list/', factura_list, name="factura_list"),
	path('create/', factura_create, name="factura_create"),
	path('listOne/<int:pk>', factura_findOne, name="factura_findOne"), 
	path('listOne/credito/<str:pk>', factura_findOne_credito, name="factura_findOne_credito"), 
	path('listLatest/', factura_list_latest, name="factura_list_latest"),	
	path('update/<int:pk>', factura_update, name="factura_update"), 
	path('generar/habilitantes/credito/', factura_generar_codigos_envios, name="factura_generar_codigos_envios"),
]