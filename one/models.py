from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    passwd = models.CharField(max_length=512, default="abc")
    email = models.EmailField(default="abc@hw.com")

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "班级"
        verbose_name_plural = "班级"


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.ForeignKey("Grade", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40)
    people = models.ManyToManyField(People)


class IDCard(models.Model):
    no = models.CharField(max_length=18, unique=True)
    people = models.OneToOneField(People, on_delete=models.PROTECT)

    def __str__(self):
        return self.no

class Pic(models.Model):
    pic = models.ImageField(upload_to='test')