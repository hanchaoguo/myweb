# coding=utf8
from django.views.generic  import  ListView, DetailView
from django.db.models import Q
from django.http  import JsonResponse, HttpResponseRedirect,QueryDict
from django.core.urlresolvers import reverse 
from django.shortcuts import render
#from pure_pagination.mixins import PaginationMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
#from books.models import Publish, Author, Book
from models import Licience,Zyid
from forms import LicienceForm,ZyidForm


import json
#import logging
#logger = logging.getLogger('opsweb')

#class LicienceListView(LoginRequiredMixin, PaginationMixin, ListView):
class LicienceListView(LoginRequiredMixin,ListView):
    '''
    动作：getlist, create
    '''
    model = Licience
    template_name =  "books/book_list.html"
    context_object_name = "book_list"
    print context_object_name
    paginate_by = 3
    keyword = ''

    def get_queryset(self):
        queryset = super(LicienceListView, self).get_queryset()
        self.keyword = self.request.GET.get('keyword', '').strip()
        print self.keyword
        if self.keyword:
            queryset = queryset.filter(Q(ProductName = self.keyword)|
                                       Q(LicienceClass = self.keyword)|
                                       Q(AccountName =self.keyword))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LicienceListView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        #context['authors']=Author.objects.all()
        #context['publishs']=Publish.objects.all()
        return context

    
    def post(self, request):
        form = LicienceForm(request.POST)
        if form.is_valid():
            form.save()
            res = {'code':0,'result': '添加Licience成功'}
        else:
            # form.errors会把验证不通过的信息以对象的形式传到前端，前端直接渲染即可
            res = {'code':1,'errmsg':form.errors}
            print form.errors   
        return JsonResponse(res,safe=True)

    def delete(self, request, *args,  **kwargs):
        webdata = QueryDict(request.body).dict()
        pk =webdata.get("id")
        # 通过出版社对象查所在该出版社的书籍，如果有关联书籍不可以删除，没有关联书籍可以删除
        try:
            #obj = self.model.objects.get(pk=pk)
            #if not obj.book_set.all():
            self.model.objects.filter(pk=pk).delete()
            res = {"code":0,"result":"删除Licicene成功"}
            #else:
            #    res = {"code":1,"errmsg":"该出版社有关联书籍,请联系管理员"}
        except:
            res = {"code":1,"errmsg":"删除错误请联系管理员"}
        return JsonResponse(res,safe=True)



    def put(self, request,**kwargs):
        res = {'code':0}
        webdata = QueryDict(request.body).dict()
        pk = kwargs.get('pk')

        #通过publishid  获取publish对象
        publishid = webdata.get('publish')
        Publishobj = Publish.objects.get(id=publishid)

        #重新赋值publish对象,通过bookid更新书籍信息
        webdata['publish'] = Publishobj
        try:
            self.model.objects.filter(pk=pk).update(**webdata)
        except Basemodel as e:
            res['code'] = 1
            res['error'] = "修改错误请联系管理员"
        return JsonResponse(res)


class ResourcesListView(LoginRequiredMixin,ListView):
    '''
    动作：getlist, create
    '''
    model = Zyid
    template_name =  "books/resources_list.html"
    #上下文环境变量
    context_object_name = "book_list"
    print context_object_name
    paginate_by = 5
    keyword = ''


    def post(self, request):
        form = ZyidForm(request.POST)
        if form.is_valid():
            form.save()
            res = {'code':0,'result': '添加成功'}
        else:
            # form.errors会把验证不通过的信息以对象的形式传到前端，前端直接渲染即可
            res = {'code':1,'errmsg':form.errors}
            print form.errors
        return JsonResponse(res,safe=True)

    def delete(self, request, *args,  **kwargs):
        webdata = QueryDict(request.body).dict()
        pk = webdata.get('id')
        # 通过出版社对象查所在该出版社的书籍，如果有关联书籍不可以删除，没有关联书籍可以删除
        try:
            #obj = self.model.objects.get(pk=pk)
            #if not obj.book_set.all():
            self.model.objects.filter(pk=pk).delete()
            res = {"code":0,"result":"删除资源ID成功"}
            #else:
            #    res = {"code":1,"errmsg":"该出版社有关联书籍,请联系管理员"}
        except:
            res = {"code":1,"errmsg":"删除错误请联系管理员"}
        return JsonResponse(res,safe=True)





#class BookDetailView(LoginRequiredMixin,DetailView):
    '''
    动作：getone, update, delete
    '''
#    model = Book
#    template_name = "books/book_detail.html"
#    context_object_name = 'book'
#    next_url = '/books/booklist/'

#    def get_context_data(self, **kwargs):
#        context = super(BookDetailView, self).get_context_data(**kwargs)
#        context['authors']=Author.objects.all()
#        context['publishs']=Publish.objects.all()
#        context['author_list']=self.get_book_authors()
#        return context

#    def post(self, request, *args, **kwargs):
#        pk = kwargs.get('pk')
#        p = self.model.objects.get(pk=pk)
#	form = BookForm(request.POST, instance=p)
#        if form.is_valid():
#	    form.save()
#            res = {"code":0,"result":"更新出版商成功", 'next_url':self.next_url}
#        else:    
#            res = {"code":1,"errmsg":form.errors,'next_url':self.next_url}
#        return render(request,settings.JUMP_PAGE,res) 
        # return HttpResponseRedirect(reverse('books:publish_detail',args=[pk]))
 
#    def delete(self, request, *args,  **kwargs):
#        pk = kwargs.get('pk')
        # 通过出版社对象查所在该出版社的书籍，如果有关联书籍不可以删除，没有关联书籍可以删除
#        try:
            #obj = self.model.objects.get(pk=pk)
            #if not obj.book_set.all():
#            self.model.objects.filter(pk=pk).delete()
#            res = {"code":0,"result":"删除出版商成功"}
            #else:
            #    res = {"code":1,"errmsg":"该出版社有关联书籍,请联系管理员"}
#        except:
#            res = {"code":1,"errmsg":"删除错误请联系管理员"}
#        return JsonResponse(res,safe=True)

