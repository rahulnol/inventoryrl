from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
import json
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from MyNetApp.models import MyUser
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password

class ValidateLogin(View):
    def post(self,req,*args,**kwargs):
        print('Hi inside validatee class')


@csrf_exempt
def validateLogin(request):
    if(request.method == 'POST'):
        pjd = request.body
        print('pjd : ',pjd)
        pdd = json.loads(pjd)
        vemail = pdd.get('jsemail',None)
        vpassword = pdd.get('jspasword',None)
        newPassword = make_password(vpassword)
        myUser = authenticate(username = pdd.get('jsemail',None), password = vpassword)
        print ('myUser...', myUser)
        if myUser:
            login(request, myUser, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'mysuccess': 'Pass', 'mymsg': 'You can create your account','myurl':'http://127.0.0.1:8000/dashboard/'})
        else:
            return JsonResponse({'mysuccess': 'Fail'})

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    def get(self, req, *args, **kwargs):
        # return render(req,'myprac.html')
        return render(req, 'pages/signup.html')
        # return render(req,'home/index.html')

    def post(self, req, *args, **kwargs):
        pjd = req.body
        pdd = json.loads(pjd)
        vuname = pdd['jsuname']
        vphoneno = pdd['jsphoneno']
        vemail = pdd['jsemail']
        vpassword = pdd['jspassword']
        dr = {'mysuccess': 'Pass', 'mymsg': 'You can create your account','myurl':'http://127.0.0.1:8000/dashboard/'}

        user = MyUser.objects.filter(username=vuname)
        if user.count():
            dr['mysuccess'] = 'Fail'
            dr['mymsguname'] = 'Username already exist'

        # user = MyUser.objects.filter(email=vemail)
        # if user.count():
        #     dr['mysuccess'] = 'Fail'
        #     dr['mymsgemail'] = 'Email already exist'

        try:
            user = MyUser.objects.get(email=vemail)
            dr['mysuccess'] = 'Fail'
            dr['mymsgemail'] = 'Email already exist'
        except MyUser.DoesNotExist:
            pass

        user = MyUser.objects.filter(phone_number=vphoneno)
        if user.count():
            dr['mysuccess'] = 'Fail'
            dr['mymsgphone'] = 'Phone no already exist'

        mysuccess = dr.get('mysuccess',None)
        if(mysuccess == 'Pass'):
            newPassword = make_password(vpassword)
            myUser = MyUser.objects.create(username=vuname,email=vemail,phone_number=vphoneno,password=newPassword)
            login(req,myUser, backend='django.contrib.auth.backends.ModelBackend')
            #req.session['myUser'] = myUser
            return JsonResponse(dr)
        else:
            return JsonResponse(dr)

        # try:
        #     user = MyUser.objects.get(username=vuname, email=vemail, phone_number=vphoneno)
        #     # dr = {'mysuccess': 'Fail', 'mymsguname': 'Username already exist', 'note': 'allthere',
        #     #       'mymsgemail': 'Email already exist','mymsgphone': 'Phone no already exist'}
        #     dr['mysuccess'] = 'Fail'
        #     dr['mymsguname'] = 'Username already exist'
        #     dr['note'] = 'allthere'
        #     dr['mymsgemail'] = 'Email already exist'
        #     dr['mymsgphone'] = 'Phone no already exist'
        #     return JsonResponse(dr)
        # except MyUser.DoesNotExist:
        #     try:
        #         user = MyUser.objects.get(username=vuname)
        #         dr = {'mysuccess': 'Fail', 'mymsg': 'Username already exist', 'note': 'username'}
        #         return JsonResponse(dr)
        #
        #     except MyUser.DoesNotExist:
        #         try:
        #             user = MyUser.objects.get(email=vemail)
        #             dr = {'mysuccess': 'Fail', 'mymsg': 'Email already exist', 'note': 'email'}
        #             return JsonResponse(dr)
        #         except MyUser.DoesNotExist:
        #             try:
        #                 user = MyUser.objects.get(phone_number=vphoneno)
        #                 dr = {'mysuccess': 'Fail', 'mymsg': 'Phone no already exist', 'note': 'phoneno'}
        #                 return JsonResponse(dr)
        #             except MyUser.DoesNotExist:
        #                 dr = {'mysuccess': 'Pass', 'mymsg': 'You can create your account'}
        #                 return JsonResponse(dr)
        #
        #     # user = MyUser.objects.get(Q(username=vuname)| Q(email=vemail) | Q(phone_number=vphoneno))

    # def post(self,req,*args,**kwargs):
    #         vemail = req.POST.get('email','No email')
    #         vp = req.POST.get('password','No email')
    #         vcp = req.POST.get('confirmPassword','No email')
    #         print('vemail : ',vemail)
    #         print('vp : ',vp)
    #         print('vcp : ',vcp)


