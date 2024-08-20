from django.db import models

class ChatMessage(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tagged_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.username}: {self.message[:20]}'

