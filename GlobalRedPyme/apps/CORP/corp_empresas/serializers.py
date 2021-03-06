from rest_framework import serializers

from apps.CORP.corp_empresas.models import (
    Empresas, EmpresasConvenio
)

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = '__all__'
        read_only_fields = ['_id']

class EmpresasInfoBasicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = ['_id','nombreEmpresa','imagen','nombreComercial']

class EmpresasFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = ['_id','nombreEmpresa','ruc','tipoEmpresa','tipoCategoria']

class EmpresasFiltroIfisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = ['_id','nombreEmpresa','nombreComercial','tipoCategoria','ruc','imagen']

class EmpresasConvenioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasConvenio
        fields = '__all__'
        read_only_fields = ['_id']
    
    def to_representation(self, instance):
            data = super(EmpresasConvenioCreateSerializer, self).to_representation(instance)
            # tomo el campo persona y convierto de OBJECTID a string
            convenio = str(data.pop('convenio'))
            data.update({"convenio": convenio})
            return data

class EmpresasConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasConvenio
        fields = ['convenio']

    def to_representation(self, instance):
            data = super(EmpresasConvenioSerializer, self).to_representation(instance)
            # tomo el campo persona y convierto de OBJECTID a string
            convenio = data.pop('convenio')
            empresa = Empresas.objects.filter(_id=convenio, state=1).first()
            data.update(EmpresasSerializer(empresa).data)
            return data


class EmpresasLogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = ['imagen']