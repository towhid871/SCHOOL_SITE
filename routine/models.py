from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from members.models import Member


# Create your models here.


class Routine(models.Model):
    days = (

        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        
    )

    time_slots = (
        ('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM'),
        ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
        ('12:00 PM - 1:00 PM', '12:00 PM - 1:00 PM'),
        ('1:00 PM - 2:00 PM', '1:00 PM - 2:00 PM'),
        ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM'),
        ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM'),
        ('break', 'break'),
    )



    department = models.ForeignKey(Member, on_delete=models.CASCADE, limit_choices_to={'member_type': 'department'}, related_name='department_routines')
    semester = models.CharField(max_length=50)
    day = models.CharField(max_length=10, choices = days)
    time_slot = models.CharField(max_length=20, choices = time_slots)

    subject = models.CharField(max_length=100)
    faculty = models.ForeignKey(Member, on_delete=models.CASCADE, limit_choices_to={'member_type': 'faculty'}, related_name='faculty_routines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.department} - {self.semester} - {self.day} - {self.time_slot}"       
    
    



