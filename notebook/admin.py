from django.contrib import admin
from .models import Post

# Register your models here.
# 관리자 페이지에서 만든 모델을 보려면
# admin.site.register(Post)로 모델을 등록
admin.site.register(Post)