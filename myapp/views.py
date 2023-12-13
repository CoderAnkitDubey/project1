#python manage.py runserver
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import usersForm
from myapp.models import service

#is index me humne get method ko implement kiya hai using index.html

def aboutus(request):
    if request.method=="GET":
        output=request.GET.get('out')
    data={
        'number':[1,2,7,8,9],
        'output':output,
        'student':[
            {'name':'ankit','phone':23232233223,'address':'mumbai'},
            {'name':'ankit','phone':23232233223,'address':'mumbai'},
            {'name':'pradeep','phone':23232233223,'address':'malad'},   
        ]
    }
    return render(request,'aboutus.html',data)


def userform(request):
    finalans=" "
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'output':finalans
            }
            url='/aboutus/?out={}'.format(finalans)
            return redirect(url)
          
    except:
        pass
    return render(request,"userform.html",data)

def index(request):
    servicesData=service.objects.all()
    data={
        'servicesData':servicesData
    }
    return render(request,"index.html",data)

def submit(request):
     try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'output':finalans
            }
            return HttpResponse(finalans)
     except:
         pass



#yaha par data pass kiya hai views se template me userreg.html
def userreg(request):
    data={
        'bdata':'',
        'title':'Ankit',
        'clist':['PHP','JAVA','PYTHON','SQL'],
        'stud_detail':[{'Name':'Ankit','MobileNO':8591288105,'Address':'Naigaon','JOB':'Web Developer'},{'Name':'Shivani','MobileNO':4992930305,'Address':'Malad','JOB':'Data Science'}],
        'number':[2,3,4,2]                                                                                                            
        }
    return render(request,"userreg.html",data)





def course(request):
    return HttpResponse("Welcome course")

def coursedetail(request,courseid):
    return HttpResponse(courseid)
def calc(request):
    output=" "
    if request.method=="POST":
        if request.POST.get('n1')=="":
            return render(request,"calc.html",{'error':True})
        num1=eval(request.POST.get('n1'))
        num2=eval(request.POST.get('n2'))
        opr=request.POST.get('opr')
        if opr=='+':
            output=num1+num2
        elif opr=="-":
            output=num1-num2
        elif opr=="*":
            output=num1*num2
        elif opr=="/":
            output=num1/num2
    return render(request,'calc.html',{'output':output})

def marksheet(request):
    total=" "
    p=" "
    d=" "
    try:
        if request.method=="POST":
            s1=eval(request.POST.get("sub1"))
            s2=eval(request.POST.get("sub2"))
            s3=eval(request.POST.get("sub3"))
            s4=eval(request.POST.get("sub4"))
            s5=eval(request.POST.get("sub5"))
            total=s1+s2+s3+s4+s5
            p=total*100/500
            if p==100:
                d="Grade O"
            elif p>=90:
                d="Grade A+"
            elif p>=80:
                d="Grade A"
            elif p>=70:
                d="Grade B+"
            elif p>=60:
                d="Grade B"
            elif p>=50:
                d="Grade C"
            elif p>=40:
                d="Grade D" 
    except:
        pass

        return render(request,'marksheet.html',  {'total':total,'p':p,'div':d})
    return render(request,'marksheet.html',  {'total':total,'p':p,'div':d})




def evenodd(request):
    d=" "
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})
        n1=eval(request.POST.get('num1'))
        if n1%2==0:
            d="Even"
        else:
            d="Odd"
    return render(request,'evenodd.html',{'d':d})
def calculator(request):
    c=""
    try:
        if request.method=="POST":
            
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('oprator')
            
            if opr=="+":
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            elif opr=='/':
                c=n1/n2    

    except:
        c="invalid Input"
    print(c)
    return render(request,"calculator.html",{'c':c}) 