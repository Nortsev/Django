from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)



class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('adminapp:admin_users')
    form_class = UserAdminRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-detele.html'
    success_url = reverse_lazy('adminapp:admin_users')
    form_class = UserAdminProfileForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

class UserDeleteView (DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-detele.html'
    success_url = reverse_lazy('adminapp:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_remove(request, user_id):
#     user = User.objects.get(id=user_id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))
