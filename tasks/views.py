from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Task
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserInvitation

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confrim_delete.html'
    success_url = reverse_lazy('task_list')


def send_invitation_email(request, task_id):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            task = get_object_or_404(Task, pk=task_id)
            
            # Create invitation
            invitation = UserInvitation.objects.create(
                email=email,
                invited_by=request.user,
                task=task
            )

            current_site = get_current_site(request)
            invite_url = f"{request.scheme}://{current_site.domain}/accounts/signup/?token={invitation.token}"
            
         
            context = {
                'task': task,
                'invite_url': invite_url,
                'domain': current_site.domain,
                'protocol': 'https' if request.is_secure() else 'http'
            }
            
           
            email_html = render_to_string('tasks/invitation_email.html', context)
            
            try:
                send_mail(
                    'Invitation to Task Manager',
                    'You have been invited to join Task Manager',
                    None,  # Uses DEFAULT_FROM_EMAIL from settings
                    [email],
                    html_message=email_html,
                    fail_silently=False,
                )
                messages.success(request, f"Invitation sent to {email}!")
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")
        else:
            messages.error(request, "Please provide a valid email address.")
    
    return HttpResponseRedirect(reverse('task_list'))

from allauth.account.forms import SignupForm
from django.shortcuts import redirect

def invite_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        send_invitation_email(request, email)
        return redirect("task_list")  
    return render(request, "tasks/invite_user.html")
