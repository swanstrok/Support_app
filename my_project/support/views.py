from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *

# Create your views here.
from .permissions import IsAdminorOwnerOrReadOnly
from .serializers import TicketSerializer, CommentSerializer


class TicketViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminorOwnerOrReadOnly,)

    # @action(methods=['get'], detail=False)
    # def chy(self, request):
    #     comm = CommentTicket.objects.all()
    #     return Response({'comm': [c.title for c in comm]})


class CommentViewset(viewsets.ModelViewSet):
    queryset = CommentTicket.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminorOwnerOrReadOnly, )


# class TicketViewset(generics.ListCreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class TicketAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class TicketAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAdminOrReadOnly,)


# class TicketViewset(generics.ListCreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class TicketAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class TicketAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (IsAdminOrReadOnly,)


# class CommentAPIList(generics.ListCreateAPIView):
#     queryset = CommentTicket.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAdminOrReadOnly, )
#
#
# class CommentAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CommentTicket.objects.all()
#     serializer_class = CommentSerializer
