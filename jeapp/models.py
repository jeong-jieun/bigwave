from django.db import models

### DB에서 문자열을 관리하는 타입은 CharField 사용
from django.db.models.fields import CharField
### DB에서 숫자값을 관리하는 타입은 IntegerField 사용
from django.db.models.fields import IntegerField


class Member(models.Model):
    mem_id = CharField(primary_key=True, max_length=20, null=False)
    mem_pass = CharField(max_length=20, null=False)
    mem_name = CharField(max_length=15, null=False)
    mem_regno1 = IntegerField(null=False)
    mem_regno2 = IntegerField(null=False)
    mem_zip = IntegerField(null=False)
    mem_add1 = CharField(max_length=100, null=False)
    mem_add2 = CharField(max_length=80, null=False)
    mem_hp = CharField(max_length=11, null=False)
    class Meta:
        db_table = "member"
        app_label = "jeapp"
        managed = False
        
class Marina(models.Model):
    mar_nm = CharField(primary_key=True, max_length=30, null=False)
    mar_add1 = CharField(max_length=100, null=False)
    mar_add2 = CharField(max_length=80, null=False)
    class Meta:
        db_table = "marina"
        app_label = "jeapp"
        managed = False
        
class Schedule(models.Model):
    sch_no = IntegerField(primary_key=True, null=False)
    sch_marina = CharField(max_length=30, null=False)
    sch_arrival = CharField(max_length=30, null=False)
    sch_taxi = CharField(max_length=10, null=False)
    # auto_now_add=True : 객체가 처음 생성될 때의 날짜
    # auto_now=True : 모델 객체가 저장될 때마다 자동 업데이트
    sch_stime = CharField(max_length=30, null=False)
    sch_etime = CharField(max_length=30, null=False)
    class Meta:
        db_table = "schedule"
        app_label = "jeapp"
        managed = False
        
class Booking(models.Model):
    book_no = IntegerField(primary_key=True, null=False)
    book_mem = CharField(max_length=30, null=False)
    book_qty = IntegerField(null=False)
    book_price = CharField(max_length=15, null=False)
    book_marina = CharField(max_length=30, null=False)
    book_arrival = CharField(max_length=30, null=False)
    book_taxi = CharField(max_length=10, null=False)
    class Meta:
        db_table = "booking"
        app_label = "jeapp"
        managed = False