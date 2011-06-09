from django.db import models

from paypal.standard.ipn.signals import payment_was_successful

def payment_receiver(sender, **kwargs):
    ipn_obj = sender
    print 'received signal for payment'
payment_was_successful.connect(payment_receiver)
