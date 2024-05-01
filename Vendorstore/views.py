import uuid
import time

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Vendorstore.models import *
from Vendorstore.serializer import *
# Create your views here.

class VendorSroreApiView(APIView):
    def get(self, request, vendor_id):
        if vendor_id:
            vendor = get_object_or_404(VendorModel, id=vendor_id)
            serializer = VendorSerializer(vendor)
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            vendors = VendorModel.objects.all()
            serializer = VendorSerializer(vendors, many=True)
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': 'True',
                'status_code': status.HTTP_201_CREATED,
                'message': 'Vendor created successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid data',
                'data': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, vendor_id):
        vendor = get_object_or_404(VendorModel, id=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Vendor updated successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid data',
                'data': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, vendor_id):
        vendor = get_object_or_404(VendorModel, id=vendor_id)
        vendor.delete()
        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': 'Vendor deleted successfully',
        }
        return Response(data, status=status.HTTP_200_OK)
    
class PurchaseOrderApiView(APIView):
    def get(self, request, po_id):
        if po_id:
            po = get_object_or_404(PurchaseOrder, id=po_id)
            serializer = PurchaseOrderSerializer(po)
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            pos = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(pos, many=True)
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Generate a unique PO Number ------------------------------------
        unique_id = uuid.uuid4().hex[:6] 
        timestamp = str(int(time.time()))[-6:]
        prefix = 'PO'
        po_number = f"{prefix}-{timestamp}-{unique_id}"
        
        data_copy = request.data.copy()
        data_copy['po_number'] = po_number
        serializer = PurchaseOrderSerializer(data=data_copy,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': 'True',
                'status_code': status.HTTP_201_CREATED,
                'message': 'Purchase Order created successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid data',
                'data': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, po_id):
        purchaseOrder = get_object_or_404(PurchaseOrder, po_number=po_id)
        serializer = PurchaseOrderSerializer(purchaseOrder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': 'True',
                'status_code': status.HTTP_200_OK,
                'message': 'Purchase Order updated successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid data',
                'data': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, po_id):
        purchaseOrder = get_object_or_404(PurchaseOrder, po_number=po_id)
        purchaseOrder.delete()
        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': 'Purchase Order deleted successfully',
        }
        return Response(data, status=status.HTTP_200_OK)
    
