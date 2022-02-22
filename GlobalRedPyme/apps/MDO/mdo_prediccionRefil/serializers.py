from rest_framework import serializers

from apps.MDO.mdo_prediccionRefil.models import PrediccionRefil, Detalles

import requests
import datetime
from apps.config import config

# Listar predicciones crosseling
class PrediccionRefilListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediccionRefil
       	fields = '__all__'

# Guardar Factura
class DetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles
       	fields = '__all__'

class PrediccionRefilSerializer(serializers.ModelSerializer):
    detalles = DetallesSerializer(many=True)
    class Meta:
        model = PrediccionRefil
       	fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        validated_data["fechaPredicciones"] = datetime.datetime.now().date()
        prediccionRefil = PrediccionRefil.objects.filter(fechaPredicciones=validated_data['fechaPredicciones'],cliente=validated_data['cliente'],state=1).first()
        if prediccionRefil is None:        
            prediccionRefil = PrediccionRefil.objects.create(**validated_data)
        
        for detalle_data in detalles_data:
            Detalles.objects.create(prediccionRefil=prediccionRefil, **detalle_data)
        return prediccionRefil

# Detalles con imagenes
class DetallesImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles
       	fields = ['id','articulo','codigo','cantidad','precio']

    def to_representation(self, instance):
        auth_data = {'codigo': str(instance.codigo)}
        resp = requests.post(config.API_BACK_END+'mdp/productos/producto/image/', data=auth_data)
        data = super(DetallesImagenesSerializer, self).to_representation(instance)
        if resp.json()['imagen']:
            data['imagen'] = resp.json()['imagen']
        return data

# PREDICCION Refil 
class PrediccionRefilProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles
       	fields = ['id','articulo','codigo','cantidad','precio','informacionAdicional']

    def to_representation(self, instance):
        auth_data = {'producto': str(instance.codigo)}
        resp = requests.post(config.API_BACK_END+'mdp/productos/prediccionRefil/', data=auth_data)
        data = super(PrediccionRefilProductosSerializer, self).to_representation(instance)
        
        data['fechaCompra'] = instance.prediccionRefil.created_at
        data['predicciones'] = resp.json()

        return data

