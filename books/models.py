from django.db import models


class Books(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('science_fiction', 'Science Fiction'),
        ('biography', 'Biography'),
    ]

    name = models.CharField(max_length=255, verbose_name='Enter book name')
    photo = models.ImageField(upload_to='post/', verbose_name='Upload picture')
    author = models.CharField(max_length=255, verbose_name='Author of book')
    description = models.TextField(verbose_name='Book description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price of book')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name='Book genre')
    publisher = models.CharField(max_length=255, verbose_name='Publisher of book')
    publication_date = models.DateField(verbose_name='Publication date')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def __str__(self):
        return f'{self.name} - {self.create_at}'