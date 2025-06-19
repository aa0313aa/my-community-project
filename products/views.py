# products/views.py (수정 후)

from django.shortcuts import render, get_object_or_404
from .models import Product

# 상품 목록 뷰
def product_list(request):
    return render(request, 'products/index.html')

# 상품 상세 뷰
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# 정적 페이지들을 위한 뷰들
def giftshop(request):
    return render(request, 'products/giftshop.html')

def customer(request):
    return render(request, 'products/customer.html')

def 머니트리(request):
    return render(request, 'products/머니트리.html')

def cart(request):
    return render(request, 'products/cart.html')

def postpay(request):
    return render(request, 'products/postpay.html')

def 모빌(request):
    return render(request, 'products/모빌.html')

# products/views.py 파일 맨 아래에 추가

def 네이버(request):
    # 네이버.html 템플릿을 보여줍니다.
    return render(request, 'products/네이버.html')

def 토스(request):
    # 토스.html 템플릿을 보여줍니다.
    return render(request, 'products/토스.html')

def index(request):
    return render(request, 'products/index.html')