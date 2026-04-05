from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("participants__username",)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "conversation", "sender", "content", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("content", "sender__username", "conversation__participants__username")
