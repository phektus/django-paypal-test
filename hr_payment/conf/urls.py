from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    (r'^payment/subscribe', 'hr_payment.apps.payment.views.subscribe'),
    (r'^payment/paypal_return', 'hr_payment.apps.payment.views.paypal_return'),
    (r'^payment/paypal_cancel', 'hr_payment.apps.payment.views.paypal_cancel'),
    (r'^payment/ipnsecret234299394/', include('paypal.standard.ipn.urls')),
)
