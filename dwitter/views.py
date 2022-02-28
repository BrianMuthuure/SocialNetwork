from django.shortcuts import render, redirect

# Create your views here.
from dwitter.models import Profile
from .forms import DweetForm


def dashboard(request):
    if request.method == 'POST':
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    form = DweetForm()
    return render(request, 'dwitter/dashboard.html', {'form': form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'dwitter/profile_list.html', context)


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    context = {
        'profile': profile
    }
    return render(request, 'dwitter/profile.html', context)