from django.shortcuts import render
from community.forms import *


# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # database에 저장한다.
            # django framework를 써서 굉장히 단순해짐(sql을 직접 명시하지 않아도 됨)
            form.save()
            form = Form()
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})


def list(request):
    # Article이라는 이름으로 등록된 데이터베이스를 모두 가져온다.
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList': articleList})


def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {"article": article})
