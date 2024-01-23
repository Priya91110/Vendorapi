from django.contrib import admin
from django.urls import path
from vendorapp import views
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('vendors/', views.getpostvendor.as_view()),
    path('vendors/<int:pk>', views.getputdelete.as_view()),
    path('purchase_orders/', views.PurchaseListCreate.as_view()),
    path('purchase_orders/<int:pk>', views.PurchaseDetailView.as_view()),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
]
