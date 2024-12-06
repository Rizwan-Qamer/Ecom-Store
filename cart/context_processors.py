from .cart import *


# Create context processor so our cart can work on all pages of the site
def cart(request):
    # Return the default data from out cart
    return {'cart': Cart(request)}