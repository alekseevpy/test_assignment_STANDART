from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from invoices.models import Invoice
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InvoiceSerializer, PaymentDetailSerializer


@swagger_auto_schema(
    method="post",
    request_body=InvoiceSerializer,
    responses={
        201: openapi.Response(
            description="Invoice created successfully",
            examples={
                "application/json": {
                    "invoice_id": 0,
                    "payment_detail": {
                        "id": 0,
                        "payment_type": "string",
                        "account_or_card_type": "string",
                        "owner_name": "string",
                        "phone_number": "string",
                        "limit_amount": 0,
                    },
                }
            },
        ),
        400: openapi.Response(
            description="Bad Request, check the request body",
        ),
    },
)
@api_view(["POST"])
def create_invoice(request):
    """
    Создание Заявки.
    ---
    """
    data = request.data
    payment_detail_data = data.get("payment_detail", {})

    invoice_serializer = InvoiceSerializer(data=data)
    if invoice_serializer.is_valid():
        payment_detail_serializer = PaymentDetailSerializer(
            data=payment_detail_data
        )
        if payment_detail_serializer.is_valid():
            payment_detail = payment_detail_serializer.save()
            invoice = invoice_serializer.save(payment_detail=payment_detail)

            response_data = {
                "invoice_id": invoice.id,
                "payment_detail": payment_detail_serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(
        invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


class InvoiceStatusView(APIView):
    """
    Проверка Статуса заявки.
    ---
    """

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="invoice_id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="ID of the invoice",
                required=True,
            )
        ],
        responses={
            201: openapi.Response(
                description="Status checked successfully",
                examples={"application/json": {"name": "Ожидает оплаты"}},
            ),
            400: openapi.Response(
                description="Bad Request, check the request body",
            ),
        },
    )
    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response(
                {"detail": "Invoice not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        status_data = {
            invoice.status.name,
        }

        return Response(status_data)
