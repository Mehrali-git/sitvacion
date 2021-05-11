from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect

# from blog.models import Articles

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields =["author","title","category","slug","description","thamnail","publish","is_special","status"]
        elif request.user.is_author:
            self.fields =["title","category","slug","description","thamnail","is_special","publish"]
        else:
            raise Http404("شما اجازه دسترسی به صفحه را ندارید")
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.author=self.request.user
            if not self.obj.status == 'i':
                self.obj.status = 'd'
        return super().form_valid(form)

# class AuthorAccessMixin():
#         def dispatch(self, request, pk ,*args, **kwargs):
#             article=get_object_or_404(Articles,pk=pk)
#             if article.author == request.user and article.status in ['b','d'] or request.user.is_superuser:
#                 return super().dispatch(request, *args, **kwargs)
#             else:
#                 redirect("login")


class NoAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')


class AuthorAccessMixin():
        def dispatch(self, request, pk, *args, **kwargs):
            article = get_object_or_404(Articles, pk=pk)
            if article.author == request.user and article.status in ['b', 'd'] or request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                redirect("login")


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دسترسی به صفحه را ندارید")
