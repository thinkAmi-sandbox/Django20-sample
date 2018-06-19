"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # for Django 1.8
    # url('myapp/', include('myapp.urls', namespace='my')),
    # path('old/', include('myapp.urls', namespace='old')),  # NG

    # for Django 2.0
    # アプリのurls.pyに app_name 設定があるパターン
    path('with/', include('myapp.urls_with_app_name')),

    # アプリのurls.pyには app_name 設定がなく、includeの引数をタプルにして名前空間を渡すパターン
    # (urlpatternsのあるモジュール, 名前空間)
    path('without/', include(('myapp.urls_without_app_name', 'without'))),

    # アプリのurls.pyに app_name 設定があるが、名前空間を別に用意するパターン
    path('over/', include('myapp.urls_overwrite_app_name', namespace='replaced')),
    # アプリのurls.pyの app_name 設定をそのまま使うパターン(再掲)
    path('not_over/', include('myapp.urls_overwrite_app_name')),
]
