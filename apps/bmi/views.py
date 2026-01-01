from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Talaba, BitiruMalakaviyIsh, Fayl, Baholash
from .serializers import (
    
    TalabaSerializer, 
    BitiruMalakaviyIshSerializer, 
    FaylSerializer, 
    BaholashSerializer
)



class TalabaViewSet(viewsets.ModelViewSet):
   
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['guruh', 'fakultet'] 
    search_fields = ['ism', 'familiya', 'email']  
    ordering_fields = ['id', 'ism', 'familiya']
    ordering = ['id']

    def get_queryset(self):
        
        queryset = super().get_queryset()
        
        return queryset

    @action(detail=True, methods=['get'])
    def bitiruvchi_ishlari(self, request, pk=None):
        
        talaba = self.get_object()
        ishlar = BitiruMalakaviyIsh.objects.filter(talaba=talaba)
        serializer = BitiruMalakaviyIshSerializer(ishlar, many=True)
        return Response(serializer.data)



class BitiruMalakaviyIshViewSet(viewsets.ModelViewSet):
   
    queryset = BitiruMalakaviyIsh.objects.select_related('talaba').all()
    serializer_class = BitiruMalakaviyIshSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['talaba', 'holat', 'turi'] 
    search_fields = ['mavzu', 'tavsif']
    ordering_fields = ['id', 'yaratilgan_sana']
    ordering = ['-yaratilgan_sana']

    def get_queryset(self):
  
        queryset = super().get_queryset()
        
        return queryset

    @action(detail=True, methods=['get'])
    def fayllar(self, request, pk=None):
        
        ish = self.get_object()
        fayllar = Fayl.objects.filter(bitiruvchi_ish=ish)
        serializer = FaylSerializer(fayllar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def baholashlar(self, request, pk=None):
       
        ish = self.get_object()
        baholashlar = Baholash.objects.filter(bitiruvchi_ish=ish)
        serializer = BaholashSerializer(baholashlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def tasdiqlash(self, request, pk=None):
       
        ish = self.get_object()
        ish.holat = 'tasdiqlangan'  
        ish.save()
        return Response({'status': 'Bitiruvchi ish tasdiqlandi'})



class FaylViewSet(viewsets.ModelViewSet):
 
    queryset = Fayl.objects.select_related('bitiruvchi_ish').all()
    serializer_class = FaylSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['bitiruvchi_ish', 'turi']  
    search_fields = ['nomi', 'tavsif']
    ordering_fields = ['id', 'yuklangan_sana']
    ordering = ['-yuklangan_sana']

    def perform_create(self, serializer):
     
        serializer.save()

    @action(detail=True, methods=['get'])
    def yuklab_olish(self, request, pk=None):
        
        fayl = self.get_object()
       
        return Response({'url': fayl.fayl.url if hasattr(fayl, 'fayl') else None})



class BaholashViewSet(viewsets.ModelViewSet):
   
    queryset = Baholash.objects.select_related('bitiruvchi_ish', 'baholovchi').all()
    serializer_class = BaholashSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['bitiruvchi_ish', 'baholovchi', 'baho']
    search_fields = ['izoh', 'tavsiya']
    ordering_fields = ['id', 'baholangan_sana']
    ordering = ['-baholangan_sana']

    def perform_create(self, serializer):
        
        serializer.save(baholovchi=self.request.user)

    @action(detail=False, methods=['get'])
    def mening_baholashlarim(self, request):
        
        baholashlar = self.queryset.filter(baholovchi=request.user)
        serializer = self.get_serializer(baholashlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def tahrirlash(self, request, pk=None):
       
        baholash = self.get_object()
        if baholash.baholovchi != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Faqat o\'z baholashingizni tahrirlashingiz mumkin'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(baholash, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)