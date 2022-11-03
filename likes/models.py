from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.


class Like(models.Model):
    """
    This is the like model, it is realted to 'owner' and post'
    'owner' is going to be the User instance and 'post' is
    going to be the post instance, 'unique_together' makes sure
    users can't like the same post twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="likes", on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
