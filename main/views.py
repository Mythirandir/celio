from django.shortcuts import render


def homepage(request):
    return render(request=request,
                  template_name="index.html",
                  )


def blog(request):
    return render(request= request,
                  template_name="blog.html",
                  )


def cart(request):
    return render(request= request,
                  template_name="cart.html",
                  )


def category(request):
    return render(request= request,
                  template_name="category.html",
                  )


def checkout(request):
    return render(request= request,
                  template_name="checkout.html",
                  )


def confirmation(request):
    return render(request= request,
                  template_name="confirmation.html",
                  )


def contact(request):
    return render(request= request,
                  template_name="contact.html",
                  )


def singleblog(request):
    return render(request= request,
                  template_name="single-blog.html",
                  )


def singleproduct(request):
    return render(request= request,
                  template_name="single-product.html",
                  )


def tracking(request):
    return render(request= request,
                  template_name="tracking.html",
                  )
