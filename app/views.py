from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Teacher, Timetable, CommonInfo, Gallery

class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all()
        context['timetables'] = Timetable.objects.all()
        context['commoninfo'] = CommonInfo.objects.first()
        gallerylist = Gallery.objects.all()
        galleries = [[],[],[]]
        i = 0
        for gallery in gallerylist:
            galleries[i].append(gallery)
            i = (i+1) % 3
        context['galleries'] = galleries
        return context
