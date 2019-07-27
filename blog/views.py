from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog, Comment
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail':details})


def create(request):
    # return HttpResponse('잘못된 접근입니다.')
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form': form} )


def edit(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+str(blog.id))
    return render(request, 'edit.html',{'blog':blog})

@login_required
def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')

@login_required
def comment_add(request, blog_id): #함수로 접근할때
    if request.method == "POST": # POST로 접근할때
        post = Blog.objects.get(pk=blog_id) # 1번게시글로 접근한때 1번으로 들어간다

        comment = Comment() 
        comment.user = request.user # 댓글작성자가 누구나 들어온 유저다
        comment.body = request.POST['body'] # 내용은 POST 메시지중 body부분을 넣어라
        comment.post = post
        comment.save()
        return redirect('/blog/'+ str(blog_id)) # 작성한 게시글 로 이동한다.
    else:
        return HttpResponse('잘못된 접근입니다!')

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user: # 댓글 수정버튼 누른 사용자가 댓글 작성자랑 일치할경우(접속한 유저가 댓글 작성자인지 유효성 검사)
        if request.method=="POST":
            comment.body = request.POST['body']
            comment.save()
            return redirect('/blog/' + str(comment.post.id)) #댓글에서, 게시글을 간뒤, 아이디를 달라 이말이야....
        elif request.method=="GET":
            context = {
                'comment' : comment
            }
            return render(request, 'comment_edit.html', context)
    else:
        return HttpResponse('사용자 아이디가 달라서 수정할 수 없어요.')

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        if request.method == "POST":
            post_id = comment.post.id
            comment.delete()
            return redirect('/blog/' + str(post_id))
    return HttpResponse('잘못된 접근입니다.')