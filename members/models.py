from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Member(models.Model):

    #Member List:
    MEMBER_TYPE = (
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('student', 'Student'),
        ('alumni', 'Alumni'),
    )

    member_type= models.CharField(max_length=10, choices=MEMBER_TYPE)


    DEPARTMENT= (
        ('cse', 'Computer Science and Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('ee', 'Electrical Engineering'),
        ('bt', 'Biotechnology'),
        ('ba', 'Business Administration'),
        ('ma', 'Mathematics'),
        ('phy', 'Physics'),
        ('chem', 'Chemistry'),
    )

    department= models.CharField(max_length=100, choices= DEPARTMENT)

    name= models.CharField(max_length=100)
    

#contact
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=15, unique=True, blank=True, null= True)
    photo= models.ImageField(upload_to ='members/photos/', blank=True, null = True)

#confitional Field:
    designation= models.CharField(max_length=100, blank =True, null= True)
    student_id= models.CharField(max_length=10, unique= True, blank=True, null=True)
    passing_year= models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.member_type
    
    def clean(self):
        #custom logic:
        if self.member_type in ['student', 'alumnni'] and not self.student_id:
            raise ValidationError("Student ID required for students and almunni members.")
        if self.member_type in ['faculty', 'staff'] and not self.designation:
            raise ValidationError("Designation required for facutlties and staff members.")
        if self.member_type in ['alumni'] and not self.passing_year:
            raise ValidationError("Passsing year required for alumni members.")

