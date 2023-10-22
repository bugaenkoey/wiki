from django import forms
from django.shortcuts import render
import markdown2

from . import util

class NewArticleForm(forms.Form ):
    
    # def __init__(self, title_txt="", article_txt=""):
    #     self.title_txt = title_txt
    #     self.article_txt = article_txt

        title = forms.CharField(initial = "", label= "Title", min_length=1)
        article = forms.CharField(initial = "", label="Article text", widget=forms.Textarea(), min_length=5)


    # birth_year = forms.DateField(
    #     widget=forms.SelectDateWidget(years=["1980", "1981", "1982"])
    # )
    


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request,title):
    return render(request,"encyclopedia/get_entry.html", {
        "get_entry":markdown2.markdown( util.get_entry(title))
        ,"title":title
        ,"entries": util.list_entries()
    })

def random_page(request):
       return get_entry(request,util.random_page())

def  search(request):
    title = request.GET.get("q")
    print(f"===+====>> {title}")
    return render(request, "encyclopedia/index.html", {
        "entries":util.search(title)
     })

def create_new_page(request,title="",article=""):
    print("create_new_page")
    form = NewArticleForm({"title" : title,"article":article})
    form.title = title
    form.article = article
    print(f"++++++++-{form.data['title']}-+++++++++{form.title}&{title}#{article[:50]}")
    # print(f"{form.cleaned_data}") 
    return render(request,"encyclopedia/create_new_page.html",{
          "form": form
     }) 

     
def add(request):
     print("*****add****")
     if request.method=="POST":
        print("POST")
        form = NewArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            article = form.cleaned_data["article"]
            print(f"{title} = {form.cleaned_data['title']}")
            try:
                util.save_entry(title,article)

            except Exception as ex:
                print(ex)
                return create_new_page(request,title,article)

                # return render(request,"encyclopedia/create_new_page.html",{
                #     "exception": ex,
                    # "form":form
                    # "form": NewArticleForm(request.POST,title,article)

                    # })
            # finally:
            #     print("The 'try except' is finished")
            
            print("SAVE_____")
            return get_entry(request,title)
        else:return create_new_page(request)


def edit_page(request,title="",article=""):
    if request.method=="POST":
        print("POST-E")
        form = NewArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            # article = form.cleaned_data["article"]
            print(f"edit_page {title}")
            print(request)

            content = util.get_entry(title)
            form = NewArticleForm({"title" : title,"article":content})
            form.title = title
            form.article = content
            print(f"---------{form.data['title']}-----------{form.title}&{title}#{article[:50]}")
            # print(f"{form.cleaned_data}") 
            return render(request,"encyclopedia/edit_page.html",{
                "form": form
            }) 


def seve_edit(request):
     if request.method=="POST":
        print("POST")
        form = NewArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            article = form.cleaned_data["article"]
            print(f"{title} = {form.cleaned_data['title']}")
            util.save_edit(title,article)
            return get_entry(request,title)