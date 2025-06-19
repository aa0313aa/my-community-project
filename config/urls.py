# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import product_list, giftshop, customer, cart, postpay, 머니트리, 모빌, 네이버, 토스

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    
    # 각 앱의 주소록을 포함(include)
    path('board/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('summernote/', include('django_summernote.urls')),
    
    # 대문 페이지 ('')는 products 앱의 index 뷰가 담당
    path('', product_list, name='index'),
    path('giftshop/', giftshop, name='giftshop'),
    path('cart/', cart, name='cart'),
    path('customer/', customer, name='customer'),
    path('postpay/', postpay, name='postpay'),
    path('머니트리/', 머니트리, name='머니트리'),
    path('모빌/', 모빌, name='모빌'),
    path('네이버/', 네이버, name='네이버'),
    path('토스/', 토스, name='토스'),
]

# 개발 환경(DEBUG=True)에서 미디어/스태틱 파일 서빙 설정
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)