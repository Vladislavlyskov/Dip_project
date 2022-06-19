from django.db import models

# Create your models here.

class Profession(models.Model):
    title = models.CharField(max_length=255)



    def __str__(self):
        return self.title

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    profession = models.ForeignKey(Profession, on_delete=models.DO_NOTHING, null=True, blank=True)
    contact_info = models.OneToOneField(
        "ContactInfo", null=True,
        related_name='customer',
        on_delete=models.SET_NULL,
    )
    hobbies = models.ManyToManyField('Hobbies', related_name='customers')

    def __str__(self):
        return f"{self.pk}, {self.firstname}"

    # def get_full_name(self):
    #     return f"{self.firstname} {self.lastname}"

    # @property
    # def full_name(self):
    #     return f"{self.firstname} {self.lastname}"


    # class Meta:
    #     verbose_name = "Customer"
    #     verbose_name_plural = "Customer"

class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)

    class Meta:
        verbose_name = "Contact info"
        verbose_name_plural = "Contact info"

    def __str__(self):
        return f" {self.phone}, {self.address}"

class Hobbies(models.Model):
    name = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobby"

    def __str__(self):
        return self.name