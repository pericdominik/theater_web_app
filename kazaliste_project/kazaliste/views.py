from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from datetime import timedelta, date as date_cls
from django.utils import timezone

from .models import Account, Predstava, Calendar, Comment, Like, PriceItem

from .forms import RegisterForm, CalendarWeekForm, CommentForm

# Create your views here.

def index(request):
    return render(request, 'kazaliste/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                form.add_error('email', "Email adresa je već iskorištena.")
                return render(request, 'kazaliste/register.html', {'form': form})

            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            Account.objects.create(
                user=user,
                phone=form.cleaned_data['phone']
            )

            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'kazaliste/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Dobrodošli natrag!")
            return redirect('index') 
        else:
            messages.error(request, "Neispravni podaci (email ili lozinka).")

    return render(request, 'kazaliste/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, "Uspješno ste se odjavili.")
    return redirect('index')


@login_required(login_url='login')
def my_account(request):
    return render(request, 'kazaliste/my_account.html')


@login_required(login_url='login')
def edit_profile(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    edit = (request.GET.get('edit') == '1')

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, "Podaci su uspješno ažurirani.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=account)

    return render(request, 'kazaliste/profile.html', {'form': form, 'user_obj': request.user, 'account': account, 'edit': edit})


def predstave_list(request):
    predstave = Predstava.objects.filter(is_active=True).order_by('title')
    return render(request, 'kazaliste/predstave_list.html', {'predstave': predstave})

def predstava_detail(request, pk):
    predstava = get_object_or_404(Predstava, pk=pk, is_active=True)

    upcoming = (
        Calendar.objects
        .filter(predstava=predstava, is_published=True, date__gte=timezone.localdate())
        .order_by('date', 'time')[:10] 
    )

    comments = predstava.comments.filter(approved=True).order_by('-created_at')

    like_count = predstava.likes.count()
    user_liked = request.user.is_authenticated and Like.objects.filter(predstava=predstava, user=request.user).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                predstava=predstava,
                user=request.user,
                text=form.cleaned_data['text'],
                approved=False 
            )
            messages.info(request, "Komentar je predan i čeka odobrenje administratora.")
            return redirect('predstava_detail', pk=predstava.pk)
    else:
        form = CommentForm()

    return render(request, 'kazaliste/predstava_detail.html', {'predstava': predstava, 'upcoming': upcoming, 'comments': comments, 
                                                               'form': form, 'like_count': like_count, 'user_liked': user_liked})


def calendar_week(request):
    form = CalendarWeekForm(request.GET)
    if form.is_valid():
        base = form.cleaned_data.get('date') or timezone.localdate()
    else:
        base = timezone.localdate()

    monday = base - timedelta(days=base.weekday())  
    sunday = monday + timedelta(days=6)

    events = (Calendar.objects
                .select_related('predstava')
                .filter(is_published=True, date__range=[monday, sunday])
                .order_by('date', 'time', 'predstava__title')
    )

    week_days = []
    for i in range(7):
        week_days.append(monday + timedelta(days=i))
        
    by_day = {d: [] for d in week_days}
    for e in events:
        by_day[e.date].append(e)

    week = [(d, by_day[d]) for d in week_days]

    context = {
        "week_days": week_days,
        "week": week,
        "monday": monday,
        "sunday": sunday,
        "prev_date": monday - timedelta(days=7),
        "next_date": monday + timedelta(days=7),
        "today": timezone.localdate(),
    }
    return render(request, "kazaliste/calendar_week.html", context)


@login_required(login_url='login')
def like_add(request, pk):
    p = get_object_or_404(Predstava, pk=pk, is_active=True)
    Like.objects.get_or_create(predstava=p, user=request.user)
    messages.success(request, "Liked!")
    return redirect('predstava_detail', pk=pk)

@login_required(login_url='login')
def like_remove(request, pk):
    p = get_object_or_404(Predstava, pk=pk, is_active=True)
    Like.objects.filter(predstava=p, user=request.user).delete()
    messages.success(request, "Unliked!")
    return redirect('predstava_detail', pk=pk)


def cjenik(request):
    items = PriceItem.objects.filter(is_active=True).order_by('display_order', 'name')
    return render(request, 'kazaliste/cjenik.html', {'items': items})