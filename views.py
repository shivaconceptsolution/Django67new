from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Student,Reg,Staff
def addstaff(request):
	return render(request,"studentapp/addstaff.html")
def stafflogic(request):
	s = Staff(sname=request.GET['txtname'],sal=request.GET['txtsal'],desig=request.GET['txtdesig'])
	s.save()
	return render(request,"studentapp/addstaff.html",{'key':'inserted successfully'}) 
def viewstaff(request):
	s = Staff.objects.all()
	return render(request,"studentapp/viewstaff.html",{'key':s})
def index(request):
    return render(request,"studentapp/index.html")
def reg(request):
	s = Student(rno=request.GET['txtrno'],sname=request.GET['txtname'],branch=request.GET['txtbranch'],fees=request.GET['txtfees'])
	s.save()
	return render(request,"studentapp/index.html") 
def login(request):
    return render(request,"studentapp/login.html")   
def loginlogic(request):
	e = request.POST["txtemail"]
	pa = request.POST["txtpass"]
	s = Reg.objects.filter(email=e,passsword=pa)
	if(s.count()==1):
	 return redirect('viewstudent')
	else: 
	 return render(request,"studentapp/login.html",{"key":"invalid userid password"})

def about(request):
    return render(request,"studentapp/about.html")
def contact(request):
    return render(request,"studentapp/contact.html")  
def viewstudent(request):
	res = Student.objects.all()
	return render(request,"studentapp/viewstudent.html",{'s1':res})          
def editstu(request):
	sid= request.GET["q"]

	res = Student.objects.get(pk=sid)
	print("value is ",res.rno)
	return render(request,"studentapp/editstu.html",{'s':res})
def deletestu(request):
	sid= request.GET["q"]
	res = Student.objects.get(pk=sid)
	res.delete()
	return redirect('viewstudent')	

def updatestu(request):
   sid= request.POST["txtid"]
   res = Student.objects.get(pk=sid)	
   res.rno=request.POST["txtrno"]
   res.sname=request.POST["txtsname"]
   res.branch=request.POST["txtbranch"]
   res.fees=request.POST["txtfees"]
   res.save()
   return redirect('viewstudent')	     

def si(request):
  p=12000
  r=2.2
  t=2
  si=(p*r*t)/100
  return HttpResponse("Result is "+str(si))

def add(request):
  return render(request,"studentapp/add.html")

def addlogic(request):

	a = request.POST["txtnum1"]
	b = request.POST["txtnum2"]
	if(request.POST['btnsubmit'] =="ADD"):
	 c = int(a)+int(b)
	elif(request.POST['btnsubmit'] =="SUB"):
	 c = int(a)-int(b)
	elif(request.POST['btnsubmit'] =="MULTI"):
	 c = int(a)*int(b)
	else:
	 c = int(a)/int(b)  
	return render(request,"studentapp/add.html",{'key':'result is '+str(c)})





