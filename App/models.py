from django.db import models
from django.db.models import Manager
from django.db import connection
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime
# from mapbox_location_field.models import LocationField
from ckeditor_uploader.fields import RichTextUploadingField


# ------------------------------------------------------------------------------------------------------------
# User[id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined]

# USER_TYPE = (
#     (1, "Subscriber"),
#     (2, "Admin"),
#     (3, "SuperAdmin")
# )
# models.IntegerField(choices=USER_TYPE, default=1)

# col_list = ['col1', 'col2', 'col3']
# Obj.objects.all().values_list(*col_list)

# class UserDetails(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     profile_image = models.ImageField(upload_to="Image/Profile/", blank=True)
#     dob = models.DateField(auto_now_add=True)
#     address = models.TextField(default="", blank=True)
#     phone = models.CharField(max_length=10, blank=True)
#     location = LocationField()
#     user_ip = models.GenericIPAddressField()
#     user_browser = models.CharField(max_length=100, default="")
#
#     objects = Manager()  # The default Manager
#
#     class Meta:
#         db_table = 'UserDetails'
# ------------------------------------------------------------------------------------------------------------


class Courses(models.Model):
    title = models.CharField(max_length=255, help_text="Topic Name")
    author = models.CharField(max_length=50, help_text="Author Name")
    tag = models.CharField(max_length=20, blank=False, help_text="Tag Name")
    created_at = models.DateTimeField(auto_now_add=True)
    question = RichTextUploadingField()
    solution = RichTextUploadingField()
    impression = models.IntegerField(default=0)

    class Meta:
        db_table = 'Courses'

    def __str__(self):
        return self.title


class Comments(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    message = RichTextUploadingField()
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField()
    user_browser = models.CharField(max_length=100, default="")
    location = models.TextField()

    class Meta:
        db_table = 'Comments'


class Screenshots(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="Course/Screenshot/", blank=True)

    class Meta:
        db_table = 'Screenshots'


class CoverPhoto(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to="Course/CoverPhoto/", blank=True)

    class Meta:
        db_table = 'CoverPhoto'


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    user_ip = models.GenericIPAddressField()
    user_browser = models.CharField(max_length=100, default="")
    location = models.TextField(default="")

    class Meta:
        db_table = 'ContactUs'


class Subscriber(models.Model):
    email = models.EmailField(unique=True, blank=False)
    user_ip = models.GenericIPAddressField()
    user_browser = models.CharField(max_length=100, default="")
    location = models.TextField(default="")
    class Meta:
        db_table = 'Subscriber'


class BaseCMS(models.Model):
    page_title = RichTextUploadingField()
    ico = models.ImageField(upload_to="CMS/BaseHTML/", blank=True)
    logo = models.ImageField(upload_to="CMS/BaseHTML/", blank=True)
    facebook = RichTextUploadingField()
    twitter = RichTextUploadingField()
    linked_in = RichTextUploadingField()
    instagram = RichTextUploadingField()

    class Meta:
        db_table = 'BaseCMS'


class HomeCMS(models.Model):
    banner_message = RichTextUploadingField()
    course_heading_main = RichTextUploadingField()
    course_heading_child = RichTextUploadingField()

    class Meta:
        db_table = 'HomeCMS'


# class AboutCMS(models.Model):
#     profile_image = models.ImageField(upload_to="CMS/About/AdminProfileImage/", blank=True, default="")
#     heading = RichTextUploadingField()
#     profession = RichTextUploadingField()
#     about = RichTextUploadingField()
#     address = RichTextUploadingField()
#     phone = RichTextUploadingField()
#     email = RichTextUploadingField()

#     class Meta:
#         db_table = 'AboutCMS'


class Portfolio(models.Model):
    photo = models.ImageField(upload_to="CMS/About/Portfolio/", blank=True)

    class Meta:
        db_table = "Portfolio"


class CourseCMS(models.Model):
    heading = RichTextUploadingField()
    sub_heading = RichTextUploadingField()

    class Meta:
        db_table = "CourseCMS"
