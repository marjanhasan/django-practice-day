from django.db import models

# Create your models here


class Practice_Model(models.Model):
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to="files/")
    file_path_field = models.FilePathField(path="/path/to/files/")
    float_field = models.FloatField()
    image_field = models.ImageField(upload_to="images/")
    integer_field = models.IntegerField()
    slug_field = models.SlugField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
