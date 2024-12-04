from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = TodoItem
        fields = [
            'id', 'created_at', 'title', 'description', 
            'due_date', 'tags', 'status'
        ]
        read_only_fields = ['created_at']

    def create(self, validated_data):
        # Handle tags separately
        tags_data = validated_data.pop('tags', [])
        todo_item = TodoItem.objects.create(**validated_data)

        # Create or get existing tags and associate with todo item
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            todo_item.tags.add(tag)

        return todo_item

    def update(self, instance, validated_data):
        # Handle tags separately during update
        tags_data = validated_data.pop('tags', None)
        
        # Update other fields
        instance = super().update(instance, validated_data)

        # Update tags if provided
        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)

        return instance