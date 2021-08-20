#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'xiaoqiao99'

from django.urls import path
from employ import views

urlpatterns = [
    path('', views.get_employ_list, name='employ_lis'), # 搜索员工表
    path('departments/', views.get_department_employ_list, name='department_employ_lis'),
]
