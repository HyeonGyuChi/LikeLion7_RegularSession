from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) : 
        return self.title

    def summary(self):
        if len(self.content) >= 43 :
            return self.content[:43] + str("…")
        else :
            return self.content