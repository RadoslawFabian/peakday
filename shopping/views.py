from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingCategory, ShoppingItem

def shopping_list(request):
    categories = ShoppingCategory.objects.all()
    return render(request, "shopping/shopping_list.html", {"categories": categories})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get("category_name")
        if name:
            ShoppingCategory.objects.create(name=name)
    return redirect("shopping_list")

def delete_category(request, category_id):
    category = get_object_or_404(ShoppingCategory, id=category_id)
    category.delete()
    return redirect("shopping_list")

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("item_name")
        quantity = request.POST.get("item_quantity", 1)
        category_id = request.POST.get("category_id")
        category = ShoppingCategory.objects.get(id=category_id)
        ShoppingItem.objects.create(name=name, quantity=quantity, category=category)
    return redirect("shopping_list")

def delete_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.delete()
    return redirect("shopping_list")

def toggle_purchased(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.purchased = not item.purchased
    item.save()
    return redirect("shopping_list")
