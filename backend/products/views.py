from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from rest_framework import serializers


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(f"in save")
        shape = serializer.validated_data.get('shape')
        # print(f"shape is {shape}")
        len_a = serializer.validated_data.get('a')
        len_b = serializer.validated_data.get('b')
        len_c = serializer.validated_data.get('c')
        # print(f"{len_a},{len_b},{len_c}")
        len_a, length_b, length_c = check_data(shape, len_a, len_b, len_c)
        # print(f"check done, update length is {len_a},{len_b},{len_c}")
        serializer.save(a=len_a, b=len_b, c=len_c)
        # send a Django signal


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        print(f"{instance.shape}, a is {instance.a}, b is {instance.b}, c is {instance.c}")
        instance.a, instance.b, instance.c = check_data(instance.shape, instance.a, instance.b, instance.c)
        print(instance)
        ##


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


def check_data(shape, a, b, c):
    # check input data is legal
    # print(f"check data{a}, {b}, {c}")
    if shape == "triangle":
        # check a, b, c are positive
        if a <= 0 or b <= 0 or c <= 0:
            raise serializers.ValidationError({"length": "input is not valid for triangle"})
        # check legal triangle
        if (a + b <= c) or (b + c <= a) or (c + a <= b):
            raise serializers.ValidationError({"length": "input is not valid, can not create a triangle"})
    elif shape == "rectangle":
        if a <= 0 or b <= 0 or a == b:
            raise serializers.ValidationError({"length": "input is not valid for rectangle"})
        # set unnecessary value to zero
        c = 0
    elif shape == "square":
        if a <= 0:
            raise serializers.ValidationError({"length": "input is not valid for square"})
        # set unnecessary value to zero
        b = 0
        c = 0
    elif shape == "diamond":
        if a <= 0 or b <= 0:
            raise serializers.ValidationError({"length": "input is not valid for diamond"})
        # set unnecessary value to zero
        c = 0
    else:
        # not support shape
        raise serializers.ValidationError({"detail": "input is not valid"})
    return a, b, c
