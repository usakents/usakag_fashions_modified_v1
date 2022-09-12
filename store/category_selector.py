from .models import(Product)

def get_bags(productId):
    return Product.objects.get(pk=productId)