from django.shortcuts import get_object_or_404, render


from .models import BlogPost

# Create your views here.
def All_blogs(request):


    all_Blogs = BlogPost.objects.all()

    return render(request,'blog/index.html',{'showBlogs': all_Blogs})


def Detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)

    return render(request,'blog/detail.html',{'blog': blog})
