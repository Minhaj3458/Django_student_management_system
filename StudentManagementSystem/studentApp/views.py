from django.shortcuts import render,redirect
import mysql.connector
from .forms import formstupage,formregstu,formregtea,AddTeachform,AddCourseform
from .import models
from django.http import HttpResponse
import environ
from django.contrib import messages
from .import forms
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'Home.html')
def index(request):
    return render(request,'index.html')
def Authority_Login(request):
    conn2 = mysql.connector.connect(host='localhost', user='root', password='', database='student_management_system1')
    if request.method == 'POST':
        User_email = request.POST.get('email')
        User_password = request.POST.get('password')
        cur2 = conn2.cursor()
        quer1 = "select Email,Password from authority_reg where Email=%s"
        val = (User_email,)
        cur2.execute(quer1,val)
        data = cur2.fetchall()
        print(data,User_email)
        if User_email == data[0][0] and User_password == data[0][1]:
            return redirect('athurpage')
    else:
        return render(request,'Authority_Login_page.html',)
def Authority_Reg(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        data = request.POST.get('data')
        time = request.POST.get('time')
        Mydata = models.Authorregiss()
        Mydata.Id = id
        Mydata.Fname = fname
        Mydata.Lname = lname
        Mydata.Email = email
        Mydata.Phone_number = phone_number
        Mydata.Password = password
        Mydata.Date = data
        Mydata.Time = time
        Mydata.save()
        return redirect('authorlogin')
    return render(request, 'Authority_Register_page.html')

def Authority_pass(request):
    return render(request,'Authority_forgetpass_page.html')
def Teacher_login(request):
    if request.method == 'POST':
        Teacher_Id = request.POST.get('Teacher_Id')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Mydata = models.Teacherreg.objects.get(Teacher_Id=Teacher_Id, Email=Email, Password=Password)
        if Mydata:
            data = models.AddTeacherpage.objects.get(Teacher_Id=Teacher_Id)
            return render(request, 'Authority/Teachershowpage.html', {'data': data})

    return render(request,'Teachers_login_page.html')
def Teacher_reg(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        teacher_id = request.POST.get('Teacher_Id')
        depart = request.POST.get('Depart')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone_number')
        password = request.POST.get('Password')
        con_password = request.POST.get('Con_password')
        check = request.POST.get('Check')
        date = request.POST.get('Date')
        time = request.POST.get('time')
        Mydata = models.AddTeacherpage.objects.get(Teacher_Id=teacher_id)
        if password == con_password and Mydata:
            Mydata = models.Teacherreg()
            Mydata.Id = id
            Mydata.Fname = fname
            Mydata.Lname = lname
            Mydata.Teacher_Id = teacher_id
            Mydata.Depart = depart
            Mydata.Email = email
            Mydata.Phone_number = phone_number
            Mydata.Password = password
            Mydata.Check = check
            Mydata.Date = date
            Mydata.Time = time
            Mydata.save()
            return redirect('teacherlogin')
        else:
            return HttpResponse("password & confirmpassword must same!")
    return render(request,'Teachers_Register_page.html')
def Teacher_pass(request):
    return render(request,'Teachers_Forgot_password.html')
def Student_login(request):
    conn3 = mysql.connector.connect(host='localhost', user='root', password='', database='student_management_system1')
    if request.method == 'POST':
        Student_id = request.POST.get('students_id')
        User_email = request.POST.get('email')
        User_password = request.POST.get('password')
        cur3 = conn3.cursor()
        quer3 = "select Email,Password,Student_Id from Student_reg where Student_Id=%s"
        val = (Student_id,)
        cur3.execute(quer3,val)
        data = cur3.fetchall()
        print(data, Student_id)
        if User_email == data[0][0] and User_password == data[0][1] and Student_id == data[0][2]:
            data = models.Addstupage.objects.get(Student_Id=Student_id)
            return render(request, 'Authority/StudentShowpase.html',{'data':data})
    else:
     return render(request,'Students_login_page.html',)
def Student_reg(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        depart = request.POST.get('Depart')
        student_id = request.POST.get('Student_Id')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone_number')
        password = request.POST.get('Password')
        con_password = request.POST.get('Con_password')
        check = request.POST.get('Check')
        date = request.POST.get('data')
        time = request.POST.get('time')
        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                       database='student_management_system1')
        cur = conn.cursor()
        quer = "select Student_Id from addstu_page where Student_Id=%s"
        val = (student_id,)
        cur.execute(quer, val)
        data = cur.fetchone()
        print(data, student_id)
        if student_id == data[0] and password ==con_password:
            Mydata = models.Studentregi()
            Mydata.Id = id
            Mydata.Fname = fname
            Mydata.Lname = lname
            Mydata.Depart = depart
            Mydata.Student_Id = student_id
            Mydata.Email = email
            Mydata.Phone_number = phone_number
            Mydata.Password = password
            Mydata.Check = check
            Mydata.Date = date
            Mydata.Time = time
            Mydata.save()
            return redirect('studentlogin')
    return render(request,'Students_Register_page.html')
def Student_pass(request):
    return render(request,'Students_ForgotPassword_page.html')
def Author_page(request):
    show = models.Addstupage.objects.all()
    return render(request,'Authority/Authority_page.html',{"data":show})
def addStudent(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        trimester = request.POST.get('Trimester')
        registration_date = request.POST.get('registration_date')
        batch_no = request.POST.get('batch_no')
        departments = request.POST.get('departments')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        parents_name = request.POST.get('parents_name')
        parents_mbl_num = request.POST.get('parents_mbl_num')
        upload_image = request.FILES.get('upload_image')
        fname = upload_image.name
        with open('F:/project1/StudentManagementSystem/static/static_files/media/' + fname, 'wb+') as location:
            for ch in upload_image.chunks():
                location.write(ch)
        address = request.POST.get('address')
        date = request.POST.get('data')
        time = request.POST.get('time')
        mydata = models.Addstupage()
        mydata.Id = id
        mydata.Student_Id = student_id
        mydata.First_Name = first_name
        mydata.Last_Name = last_name
        mydata.Email = email
        mydata.Mobile_Number = mobile_number
        mydata.Trimester = trimester
        mydata.Registration_Date = registration_date
        mydata.Batch_No = batch_no
        mydata.Departments = departments
        mydata.Gender = gender
        mydata.Blood_Group = blood_group
        mydata.Parents_Name = parents_name
        mydata.Parents_Mbl_Num = parents_mbl_num
        mydata.Upload_Image = upload_image
        mydata.Address = address
        mydata.Date = date
        mydata.Time = time
        mydata.save()
        show = models.Addstupage.objects.all()
        return render(request, 'Authority/AddStudents.html', {"data": show})
    else:
        show = models.Addstupage.objects.all()
        return render(request, 'Authority/AddStudents.html', {"data": show})
def allStudent(request):
    if request.method == 'POST':
        Serch = request.POST.get('search')
        print(Serch)
        show = models.Addstupage.objects.filter(Student_Id=Serch) or models.Addstupage.objects.filter(Departments=Serch)
        return render(request,'Authority/AllStudents.html',{"data":show})

    show = models.Addstupage.objects.all().order_by('-Id')
    return render(request,'Authority/AllStudents.html',{"data":show})
def editStudent(request,id):
    data = models.Addstupage.objects.get(Student_Id =id)
    if request.method == 'POST':
        data = formstupage (request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('allstudent')
        else:
            return HttpResponse("Failed")
    return render(request,'Authority/editstudent.html',{'data':data})
def addteacher(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Upload_Image')
        fname = upload_image.name
        with open('F:/project1/StudentManagementSystem/static/static_files/media/' + fname, 'wb+') as location:
            for ch in upload_image.chunks():
                location.write(ch)
        Mydata = models.AddTeacherpage()
        Mydata.Id = request.POST.get('Id')
        Mydata.Teacher_Id = request.POST.get('Teacher_Id')
        Mydata.First_Name = request.POST.get('First_Name')
        Mydata.Last_Name = request.POST.get('Last_Name')
        Mydata.Email = request.POST.get('Email')
        Mydata.Mobile_Number = request.POST.get('Mobile_Number')
        Mydata.Joining_Date = request.POST.get('Joining_Date')
        Mydata.Nid_NO = request.POST.get('Nid_NO')
        Mydata.Departments = request.POST.get('Departments')
        Mydata.Gender = request.POST.get('Gender')
        Mydata.Blood_Group = request.POST.get('Blood_Group')
        Mydata.Parents_Name = request.POST.get('Parents_Name')
        Mydata.Parents_Mbl_Num = request.POST.get('Parents_Mbl_Num')
        Mydata.Upload_Image = upload_image
        Mydata.Address = request.POST.get('Address')
        Mydata.Date = request.POST.get('Date')
        Mydata.Time = request.POST.get('Time')
        Mydata.save()
        show = models.AddTeacherpage.objects.all().order_by('-Teacher_Id')
        return render(request,'Authority/addteacher.html', {"data": show})
    else:
        show = models.AddTeacherpage.objects.all().order_by('-Teacher_Id')
        return render(request,'Authority/addteacher.html', {"data": show})
def allteacher(request):
    show = models.AddTeacherpage.objects.all().order_by('-Teacher_Id')
    return render(request,'Authority/allteachers.html', {"data": show})
def editteacher(request,id):
    data = models.AddTeacherpage.objects.get(Teacher_Id=id)
    if request.method == 'POST':
        data = AddTeachform(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('allteacher')
        else:
            return HttpResponse("Failed")
    return render(request, 'Authority/editteacher.html',{'data':data})

def Teachdelete(request,id):
    data = models.AddTeacherpage.objects.get(Teacher_Id=id)
    data.delete()
    return redirect('allteacher')
def TeachShow(request):
    return render(request, 'Authority/Teachershowpage.html')
def addcourses(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Course_Photo')
        fname = upload_image.name
        with open('F:/project1/StudentManagementSystem/static/static_files/media/' + fname, 'wb+') as location:
            for ch in upload_image.chunks():
                location.write(ch)
        Mydata = models.AddCourse()
        Mydata.Id = request.POST.get('Id')
        Mydata.Course_Name = request.POST.get('Course_Name')
        Mydata.Course_Code = request.POST.get('Course_Code')
        Mydata.Start_Date = request.POST.get('Start_Date')
        Mydata.Course_Duration = request.POST.get('Course_Duration')
        Mydata.Course_Price = request.POST.get('Course_Price')
        Mydata.Batch = request.POST.get('Batch')
        Mydata.Trimester = request.POST.get('Trimester')
        Mydata.Professor_Name = request.POST.get('Professor_Name')
        Mydata.Contact_Number = request.POST.get('Contact_Number')
        Mydata.Course_Photo = upload_image
        Mydata.Course_Details = request.POST.get('Course_Details')
        Mydata.Date = request.POST.get('Date')
        Mydata.Time = request.POST.get('Time')
        Mydata.save()
        show = models.AddCourse.objects.all().order_by('-Id')
        return render(request,'Authority/addcourses.html', {"data": show})
    elif request.method == 'POST':
        Serch = request.POST.get('search')
        print(Serch)
        show = models.AddCourse.objects.filter(Batch=Serch) or models.AddCourse.objects.filter(Professor_Name=Serch) or models.AddCourse.objects.filter(Course_Name=Serch)
        return render(request,'Authority/addcourses.html',{"data": show})
    else:
        show = models.AddCourse.objects.all().order_by('-Id')
        return render(request, 'Authority/addcourses.html', {"data": show})
def AllCourse(request):
    if request.method == 'POST':
        Serch = request.POST.get('search')
        print(Serch)
        show = models.AddCourse.objects.filter(Batch=Serch) or models.AddCourse.objects.filter(Professor_Name=Serch) or models.AddCourse.objects.filter(Course_Name=Serch)
        return render(request, 'Authority/AllCourses.html', {"data": show})
    show = models.AddCourse.objects.all().order_by('-Id')
    return render(request,'Authority/AllCourses.html',{"data": show})
def EditCourse(request,id):
    data = models.AddCourse.objects.get(Id=id)
    if request.method == 'POST':
        data = AddCourseform(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('AllCourse')
        else:
            return HttpResponse("Failed")
    return render(request, 'Authority/CourseEdit.html', {'data': data})

def Couresdelete(request,id):
    data = models.AddCourse.objects.get(Id=id)
    data.delete()
    return redirect('AllCourse')

def stushow(request):
    return render(request,'Authority/StudentShowpase.html')
def delete(request,id):
    data = models.Addstupage.objects.get(Student_Id=id)
    data.delete()
    return redirect('allstudent')
def addstusearch(request):
    return render(request, 'Authority/addstudentsearch.html')
def admissions(request):
    if request.method == 'POST':
        Id = request.POST.get('Id')
        Name = request.POST.get('Name')
        Surname = request.POST.get('Surname')
        Email = request.POST.get('Email')
        Phone_Number = request.POST.get('Phone_Number')
        trimester = request.POST.get('Trimester')
        Gender = request.POST.get('Gender')
        Departments = request.POST.get('Departments')
        Guardian_Name = request.POST.get('Guardian_Name')
        Guardian_Number = request.POST.get('Guardian_Number')
        Personal_Identity = request.POST.get('Personal_Identity')
        upload_image = request.FILES.get('Img')
        fname = upload_image.name
        with open('F:/project1/StudentManagementSystem/static/static_files/media/' + fname, 'wb+') as location:
            for ch in upload_image.chunks():
                location.write(ch)
        Address = request.POST.get('Address')
        Date = request.POST.get('Date')
        Time = request.POST.get('Time')
        data = models.Online_Apply()
        data.Id = Id
        data.Name = Name
        data.Surname = Surname
        data.Email = Email
        data.Phone_Number = Phone_Number
        data.Gender = Gender
        data.Trimester = trimester
        data.Departments = Departments
        data.Guardian_Name = Guardian_Name
        data.Guardian_Number = Guardian_Number
        data.Personal_Identity = Personal_Identity
        data.Img = upload_image
        data.Address = Address
        data.Date = Date
        data.Time = Time
        data.save()
        return HttpResponse("Apply successfully")
    return render(request, 'admissions.html')
def OnlineApply(request):
    show = models.Online_Apply.objects.all().order_by('-Id')
    return render(request, 'Authority/OnlineApply.html',{"data":show})

def admissionsdetail(request):
    return render(request,'admissionsdetail.html')

def AddStuResult(request):
    if request.method == 'POST':
        Mydata = models.AddstuResult()
        Mydata.Id = request.POST.get('Id')
        Mydata.student_id = request.POST.get('student_id')
        Mydata.First_name = request.POST.get('First_name')
        Mydata.Last_name = request.POST.get('Last_name')
        Mydata.Batch_No = request.POST.get('Batch_No')
        Mydata.Trimester = request.POST.get('Trimester')
        Mydata.Departments = request.POST.get('Departments')
        Mydata.Date = request.POST.get('Date')
        Mydata.Time = request.POST.get('Time')
        Mydata.save()

    return render(request, 'Authority/AddStuResult.html')
