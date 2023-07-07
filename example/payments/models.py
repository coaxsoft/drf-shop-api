from django.contrib.auth import get_user_model
from django.db import models


class AbstractPayment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.FloatField(null=True, blank=True)
    is_refundable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Payment(AbstractPayment):
    class Meta:
        db_table = "payments"
        verbose_name = "payment"
        verbose_name_plural = "payments"
        ordering = ("-id",)
