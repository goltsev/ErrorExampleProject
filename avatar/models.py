from copy import deepcopy
from django.contrib.auth.models import User
from django.db import models


# def upload_to(instance, filename):
#     return 'test_folder' % (instance.email, filename)

# admim
# pass chupakabra

class Avatar(models.Model):

    class Meta:
        verbose_name = 'Авы'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_instance = deepcopy(self)

        print('__init__: self.avatar == self.__old_instance.avatar=> ', self.avatar == self.__old_instance.avatar)

        self.__old_instance.id = None

    avatar = models.ImageField(upload_to="test_folder/", null=True, blank=True, verbose_name='avatar')

    def save(self, *args, **kwargs):
        if self.avatar == self.__old_instance.avatar:
            print('Бага нет')
        else:
            print('Баг есть')
            print("NEW avatar", self.avatar)
            print("OLD old avatar", self.__old_instance.avatar)
        super(Avatar, self).save(*args, **kwargs)
