from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import connection

from employ.models import *


# Create your views here.

def get_employ_list(request):
    gender = request.GET.get('gender')
    first_name = request.GET.get('first_name')
    page_row = int(request.GET.get('page_row', 10))
    page = int(request.GET.get('page', 1))

    query = Employees.objects
    if first_name:
        query = query.filter(first_name=first_name)
    if gender:
        query = query.filter(gender=gender)
    query = query.all()

    # 分页
    paginator = Paginator(query, page_row)
    page_of_blogs = paginator.get_page(page)
    data = [elem.listJson() for elem in page_of_blogs.object_list]
    print(connection.queries)
    return JsonResponse({"data": data})


def get_department_employ_list(request):
    page_row = int(request.GET.get('page_row', 10))
    page = int(request.GET.get('page', 1))
    dept = request.GET.get('dept')
    query = DeptEmp.objects.filter(dept_no=dept).select_related("emp_no")
    # 这里使用分页器不能达到分页故使用手工分页
    # 使用一次select_related join操作 只查需要的字段

    startRow = (page - 1) * page_row  # 分页待优化
    endRow = page * page_row
    result = list(query.values('emp_no', 'emp_no__birth_date', 'emp_no__first_name', 'emp_no__last_name', 'emp_no__gender', 'emp_no__hire_date')[startRow:endRow])
    print(connection.queries)

    return JsonResponse({"data": result})
