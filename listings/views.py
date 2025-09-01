from rest_framework import viewsets
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # Trigger the email task asynchronously
        send_booking_confirmation_email.delay(booking.id, booking.email)
