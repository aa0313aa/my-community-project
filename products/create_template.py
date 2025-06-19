import os

# 생성할 경로
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates', 'products')
os.makedirs(template_dir, exist_ok=True)

# 템플릿 파일 경로
template_path = os.path.join(template_dir, 'product_list.html')

# 템플릿 내용
template_content = """{% extends 'base.html' %}

{% block content %}
<div class="container my-5">
    <div class="text-center mb-5">
        <h1 class="display-4 fw-bold">기프트샵</h1>
        <p class="lead text-muted">휴대폰결제, 카드결제로 간편하게 구매하세요.</p>
    </div>

    <div class="row row-cols-1 row-cols-md-3 g-4">
        {% for product in products %}
        <div class="col">
            <div class="card h-100 shadow-sm">
                {% if product.image %}
                    <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}" style="height: 200px; object-fit: cover;">
                {% else %}
                    <div class="d-flex justify-content-center align-items-center card-img-top bg-light" style="height: 200px;">
                        <span class="text-muted">No Image</span>
                    </div>
                {% endif %}
                <div class="card-body">
                    <h5 class="card-title">{{ product.name }}</h5>
                    <p class="card-text text-muted small">{{ product.description|truncatewords:15 }}</p>
                </div>
                <div class="card-footer text-center">
                    <span class="fw-bold fs-5">{{ product.price }}원</span>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
"""

# 파일 생성
with open(template_path, 'w', encoding='utf-8') as f:
    f.write(template_content)

print(f"템플릿 파일이 생성되었습니다: {template_path}")