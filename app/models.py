# -*- coding: utf-8 -*-
import os
from django.db import models
from app import configs

def profile_upload_path(instance, filename):
    return os.path.join('profile', filename)

def gallery_upload_path(instance, filename):
    return os.path.join('gallery', filename)

class Teacher(models.Model):
    """ 강사 정보 """
    profile_image = models.FileField(u"프로필사진", upload_to=profile_upload_path)
    name = models.CharField(u"이름", max_length=32)
    introduce = models.TextField(u"소개")
    display_order = models.PositiveIntegerField(u"노출순서", default=0)
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    class Meta:
        ordering = ['display_order']

class Timetable(models.Model):
    """ 수업 시간표 """
    name = models.CharField(u"수업명", max_length=32)
    day_of_week = models.PositiveSmallIntegerField(
        u"요일", choices=configs.DAY_OF_WEEK.CHOICES)
    class_room = models.PositiveSmallIntegerField(
        u"강의실", choices=configs.CLASS_ROOM.CHOICES)
    start_time = models.FloatField(u"시작시간", help_text=u"11부터 21까지. 오후 3시 30분이면, 15.5")
    end_time = models.FloatField(u"종료시간", help_text=u"11부터 21까지. 예) 오후 3시 30분 => 15.5")
    color = models.CharField(
        u"컬러코드", max_length=9, help_text=u"#을 포함한 색상 코드. 예) 빨간색 => #ff0000")
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    class Meta:
        ordering = ['day_of_week', 'class_room']

    def get_item_left(self):
        return (self.start_time - 11) * 90;

    def get_item_width(self):
        return (self.end_time - self.start_time) * 90;

class CommonInfo(models.Model):
    """ 일반 정보들 """
    community_text = models.TextField(u"커뮤니티 텍스트")
    naver_text = models.TextField(u"네이버카페 텍스트")
    instagram_text = models.TextField(u"인스타그램 텍스트")
    facebook_text = models.TextField(u"페이스북 텍스트")
    timetable_text = models.TextField(u"수업시간표 텍스트")

class Gallery(models.Model):
    """ 사진 갤러리 """
    photo = models.FileField(u"사진", upload_to=gallery_upload_path)
    display_order = models.PositiveIntegerField(u"노출순서", default=0)
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    class Meta:
        ordering = ['display_order']
