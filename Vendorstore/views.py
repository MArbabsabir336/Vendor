import uuid
import time

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from Vendorstore.models import *
from Vendorstore.serializer import *
from Vendorstore.logic import *
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    

class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': 'Login successful',
            'Token': token.key,
        }
        return Response(data, status=status.HTTP_200_OK)
    
class VendorSroreApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, vendor_id=None):
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
            vendors = VendorModel.objects.order_by('-created_at')
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
    permission_classes = [IsAuthenticated]
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
            pos = PurchaseOrder.objects.select_related('vendor').order_by('-created_at')
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
    
    
class HistoricalPerformanceApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, vendor_id):
        if not vendor_id:
            data = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Vendor ID is required',
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        historical_performances = HistoricalPerformance.objects.filter(vendor_id=vendor_id)
        serializer = HistoricalPerformanceSerializer(historical_performances, many=True)
        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': ' Vendor Performance History Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    
class VendorPerformanceApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, vendor_id):
        vendor = get_object_or_404(VendorModel, id=vendor_id)
        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': 'Get Vendor Performance Success',
            'data': {
                'vendor_name': vendor.name,
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate
            }
        }
        return Response(data, status=status.HTTP_200_OK)


class AcknowledgePurchaseOrderApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, po_number=po_id)
        purchase_order.acknowledgment_date = timezone.now()  # Update acknowledgment_date
        purchase_order.save()  # Save the changes

        # Recalculate average_response_time
        calculate_average_response_time(purchase_order.vendor)

        data = {
            'success': 'True',
            'status_code': status.HTTP_200_OK,
            'message': 'Purchase Order acknowledged successfully',
        }
        return Response(data, status=status.HTTP_200_OK)
