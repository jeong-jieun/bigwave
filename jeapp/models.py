from django.db import models

### DB에서 문자열을 관리하는 타입은 CharField 사용
from django.db.models.fields import CharField
### DB에서 숫자값을 관리하는 타입은 IntegerField 사용
from django.db.models.fields import IntegerField
from django.db.models.fields import BigIntegerField
from django.db.models.fields import FloatField


class Member(models.Model):
    mem_id = CharField(primary_key=True, max_length=20, null=False)
    mem_pass = CharField(max_length=20, null=False)
    mem_name = CharField(max_length=15, null=False)
    mem_regno1 = IntegerField(null=False)
    mem_mail = CharField(max_length=30)
    mem_add1 = CharField(max_length=100)
    mem_add2 = CharField(max_length=80)
    mem_hp = CharField(max_length=11, null=False)
    class Meta:
        db_table = "member"
        app_label = "jeapp"
        managed = False
        
class Marina(models.Model):
    mar_nm = CharField(primary_key=True, max_length=30, null=False)
    mar_add1 = CharField(max_length=100, null=False)
    mar_add2 = CharField(max_length=80, null=False)
    mar_lat = FloatField(null=False)
    mar_lon = FloatField(null=False)
    class Meta:
        db_table = "marina"
        app_label = "jeapp"
        managed = False
        
class Schedule(models.Model):
    sch_no = BigIntegerField(primary_key=True, null=False)
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
    book_no = BigIntegerField(primary_key=True, null=False)
    book_mem = CharField(max_length=30, null=False)
    book_qty = IntegerField(null=False)
    book_price = IntegerField(null=False)
    book_schedule = BigIntegerField(null=False)
    class Meta:
        db_table = "booking"
        app_label = "jeapp"
        managed = False

class Service(models.Model):
    ser_mar = models.CharField(max_length=30, null=False)
    ser_gu = models.CharField(max_length=10, null=False)
    ser_group = models.CharField(max_length=50, null=False)
    ser_nm = models.CharField(primary_key=True, max_length=50, null=False)
    ser_img = models.CharField(max_length=300, null=False)
    ser_distance = models.IntegerField(null=False)
    ser_url = models.CharField(max_length=100, null=False)
    ser_lat = models.FloatField(null=False)
    ser_lon = models.FloatField(null=False)
    class Meta:
        db_table = "service"
        app_label = "jeapp"
        managed = False

class Traffic(models.Model):
    tra_mar = CharField(max_length=30, null=False)
    tra_id = CharField(max_length=5, primary_key=True)
    tra_nm = CharField(max_length=50, null=False)
    tra_lat = models.FloatField(null=False)
    tra_lon = models.FloatField(null=False)
    tra_dis = models.FloatField(null=False)
    class Meta:
        db_table = "traffic"
        app_label = "jeapp"
        managed = False
        
class Chatbot(models.Model):
    request = CharField(primary_key=True, max_length=1000, null=False)
    response = CharField(max_length=1000, null=False)

    class Meta:
        db_table = "chatbot"
        app_label = "jeapp"
        managed = False
        
class Businfo(models.Model):
    bus_index = CharField(max_length=5, primary_key=True, null=False)
    bus_stop = CharField(max_length=5)
    bus_no = CharField(max_length=10)
    bus_nm = CharField(max_length=50)
    bus_time = CharField(max_length=10)
    bus_remain= CharField(max_length=10)
    class Meta:
        db_table = "businfo"
        app_label = "jeapp"
        managed = False
        
class Busstop(models.Model):
    stop_id = CharField(max_length=5, primary_key=True)
    class Meta:
        db_table = "busstop"
        app_label = "jeapp"
        managed = False
        
class Boo_mem(models.Model):
    book_no = BigIntegerField(primary_key=True, null=False)
    book_qty = IntegerField(null=False)
    book_price = IntegerField(null=False)

    boo_mem1 = models.ForeignKey(Member, to_field="mem_id", db_column="book_mem", on_delete=models.PROTECT)
    boo_sch1 = models.ForeignKey(Schedule, to_field="sch_no", db_column="book_schedule", on_delete=models.PROTECT)

    class Meta:
        db_table = 'booking'
        app_label = "jeapp"
        managed = False