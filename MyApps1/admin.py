from django.contrib import admin
from MyApps1.models import Employees
from MyApps1.models import ProxyEmployees1
from MyApps1.models import ProxyEmployees2

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr'];
admin.site.register(Employees,EmployeesAdmin)

class ProxyEmployees1Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr'];
admin.site.register(ProxyEmployees1,ProxyEmployees1Admin)

class ProxyEmployees2Admin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']
admin.site.register(ProxyEmployees2,ProxyEmployees2Admin)