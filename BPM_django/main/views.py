
from django import http
from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
import json
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    user_id = request.session.get('user')
    print('1')
    if user_id:
        print('2')
        member = User.objects.get(pk=user_id)
        return HttpResponse(member.user_name)

    return HttpResponse('Home')

def index(request):
    return render(request, 'main/index.html')

def join(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                        user_name=request.POST['username'],
                        user_password=request.POST['password1'],
                        userBirth=request.POST['userBirth'],
                        userWeight=request.POST['userWeight'],
                        userHeight=request.POST['userHeight'],)
            # auth.login(request, user)
            user.save()
            return redirect('/')
        return render(request, 'main/join.html')
    return render(request, 'main/join.html')

def logout(request):
    if request.session['user'] : 
        print('1')
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method=='GET':
        print('111')
        return render(request,'main/login.html')
    elif request.method =='POST' :
        print('222')
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')

        #유효성 처리
        res_data = {}
        print("1")
        if not (username and password):
            print('2')
            res_data['error']='모든 칸을 다 입력해주세요'
        else:
            print('3')
            # 기존(DB)에 있는 모델과 같은 값인 걸 가져온다.
            user = User.objects.get(user_name = username) #(필드명 = 값)
            print('5')
            print(user.user_password)
            #비밀번호가 맞는지 확인한다. 위에 check_password를 참조
            if password == user.user_password:
                #응갑 데이터 세션에 fuser의 기본키(pk)값인 id 추가. 나중에 쿠키에 저장됨
                request.session['user'] = user.id
                print('6')
                return redirect('/')
            else:
                print('7')
                res_data['error'] = '비밀번호가 틀림'
        print('4')
        return render(request, 'main/login.html', res_data) #응답 데이터 res_data 전달



'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import User

def index(request):
    return render(request, 'main/index.html')

# def index(request):
#     user_id = request.session.get('user')
#     #print(user_id)
#     if user_id:
#         member = User.objects.get(pk=user_id)
#         return HttpResponse(member.username)
# 
    # return HttpResponse('Home!')

def login(request):
    if request.method == "GET":
        return render(request, 'main/login.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data ={}
        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요!'

        else:
            member = User.objects.get(username=username)
            #print(member.id)

            if check_password(password, member.password):
                #print(request.session.get('user'))
                request.session['user'] = member.id

                return redirect('/')


            else:
                res_data['error'] = '비밀번호가 다릅니다!'

        return render(request, 'main/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def join(request):
    if request.method == "GET":
        return render(request, 'main/join.html')

    elif request.method == "POST":
        #print (request.POST)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        userBirth = request.POST.get('userBirth', None)
        userWeight = request.POST.get('userWeight', None)
        userHeight = request.POST.get('userHeight', None)

        res_data = {}
        if not (username and password and re_password ):
            res_data['error'] = '모든 값을 입력하세요!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print(res_data)

        else:
            member = User(
                username    = username,
                password    = make_password(password),
                userBirth   = userBirth,
                userWeight  = userWeight,
                userHeight  = userHeight,
            )
            member.save()

        return render(request, '/', res_data)
'''