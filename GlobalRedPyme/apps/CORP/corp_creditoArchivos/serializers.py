from rest_framework import serializers
# ObjectId
from bson import ObjectId

from apps.CORP.corp_creditoArchivos.models import (
    PreAprobados,
)

from apps.CORP.corp_empresas.models import Empresas 

class CreditoArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAprobados
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        data = super(CreditoArchivosSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        empresa_financiera = data.pop('empresa_financiera')
        empresa_comercial = data.pop('empresa_comercial')
        entidadFinanciera = Empresas.objects.filter(_id=ObjectId(empresa_financiera), state=1).first()
        entidadComercial = Empresas.objects.filter(_id=ObjectId(empresa_comercial), state=1).first()
        if entidadFinanciera:
            data['empresa_financiera'] = entidadFinanciera.nombreComercial
        if entidadComercial:
            data['empresa_comercial'] = entidadComercial.nombreComercial
        return data
