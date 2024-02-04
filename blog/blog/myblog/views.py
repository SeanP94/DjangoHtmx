from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomeView(ListView):
    model = Post
    # template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10
    def get_template_names(self):
        is_htmx = self.request.headers.get('HX-Request') != None
        print(is_htmx, self.request.headers.get('HX-Request'))
        if is_htmx:
            print('succ')
            return "components/post-list-elements.html"
        print('fuc a ')
        return "blog/index.html"
