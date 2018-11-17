from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

from orders.models import Order


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # 支付成功
        order = get_object_or_404(Order, id=ipn_obj.invioce)
        # 标记为已支付
        order.paid = True
        order.save()


valid_ipn_received.connect(payment_notification)
