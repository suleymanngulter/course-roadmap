"""
GET  = formu göster
POST = formu kaydet, teşekkür sayfasına git
"""

from django.shortcuts import redirect, render

from .forms import MesajForm


def form_view(request):
    if request.method == "POST":
        #? request.POST: kutulara yazılanlar
        form = MesajForm(request.POST)
        if form.is_valid():
            form.save()
            #? redirect: yenileyince formu tekrar göndermesin
            return redirect("iletisim:tesekkur")
    else:
        form = MesajForm()  #? boş form
    return render(request, "iletisim/form.html", {"form": form})


def tesekkur(request):
    return render(request, "iletisim/tesekkur.html")
