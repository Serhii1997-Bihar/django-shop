from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import GalleryUser, ProfileUser, ImagesUser, VideosUser
from django.contrib.auth import authenticate, login, logout
import requests, time
from django.core.paginator import Paginator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def UserCreation(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users_templates/registration.html', context)

def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account', user.id)

    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users_templates/login.html', context)

@login_required
def UserAccount(request, id):
    user = get_object_or_404(User, id=id)
    profile, created = ProfileUser.objects.get_or_create(user=user)
    gallery, created = GalleryUser.objects.get_or_create(user=user)

    images = ImagesUser.objects.filter(gallery=gallery).order_by('?')
    vids = VideosUser.objects.filter(gallery=gallery)
    main_videos = vids[:5]
    paginator = Paginator(vids, 5)
    page = request.GET.get('page')
    videos = paginator.get_page(page)

    import requests
    url = 'http://api.forismatic.com/api/1.0/'
    params = {'method': 'getQuote', 'lang': 'ru', 'format': 'json'}
    response = requests.get(url, params=params)
    resp = response.json()
    text = resp['quoteText']
    author = resp['quoteAuthor']
    content = f"{text} - {author}"

    context = {
        'user': user,
        'profile': profile,
        'gallery': gallery,
        'main_videos': main_videos,
        'images': images,
        'videos': videos,
        'content': content,
    }
    return render(request, 'users_templates/account.html', context)

@login_required
def DeleteImage(request, id):
    image = get_object_or_404(ImagesUser, id=id)
    if image.gallery.user != request.user:
        return HttpResponse("У вас немає прав для видалення цього зображення", status=403)
    image.delete()
    return redirect('account', id=request.user.id)

@login_required
def DeleteVideo(request, id):
    video = get_object_or_404(VideosUser, id=id)
    if video.gallery.user != request.user:
        return HttpResponse("У вас немає прав для видалення цього зображення", status=403)
    video.delete()
    return redirect('account', id=request.user.id)

def Custom_Logout(request):
    logout(request)
    return redirect('login')

@login_required
def UserEdit(request):
    user = request.user
    profile = get_object_or_404(ProfileUser, user=user)
    gallery, created = GalleryUser.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        gallery_form = GalleryForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid() and gallery_form.is_valid():
            user_form.save()
            profile_form.save()

            for image in request.FILES.getlist('images'):
                ImagesUser.objects.create(gallery=gallery, images=image)

            if 'videos' in request.FILES:
                for video_file in request.FILES.getlist('videos'):
                    VideosUser.objects.create(gallery=gallery, videos=video_file)

            return redirect('account', user.id)
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)
        gallery_form = GalleryForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'gallery_form': gallery_form}
    return render(request, 'users_templates/edit.html', context)

def UsersAccounts(request):
    user = request.user
    users = User.objects.prefetch_related('profileuser').exclude(id=user.id).all()
    context = {'users': users}
    return render(request, 'users_templates/users_accounts.html', context)

def UserPerson(request, id):
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(ProfileUser, user=user)
    gallery, created = GalleryUser.objects.get_or_create(user=user)

    images = ImagesUser.objects.filter(gallery=gallery).order_by('?')
    vids = VideosUser.objects.filter(gallery=gallery)
    main_videos = vids[:5]

    paginator = Paginator(vids, 5)
    page = request.GET.get('page')
    videos = paginator.get_page(page)

    url = 'http://api.forismatic.com/api/1.0/'
    params = {'method': 'getQuote', 'lang': 'ru', 'format': 'json'}
    response = requests.get(url, params=params)
    resp = response.json()
    text = resp['quoteText']
    author = resp['quoteAuthor']
    content = f"{text} - {author}"

    context = {'user': user, 'profile': profile, 'images': images, 'videos': videos,
               'main_videos': main_videos, 'content': content}
    return render(request, 'users_templates/user_person.html', context)

def SearchInfo(request, id):
    user = User.objects.get(id=id)
    username = f"{user.first_name} {user.last_name}"

    service = Service(
        'C:\Projects PyCharm\Shop_5\dried_fruits_shop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.google.com')

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
        search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        search.send_keys(username)

        btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))

        driver.execute_script("arguments[0].click();", btn)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[1]/div/div/span/a/h3')))

    except TimeoutException:
        print("Час очікування вичерпано. Елемент не знайдено.")
    finally:
        time.sleep(10)
        driver.quit()
    return redirect('userperson', user.id)

def SendMessage(request, id):
    user = get_object_or_404(User, id=id)
    req_user = request.user

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = MessageUser(
                sender=req_user,
                receiver=user,
                content=cd['content']
            )
            message.save()
            return redirect('userperson', user.id)
    else:
        form = MessageForm()

    context = {'user': user, 'form': form}
    return render(request, 'users_templates/send_message.html', context)

def MessagesIn(request, id):
    user = get_object_or_404(User, id=id)
    req_user = request.user
    messages = MessageUser.objects.filter(receiver=req_user) | MessageUser.objects.filter(sender=req_user)
    senders = messages.values_list('sender', flat=True).distinct()
    receivers = messages.values_list('receiver', flat=True).distinct()
    participants_ids = list(set(senders) | set(receivers))
    sender_users = User.objects.filter(id__in=participants_ids).exclude(id=req_user.id)
    context = {'user': user, 'sender_users': sender_users, 'req_user': req_user}
    return render(request, 'users_templates/messagesin.html', context)

def Dialogue(request, id):
    user = get_object_or_404(User, id=id)
    req_user = request.user
    profile = get_object_or_404(ProfileUser, user=user)
    req_profile = get_object_or_404(ProfileUser, user=req_user)
    dialogue_in = MessageUser.objects.filter(receiver=req_user, sender=user).order_by('-timestamp')
    dialogue_out = MessageUser.objects.filter(receiver=user, sender=req_user).order_by('-timestamp')
    all_messages = list(dialogue_in) + list(dialogue_out)
    all_messages.sort(key=lambda message: message.timestamp)

    paginator = Paginator(all_messages, 8)
    page = request.GET.get('page')
    messages = paginator.get_page(page)


    context = {'user': user, 'messages': messages, 'req_user': req_user, 'req_profile': req_profile,
                'profile': profile}
    return render(request, 'users_templates/dialogue.html', context)






