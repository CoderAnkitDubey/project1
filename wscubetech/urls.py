"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import: 
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('course/', views.course,name='course'),
    path('course/<courseid>', views.coursedetail),
    path('index/',views.index,name='index'),
    path('userform/',views.userform),
    path('userreg/',views.userreg),
    path('submit/',views.submit ,name="submit"),
    path('calc/',views.calc ,name="calc"),
    path('marksheet/',views.marksheet,name="marksheet"),
    path('evenodd/',views.evenodd,name="evenodd"),
    path('calculator/',views.calculator,name="calculator"),
]





