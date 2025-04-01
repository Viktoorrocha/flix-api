from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, message="A avaliação não pode ser inferior a 0 estrelas"),
            MaxValueValidator(5, message="A avaliação não pode ser superior a 5 estrelas")
        ]
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.user} para {self.movie}"
