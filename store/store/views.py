from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 自動登入剛註冊的用戶
            login(request, user)
            return redirect('login')  # 重定向到登入頁面或其他頁面
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})