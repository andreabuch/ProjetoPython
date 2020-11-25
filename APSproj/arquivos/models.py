from django.db import models
from django.contrib.auth import get_user_model
class Arquivo(models.Model):

    STATUS = (
        ('rest', 'Restrito'),
        ('prot', 'Protegido'),
        ('publ', 'Publico')
    )
    title = models.CharField(max_length=255)
    descrição = models.TextField()
    categoria = models.CharField(
        max_length=4,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

