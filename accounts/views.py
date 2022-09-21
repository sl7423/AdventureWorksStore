from django.shortcuts import render, redirect
from store.models import Detail
from .models import Account, CustomerIDBusinessEntityID
from .forms import LoginForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from accounts.MLModels.recommendation import GenerateRecommendations
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):

    def get_context_data(request, **kwargs):
        context = {
            'recommendations': Detail.objects.filter(productid__in=kwargs['recommendation_id'])
        }
        return context


    def get(self, request, *args, **kwargs):
        customerid = CustomerIDBusinessEntityID.objects.filter(business_entity_id=request.user.business_entity_id).values_list('customerid').get()[0]
        recommendation_id = GenerateRecommendations(Detail.as_dataframe()).generate_recommendation(customerid)
        context = self.get_context_data(recommendation_id=recommendation_id)
        return render(request, 'accounts/dashboard.html', context)



class LoginPageView(View):

    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
        

class LoggingOutView(LogoutView):
    next_page = 'login'

    def get_next_page(self):
        next_page = super().get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'You have logged out!'
        )
        return next_page