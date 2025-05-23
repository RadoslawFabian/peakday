from django.db import models

class ShoppingCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="Unnamed Category")

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    purchased = models.BooleanField(default=False)
    category = models.ForeignKey(ShoppingCategory, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.name} ({self.quantity})"
