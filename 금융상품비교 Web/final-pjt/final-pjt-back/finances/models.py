from django.db import models

# Create your models here.
class Finance(models.Model):
    prdt_category = models.CharField(max_length=10)
    fin_prdt_cd =models.TextField(unique=True)
    dcls_month = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way =models.TextField()
    spcl_cnd = models.TextField()
    join_deny =models.IntegerField()
    join_member = models.TextField()
    max_limit = models.IntegerField(null=True)

class Option(models.Model):
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    fin_prdt_cd =models.TextField()
    intr_rate_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2= models.FloatField()

