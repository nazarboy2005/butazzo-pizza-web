from django.views.generic import TemplateView

from pages.models import PicturesModel, ScrollModel
from products.models import ProductsModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pizza = ProductsModel.objects.filter(category__name='Pizza')
        salads = ProductsModel.objects.filter(category__name='Salad')
        burgers = ProductsModel.objects.filter(category__name='Burgers')
        drinks = ProductsModel.objects.filter(category__name='Drinks')
        fries = ProductsModel.objects.filter(category__name='Fries')

        images = PicturesModel.objects.all()
        discounted_products = ScrollModel.objects.all()[:5]

        context = {
            'fries': fries,
            'drinks': drinks,
            'burgers': burgers,
            'salads': salads,
            'pizza': pizza,

            'images': images,
            'discounted_products':discounted_products,
        }
        return context
