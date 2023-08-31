from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=70, db_collation='utf8mb3_general_ci', blank=True, null=True)
    phone = models.CharField(max_length=70, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mail = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    image = models.CharField(max_length=70, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dateupdated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'