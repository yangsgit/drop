from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import os, shutil


class Profile(models.Model):
    def portrait_path(self):
        portrait = 'portrait'
        file_name = '{}_{}'.format(self.user.username, 'portrait')
        return user_directory_path(self.user.username, portrait, file_name)

    user = models.OneToOneField(User, related_name="profile")
    intro = models.CharField(max_length=3000)
    portrait = models.ImageField(upload_to=portrait_path)


class ThemeStyle(models.Model):

    def bgImage_path(self):
        bgImage = 'bgImage'
        fileName = '{}_{}'.format(self.user.username, bgImage)
        return user_directory_path(self.user.username, bgImage, fileName)

    TYPOGRAPHY_STYLE = (('Dark', 'dark'), ('Light', 'light'))
    user = models.OneToOneField(User, related_name='setting')
    backgroundImage = models.ImageField(upload_to=bgImage_path, default=None)
    typography_style = models.CharField(choices=TYPOGRAPHY_STYLE,
                                        default='dark',
                                        max_length=20)


def user_directory_path(user_name, derictory_name, file_name):  # delete files before upload

    loc = '{}/{}/{}'.format(settings.MEDIA_ROOT, user_name, derictory_name)
    folder = loc
    if not os.path.exists(folder):
        os.makedirs(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    return '{}/{}/{}'.format(user_name, derictory_name, file_name)

