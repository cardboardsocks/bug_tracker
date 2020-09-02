from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from homepage.models import MyUser, Ticket
from homepage.forms import LoginForm, AddTicketForm


@login_required
def index(request):
    my_tickets = Ticket.objects.all()
    return render(request, "index.html", {"tickets": my_tickets})


@login_required
def add_ticket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                ticket_author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddTicketForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def edit_ticket_view(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    form = AddTicketForm(instance=ticket)
    if request.method == "POST":
        form = AddTicketForm(request.POST, instance=ticket)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    return render(request, "generic_form.html", {"form": form})


@login_required
def ticket_detail_view(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, "ticket_detail.html", {"my_ticket": my_ticket})

@login_required
def assign_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "INPROGRESS"
    ticket.assigned_to = request.user
    ticket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def unassign_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "New"
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def done_view(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "Done"
    my_ticket.assigned_to = None
    my_ticket.completed_by = request.user
    my_ticket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def reopen_view(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "New"
    my_ticket.assigned_to = None
    my_ticket.completed_by = None
    my_ticket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def invalid_view(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "Invalid"
    my_ticket.assigned_to = None
    my_ticket.completed_by = None
    my_ticket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))