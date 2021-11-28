from django.urls import path,include
from apps.CORP.corp_cobrarSupermonedas.views import(
	cobrarSupermonedas_create,
	cobrarSupermonedas_list,
	cobrarSupermonedas_listOne,
	cobrarSupermonedas_update,
	cobrarSupermonedas_delete
)
app_name = 'corp_cobrarSupermonedas'

urlpatterns = [
	path('create/', cobrarSupermonedas_create, name="cobrarSupermonedas_create"),
	path('list/', cobrarSupermonedas_list, name="cobrarSupermonedas_list"),
	path('listOne/<str:pk>', cobrarSupermonedas_listOne, name="cobrarSupermonedas_listOne"),
	path('update/<str:pk>', cobrarSupermonedas_update, name="cobrarSupermonedas_update"),
	path('delete/<str:pk>', cobrarSupermonedas_delete, name="cobrarSupermonedas_delete"),
]

