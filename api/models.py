from django.db import models


class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class VideosDetails(models.Model):
    class VIDEOS(models.TextChoices):
        MusicVideos = 'Music Videos'
        WebSeries = 'Web Series'
        Movies = 'Movies'
        Trailers = 'Trailers'
        Kids = 'Kids'
        Devotional = 'Devotional'

    # videosId = models.IntegerField(default=0 ,primary_key=True)
    image = models.ImageField(upload_to ='image/')
    titleImage = models.ImageField(upload_to ='titleImage/')
    thumbnailImage = models.ImageField(upload_to ='thumbnailImage/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    year = models.IntegerField(null=True)
    genre = models.CharField(null=True, max_length=100)
    # type = models.CharField(null=True, max_length=100)
    # Duration = models.CharField(max_length=100)
    type = models.CharField(
        max_length=12,
        choices=VIDEOS.choices,
        default=VIDEOS.MusicVideos,
    )
    trailer = models.FileField(upload_to='tailers/', null=True, verbose_name="Trailer")
    video = models.FileField(upload_to='videos/%y', null=True, verbose_name="Video")




class UserDetails(models.Model):
    userId = models.IntegerField(default=0 ,primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100 , unique=True)
    password = models.CharField(max_length=100)