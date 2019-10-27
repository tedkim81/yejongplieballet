# -*- coding: utf-8 -*-
import os
from django.db import models
from app import configs

def intro_upload_path(instance, filename):
    return os.path.join('intro', filename)

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

class ClassInfo(models.Model):
    """ 수업 정보 """
    name = models.CharField(u"수업명", max_length=32)
    introduce = models.TextField(u"소개")
    color = models.CharField(
        u"컬러코드", max_length=9, help_text=u"#을 포함한 색상 코드. 예) 빨간색 => #ff0000")
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    """ 수업 시간표 """
    classinfo = models.ForeignKey("ClassInfo", on_delete=models.CASCADE, verbose_name=u"수업")
    day_of_week = models.PositiveSmallIntegerField(
        u"요일", choices=configs.DAY_OF_WEEK.CHOICES)
    class_room = models.PositiveSmallIntegerField(
        u"강의실", choices=configs.CLASS_ROOM.CHOICES)
    start_time = models.FloatField(u"시작시간", help_text=u"11부터 21까지. 오후 3시 30분이면, 15.5")
    end_time = models.FloatField(u"종료시간", help_text=u"11부터 21까지. 예) 오후 3시 30분 => 15.5")
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    class Meta:
        ordering = ['day_of_week', 'class_room']

    def get_item_left(self):
        return (self.start_time - 11); # 단위width 곱하는것은 템플릿에서

    def get_item_width(self):
        return (self.end_time - self.start_time); # 단위width 곱하는것은 템플릿에서

class CommonInfo(models.Model):
    """ 일반 정보들 """
    intro_image = models.FileField(u"첫화면배경이미지", blank=True, null=True, upload_to=intro_upload_path)
    about_text = models.TextField(u"ABOUT 텍스트", blank=True, null=True)
    about_link_m = models.URLField(u"학원소개더보기 링크(모바일)", max_length=500, blank=True, null=True)
    about_link_pc = models.URLField(u"학원소개더보기 링크(PC)", max_length=500, blank=True, null=True)
    teachers_link_m = models.URLField(u"강사소개더보기 링크(모바일)", max_length=500, blank=True, null=True)
    teachers_link_pc = models.URLField(u"강사소개더보기 링크(PC)", max_length=500, blank=True, null=True)
    timetable_text = models.TextField(u"수업시간표 텍스트", blank=True, null=True)
    class_link_1 = models.URLField(u"전공반 안내링크", max_length=500, blank=True, null=True)
    class_link_2 = models.URLField(u"어린이취미반 안내링크", max_length=500, blank=True, null=True)
    class_link_3 = models.URLField(u"성인취미반 안내링크", max_length=500, blank=True, null=True)
    location_text = models.TextField(u"LOCATION 텍스트", blank=True, null=True)
    contact_text = models.TextField(u"CONTACT 텍스트", blank=True, null=True)
    notice_link_m = models.URLField(u"공지사항 링크(모바일)", max_length=500, blank=True, null=True)
    notice_link_pc = models.URLField(u"공지사항 링크(PC)", max_length=500, blank=True, null=True)
    cs_link_m = models.URLField(u"온라인상담실 링크(모바일)", max_length=500, blank=True, null=True)
    cs_link_pc = models.URLField(u"온라인상담실 링크(PC)", max_length=500, blank=True, null=True)
    navercafe_link = models.URLField(u"네이버카페 링크", max_length=500, blank=True, null=True)
    instagram_link = models.URLField(u"인스타그램 링크", max_length=500, blank=True, null=True)
    facebook_link = models.URLField(u"페이스북 링크", max_length=500, blank=True, null=True)
    vdenie_link = models.URLField(u"브이데니에 링크", max_length=500, blank=True, null=True)
    sungnamvallet_link = models.URLField(u"성남시티발레단 링크", max_length=500, blank=True, null=True)
    foreigner_text = models.TextField(u"FOREIGNER 텍스트", blank=True, null=True)
    footer_text = models.TextField(u"FOOTER 텍스트", blank=True, null=True)

class Gallery(models.Model):
    """ 사진 갤러리 """
    photo = models.FileField(u"사진", upload_to=gallery_upload_path)
    display_order = models.PositiveIntegerField(u"노출순서", default=0)
    pub_date = models.DateTimeField(u"등록일", auto_now_add=True)

    class Meta:
        ordering = ['display_order']
