from django.db import models


class Order(models.Model):

    STATUS_PENDING = "PENDING"
    STATUS_PROCESSING = "PROCESSING"
    STATUS_COMPLETED = "COMPLETED"
    STATUS_CANCELD= "CANCELD"

    STATUS_CHOICES = (
        (STATUS_PENDING, 'pending status'),
        (STATUS_PROCESSING, 'processing status'),
        (STATUS_COMPLETED, 'completed status'),
        (STATUS_CANCELD, 'canceld status'),
    )

    total_amount = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=12)

    customer_name = models.CharField(verbose_name="Customer Name", max_length=255)

    customer_email = models.EmailField(verbose_name="Customer Email", max_length=255)

    status = models.CharField(choices=STATUS_CHOICES, max_length=25, default=STATUS_PENDING)

    create_date = models.DateTimeField(auto_now_add=True)

    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#{} {}".format(self.pk, self.customer_name)