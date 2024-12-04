from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled')
    ]

    # Timestamp: Auto-set and non-editable
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # Title: Mandatory with max length 100
    title = models.CharField(
        max_length=100, 
        validators=[
            MinLengthValidator(1, "Title cannot be empty"),
            MaxLengthValidator(100, "Title cannot exceed 100 characters")
        ]
    )

    # Description: Mandatory with max length 1000
    description = models.TextField(
        validators=[
            MinLengthValidator(1, "Description cannot be empty"),
            MaxLengthValidator(1000, "Description cannot exceed 1000 characters")
        ]
    )

    # Due Date: Optional
    due_date = models.DateField(null=True, blank=True)

    # Tags: Optional, Many-to-Many relationship
    tags = models.ManyToManyField(Tag, blank=True)

    # Status: Mandatory with predefined choices
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='OPEN'
    )

    def __str__(self):
        return self.title