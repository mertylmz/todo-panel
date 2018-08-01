from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post, Personel
from .forms import PostForm
from django.core import serializers

def post_personel(request, ids):

    personels = []
    for id in ids.split(","):
        personel = get_object_or_404(Personel, id=id)
        personels.append(personel.post_set.all())
    ctx = {
        'posts': personels
    }
    return render(request, 'post/personel.html', ctx)


def post_personel_ajax(request, id):
    personel = get_object_or_404(Personel, id=id)
    posts = personel.post_set.all()
    ctx = {
        'personel': personel,
        'posts': posts
    }
    data = serializers.serialize("json", posts)
    return HttpResponse(data, content_type='text/json')


def post_index(request):

    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts':posts})


def post_detail(request, id):
    posts = get_object_or_404(Post, id=id)
    context = {
        'post': posts,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # post = form.save(commit='False')
            # post.slug = slugify(post.title)
            # post.save()
            # return HttpResponseRedirect(post.get_absolute_url())
            return redirect('post:index')

    else:
        form = PostForm()
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post:index')

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_delete(request,  id):
    post = get_object_or_404(Post, id=id)
    post.delete()

    return redirect('post:index')



