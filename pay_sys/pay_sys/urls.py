
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from payroll.views import StaffViewset, OvertimeViewset,Advance_paidViewset, DeductionsViewset, ScheduleViewset, PayrollsViewset, CurrencyViewset


router = routers.DefaultRouter()
router.register(r'staff', StaffViewset, 'staff')
router.register(r'overtime', OvertimeViewset, 'overtime')
router.register(r'advance', Advance_paidViewset, 'advance')
router.register(r'deductions', DeductionsViewset, 'deductions')
router.register(r'payroll', PayrollsViewset, 'payroll')
router.register(r'currency', CurrencyViewset, 'currency')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework'))
]
