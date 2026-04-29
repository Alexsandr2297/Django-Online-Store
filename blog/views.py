from django.urls import reverse_lazy, reverse

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        # Фильтруем статьи, у которых признак публикации равен True
        return Blog.objects.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.quantity_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("heading", "content", "picture", "publication_attribute", "quantity_views")
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog_form.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("heading", "content", "picture", "publication_attribute", "quantity_views")
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog_form.html'

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')

