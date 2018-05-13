# -*- coding: utf-8 -*-

class DAY_OF_WEEK(object):
    """ 수업 요일 """
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    DISPLAY = {
        MON: u"월",
        TUE: u"화",
        WED: u"수",
        THU: u"목",
        FRI: u"금",
        SAT: u"토",
        SUN: u"일",
    }
    CHOICES = (
        (MON, u"월"),
        (TUE, u"화"),
        (WED, u"수"),
        (THU, u"목"),
        (FRI, u"금"),
        (SAT, u"토"),
        (SUN, u"일"),
    )

class CLASS_ROOM(object):
    """ 강의실 """
    NO1 = 1
    NO2 = 2
    NO3 = 3

    DISPLAY = {
        NO1: u"강의실1",
        NO2: u"강의실2",
        NO3: u"강의실3",
    }
    CHOICES = (
        (NO1, u"강의실1"),
        (NO2, u"강의실2"),
        (NO3, u"강의실3"),
    )