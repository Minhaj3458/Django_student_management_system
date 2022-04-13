from django.db import models
import mysql.connector
# Create your models here.
class Authorregiss(models.Model):
    Id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Phone_number = models.CharField(max_length=20)
    Password = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Fname
    class Meta:
        db_table = 'authority_reg'

class Addstupage(models.Model):
    Id = models.AutoField(primary_key=True)
    Student_Id = models.CharField(max_length=255,unique=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Mobile_Number = models.IntegerField()
    Registration_Date = models.CharField(max_length=255)
    Batch_No = models.CharField(max_length=255)
    Departments = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Trimester = models.CharField(max_length=255)
    Blood_Group = models.CharField(max_length=255)
    Parents_Name = models.CharField(max_length=255)
    Parents_Mbl_Num = models.IntegerField()
    Upload_Image = models.ImageField(upload_to ='')
    Address = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Student_Id
    class Meta:
        db_table = 'Addstu_page'


class Studentregi(models.Model):
    Id = models.AutoField(primary_key=True)
    Student_Id = models.CharField(max_length=255,unique=True)
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Depart = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Phone_number = models.IntegerField()
    Password = models.CharField(max_length=255)
    Check = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = 'Student_reg'

class Teacherreg(models.Model):
    Id = models.AutoField(primary_key=True)
    Teacher_Id = models.CharField(max_length=255,unique=True)
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Depart = models.CharField(max_length=255)
    Email = models.CharField(max_length=255, unique=True)
    Phone_number = models.IntegerField()
    Password = models.CharField(max_length=255)
    Check = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'Teacher_reg'
class Online_Apply(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Phone_Number = models.IntegerField()
    Gender = models.CharField(max_length=255)
    Departments = models.CharField(max_length=255)
    Trimester = models.CharField(max_length=255)
    Guardian_Name = models.CharField(max_length=255)
    Guardian_Number = models.CharField(max_length=255)
    Personal_Identity = models.IntegerField(unique=True)
    Img = models.ImageField(upload_to ='')
    Address = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = 'Online_Apply_table'

class AddTeacherpage(models.Model):
    Id = models.AutoField(primary_key=True)
    Teacher_Id = models.CharField(max_length=255,unique=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Mobile_Number = models.IntegerField()
    Joining_Date = models.CharField(max_length=255)
    Nid_NO = models.IntegerField(unique=True)
    Departments = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Blood_Group = models.CharField(max_length=255)
    Parents_Name = models.CharField(max_length=255)
    Parents_Mbl_Num = models.IntegerField()
    Upload_Image = models.ImageField(upload_to='')
    Address = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Teacher_Id
    class Meta:
        db_table = 'AddTeacherpage'

class AddCourse(models.Model):
    Id = models.AutoField(primary_key=True)
    Course_Name = models.CharField(max_length=255)
    Course_Code = models.CharField(max_length=255)
    Start_Date = models.CharField(max_length=255)
    Course_Duration = models.CharField(max_length=255)
    Course_Price = models.CharField(max_length=255)
    Batch = models.CharField(max_length=255)
    Trimester = models.CharField(max_length=255)
    Professor_Name = models.CharField(max_length=255)
    Contact_Number = models.IntegerField()
    Course_Photo = models.ImageField(upload_to='')
    Course_Details = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Course_Name
    class Meta:
        db_table = 'AddCourses'

class AddstuResult(models.Model):
    Id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Addstupage,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Batch_No = models.CharField(max_length=255)
    Trimester = models.CharField(max_length=255)
    Departments = models.CharField(max_length=255)
    CGPA = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.student_id
    class Meta:
        db_table = 'AddStudentResults'
