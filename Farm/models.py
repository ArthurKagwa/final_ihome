from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('In Progress', 'In Progress'),
    ('Cancelled', 'Cancelled'),
]

ANIMAL_STATUS_CHOICES = [
    ('Alive', 'Alive'),
    ('Dead', 'Dead'),
    ('Sold', 'Sold'),
    ('Slaughtered', 'Slaughtered'),
    ('Stolen', 'Stolen'),
    ('Lost', 'Lost'),
    ('Unknown', 'Unknown'),
    ('Sick', 'Sick'),
    ]


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "Type: " + self.name + " Description: " + self.desc


class Breed(models.Model):
    breed_origin = models.CharField(max_length=10)
    breed_name = models.CharField(max_length=50)
    breed_description = models.CharField(max_length=500)
    animal_type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "Origin: " + self.breed_origin + " Breed: " + self.breed_name + " Description: " + self.breed_description


class Animal(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='animal_mother', blank=True)
    father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='animal_father', blank=True)
    dob = models.DateField()  # Date of birth
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    births = models.IntegerField(null=True, blank=True)  # Number of births (if applicable)
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)
    tag_color = models.CharField(max_length=50, blank=True, null=True)  # Tag color for identification
    status = models.CharField(max_length=40, default='Alive', choices=ANIMAL_STATUS_CHOICES)
    def __str__(self):
        return f"ID: {self.id}, Type: {self.type.name if self.type else 'Unknown'}, Breed: {self.breed.breed_name if self.breed else 'Unknown'}, DOB: {self.dob}"

# exited animals
class ExitedAnimal(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='animal_mother', blank=True)
    father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='animal_father', blank=True)
    dob = models.DateField()  # Date of birth
    type_of_exit = models.CharField(max_length=50, choices=[('Sold', 'Sold'), ('Slaughtered', 'Slaughtered'), ('Stolen', 'Stolen'), ('Lost', 'Lost'), ('Unknown', 'Unknown')], default='Unknown', blank=False ),
    exit_date = models.DateField()

class Staff(models.Model):
    staff_id = models.CharField(max_length=10, primary_key=True)
    staff_name = models.CharField(max_length=50)
    staff_address = models.CharField(max_length=100)
    staff_phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")],
    )
    staff_email = models.EmailField()
    staff_position = models.CharField(max_length=50)
    staff_nin = models.CharField(max_length=30, unique=True)
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "Staff ID: " + self.staff_id + " Name: " + self.staff_name + " Position: " + self.staff_position


class Medical(models.Model):
    animal_no = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True)
    treatment_date = models.DateField()
    treatment_name = models.CharField(max_length=50)
    treatment_cost = models.FloatField(null=True)
    treatment_description = models.CharField(max_length=100)
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "Animal No: " + self.animal_no.id + " Treatment Date: " + str(
            self.treatment_date) + " Treatment Name: " + self.treatment_name + " Treatment Cost: " + str(
            self.treatment_cost) + " Treatment Description: " + self.treatment_description


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=300)
    task_day = models.DateField()
    task_staff = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)
    task_animal = models.ForeignKey('Animal', on_delete=models.SET_NULL, related_name='task_animal', null=True)
    task_animal_type = models.ForeignKey('Type', on_delete=models.SET_NULL, related_name='task_animal_type', null=True)
    task_time = models.TimeField(default='00:00:00')
    task_status = models.CharField(max_length=40, default='Pending', choices=STATUS_CHOICES)
    task_notes = models.CharField(max_length=100, default="not bad")
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return " Name: " + self.task_name + " Description: " + self.task_description + " Day: " + str(
            self.task_day) + " Staff: " + self.task_staff.staff_name + " Animal: " + self.task_animal.id + " Type: " + self.task_animal_type.name + " Time: " + str(
            self.task_time) + " Status: " + self.task_status + " Notes: " + self.task_notes


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.CharField(max_length=500)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_staff = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)
    event_animal_type = models.ForeignKey('Type', on_delete=models.SET_NULL, related_name='event_animal_type',
                                          null=True)
    event_notes = models.CharField(max_length=100, default="not bad")
    event_status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='Pending')
    farm = models.ForeignKey('Farm', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return " Name: " + self.event_name + " Description: " + self.event_description + " Date: " + str(
            self.event_date) + " Time: " + str(
            self.event_time) + " Staff: " + self.event_staff.staff_name + " Type: " + self.event_animal_type.name + " Status: " + self.event_status + " Notes: " + self.event_notes


class Farm(models.Model):
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True , unique=True)
    email = models.EmailField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farms' ,default=1)  # ForeignKey to User
    # created_at = models.DateTimeField(auto_now_add=True , blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return f"{self.username} ({self.email})"


