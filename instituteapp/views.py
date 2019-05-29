from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedBackForm
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()


def main_page(request):
    return render(request,'base.html')


def home_page(request):
    return render(request,'home_page.html')


def contact_page(request):
    return render(request,'contact_page.html')


def courses_page(request):
    return render(request,'courses_page.html')


def feedback_page(request):
    if request.method == "POST":
        fform = FeedBackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name', '')
            rating = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedBackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request, 'feedback_page.html', {'fform': fform, 'feedbacks': feedbacks})
    else:
        fform = FeedBackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedback_page.html', {'fform': fform, 'feedbacks': feedbacks})


def ourteam_page(request):
    return render(request, 'ourteam_page.html')