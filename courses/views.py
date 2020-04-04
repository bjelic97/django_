from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course
from .forms import CourseModelForm



class CourseObjectMixin(object):
    model = Course
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


#raw create view

class CourseCreateView(View):
    template_name = "courses/course_create.html"
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {"form": form}        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}        
        return render(request, self.template_name, context)


#raw update view

class CourseUpdateView(View):
    template_name = "courses/course_update.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):       
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form        
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form   
        return render(request, self.template_name, context)



#raw delete view

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"
    def get(self, request, id=None, *args, **kwargs):       
        context = {}
        obj = self.get_object()
        if obj is not None:        
            context['object'] = obj     
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

#raw list view


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, id=None, *args, **kwargs):
        return render(request,self.template_name, {'object_list': self.get_queryset()})


class MyListView(CourseListView):
    queryset = Course.objects.filter(id=1)          

# base view class = view
class CourseView(View):
    template_name = "courses/course_detail.html"
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


#function-based views

def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})