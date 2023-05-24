from django.urls import path
from . import views

urlpatterns = [
    path('free/', views.free_article),
    path('free/<int:article_pk>', views.free_detail),
    path('together/', views.together_article),    
    path('together/<int:article_pk>/', views.together_detail),
    
    # 댓글 추가
    path('together/<int:article_pk>/comment/', views.together_comment),
    path('free/<int:article_pk>/comment/', views.free_comment),

    # 삭제, 수정하려고 추가한 코드
    path('together/<int:article_pk>/<int:comment_pk>/', views.together_comment_detail),
    path('free/<int:article_pk>/<int:comment_pk>/', views.free_comment_detail),
]