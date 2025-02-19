from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __unicode__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Department(models.Model):
    department_name = models.CharField(max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Prerequisite(models.Model):
    blocked_class = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='prerequisites')
    requirement = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='required_for')
