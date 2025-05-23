from django.urls import path
from . import views

urlpatterns = [
    path("", views.shopping_list, name="shopping_list"),
    path("add_category/", views.add_category, name="add_category"),
    path("delete_category/<int:category_id>/", views.delete_category, name="delete_category"),
    path("add_item/", views.add_item, name="add_item"),
    path("delete_item/<int:item_id>/", views.delete_item, name="delete_item"),
    path("toggle_purchased/<int:item_id>/", views.toggle_purchased, name="toggle_purchased"),
]
