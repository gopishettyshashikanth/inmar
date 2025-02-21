from django.urls import path
from . import views

urlpatterns = [
    
    path('api/v1/insert_metadata/', views.InsertMetaData.as_view(), name='metadata-insert'),
    path('api/v1/insert_skudata/', views.InsertSKUData.as_view(), name='skudata-insert'),

    path('api/v1/location/', views.AllLocationList.as_view(), name='All_Locations'),
    path('api/v1/create_metadata/', views.CreateMetaDataList.as_view(), name='metadata-create'),
    path('api/v1/location/<str:location_id>/department/', views.LocationList.as_view(), name='location'),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/', views.DepartmentList.as_view(), name='department'),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/<str:category_id>/subcategory/', views.CategoryList.as_view(), name='category'),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/<str:category_id>/subcategory/<str:subcategory_id>', views.SubCategoryList.as_view(), name='subcategory'),

    path('api/v1/update_metadata/<str:subcategory_id>/', views.SubCategoryList.as_view(), name='metadata-update'),
    path('api/v1/SKUdata/', views.SKUDataList.as_view(), name='skudata-match-list'),
]