from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from rest_framework import serializers, permissions
from user.auth import UserAuth
from user.permissions import IsUser


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (UserAuth,)
    permission_classes = (IsUser,)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(f"in save")
        shape = serializer.validated_data.get('shape')
        # print(f"shape is {shape}")
        len_a = serializer.validated_data.get('a')
        len_b = serializer.validated_data.get('b')
        len_c = serializer.validated_data.get('c')
        # print(f"{len_a},{len_b},{len_c}")
        len_a, len_b, len_c = check_data(shape, len_a, len_b, len_c)
        # print(f"check done, update length is {len_a},{len_b},{len_c}")
        serializer.save(a=len_a, b=len_b, c=len_c)
        # send a Django signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes
    authentication_classes = (UserAuth,)
    # permission_class
    permission_classes = (IsUser,)

    def get(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        print(f"get action is {action}")
        # show get result
        if action is None:
            return self.retrieve(request, *args, **kwargs)

        # area
        if action.lower() == "area":
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            # get area
            area = self.calculate_area(serializer.data)
            data = {
                "id": serializer.data.get('id'),
                "shape": serializer.data.get('shape'),
                "area": area
            }
            return Response(data)
        elif action.lower() == "perimeter":
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            # get perimeter
            perimeter = self.calculate_perimeter(serializer.data)
            data = {
                "id": serializer.data.get('id'),
                "shape": serializer.data.get('shape'),
                "perimeter": perimeter
            }
            return Response(data)

    @staticmethod
    def calculate_area(shape_detail):
        shape = shape_detail.get('shape')
        a = shape_detail.get('a')
        b = shape_detail.get('b')
        c = shape_detail.get('c')

        if shape == 'triangle':
            p = (a + b + c) / 2
            area = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
            return area
        elif shape == 'rectangle':
            return a * b
        elif shape == 'square':
            return a * a
        elif shape == 'diamond':
            return a * b / 2

    @staticmethod
    def calculate_perimeter(shape_detail):
        shape = shape_detail.get('shape')
        a = shape_detail.get('a')
        b = shape_detail.get('b')
        c = shape_detail.get('c')

        if shape == 'triangle':
            return a + b + c
        elif shape == 'rectangle':
            return 2 * (a + b)
        elif shape == 'square':
            return 4 * a
        elif shape == 'diamond':
            return 2 * pow((a * a + b * b), 0.5)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # authentication_classes
    authentication_classes = (UserAuth,)
    # permission_class
    permission_classes = (IsUser,)

    def perform_update(self, serializer):
        instance = serializer.save()
        print(f"{instance.shape}, a is {instance.a}, b is {instance.b}, c is {instance.c}")
        instance.a, instance.b, instance.c = check_data(instance.shape, instance.a, instance.b, instance.c)
        print(instance)
        ##


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # authentication_classes
    authentication_classes = (UserAuth,)
    # permission_class
    permission_classes = (IsUser,)

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


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
