
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('home/', views.home),
    path('', views.index, name='index'),
    path('authorlogin/', views.Authority_Login, name="authorlogin"),
    path('authorreg/', views.Authority_Reg, name='authorreg'),
    path('authorpass/', views.Authority_pass, name='authorpass'),
    path('teacherlogin/', views.Teacher_login, name='teacherlogin'),
    path('teacherreg/', views.Teacher_reg, name='teacherreg'),
    path('teacherpass/', views.Teacher_pass, name='teacherpass'),
    path('studentlogin/', views.Student_login, name='studentlogin'),
    path('studentreg/', views.Student_reg, name='studentreg'),
    path('studentpass/', views.Student_pass, name='studentpass'),
    path('athurpage/', views.Author_page,  name='athurpage'),
    path('addstudent/', views.addStudent, name='addstudent'),
    path('allstudent/', views.allStudent, name='allstudent'),
    path('editStudent/<id>', views.editStudent, name='editStudent'),
    path('addteacher/', views.addteacher, name='addteacher'),
    path('allteacher/', views.allteacher, name='allteacher'),
    path('editteacher/<id>', views.editteacher, name='editteacher'),
    path('Teachdelete/<id>', views.Teachdelete, name='Teachdelete'),
    path('TeachShow', views.TeachShow, name='TeachShow'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('EditCourse/<id>', views.EditCourse, name='EditCourse'),
    path('AllCourse/', views.AllCourse, name='AllCourse'),
    path('Couresdelete/<id>', views.Couresdelete, name='Couresdelete'),
    path('stushow/', views.stushow, name='stushow'),
    path('delete/<id>', views.delete, name='delete'),
    path('addstusearch', views.addstusearch, name='addstusearch'),
    path('admissions', views.admissions, name='admissions'),
    path('OnlineApply', views.OnlineApply, name='OnlineApply'),
    path('admissionsdetail', views.admissionsdetail, name='admissionsdetail'),
    path('AddStuResult', views.AddStuResult, name='AddStuResult')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)