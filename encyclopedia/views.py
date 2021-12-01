from django.core.exceptions import ValidationError
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import markdown2
import random

from . import util
from .forms import EditForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    return render(request, "encyclopedia/entry.html", {
       "title": title,
       "entry": markdown2.markdown(util.get_entry(title)) 
    })

def newpage(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
                title = form.cleaned_data["title"]
                content = form.cleaned_data["content"]

                if title in util.list_entries():
                    return render(request, "encyclopedia/error.html")

                util.save_entry(title, content)
                return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "entry": markdown2.markdown(util.get_entry(title)) 
                })
                
    else:
        form = EditForm()

        return render(request, "encyclopedia/newpage.html", {
        "form": form
        })         

def search(request):
    if request.method == "POST":
        # put search value in variable
        search_value = request.POST["q"]
        search_substring = [entry for entry in util.list_entries() if search_value in entry]
        if search_value.lower() in (entry.lower() for entry in util.list_entries()):
            # store original title in variable
            title = [entry for entry in util.list_entries() if entry.lower() == search_value.lower()][0]
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "entry": markdown2.markdown(util.get_entry(search_value))
            })

        return render(request, "encyclopedia/search_results.html", {
            "search_value": search_value,
            "entries": search_substring
        })
