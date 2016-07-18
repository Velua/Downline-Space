from django.shortcuts import render

# Create your views here.
from .models import Post

def blog_list(request):


	queryset = Post.objects.all()

	context = {

		"posts" : queryset,

	}

	return render(request, "blog_list.html", context)