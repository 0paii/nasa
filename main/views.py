from django.views.generic import TemplateView
from common.views import TitleMixin
from main.models import SortableCarousel


# Create your views here.
class IndexView(TitleMixin, TemplateView):
    template_name = 'main.html'
    title = 'Nasa'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['images'] = SortableCarousel.objects.all()
        return context
