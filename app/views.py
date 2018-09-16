from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Teacher, ClassInfo, Timetable, CommonInfo, Gallery

class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all()
        context['timetables'] = Timetable.objects.all()
        context['classinfos'] = ClassInfo.objects.all()
        context['commoninfo'] = CommonInfo.objects.first()
        gallerylist = Gallery.objects.all()
        galleries = [[],[],[]]
        galleries_size = [0, 0, 0]
        for i in range(gallerylist.count()):
            galleries_size[i%3] += 1
        i1 = 0
        i2 = 0
        for gallery in gallerylist:
            galleries[i1].append(gallery)
            i2 += 1
            if i2 == galleries_size[i1]:
                i1 += 1
                i2 = 0
        context['galleries'] = galleries
        return context
