from django.shortcuts import render
from datetime import datetime

# Create your views here.
def uncompleted_list_show(request):

    tasks = [
        {
            'id': '1',
            'name': 'Go to the gym',
            'created': datetime(2021, 2, 21).strftime("%d/%m/%Y"),
            'due': datetime(2021, 2, 23).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        },
        {
            'id': '2',
            'name': 'Write internship report',
            'created': datetime(2021, 2, 22).strftime("%d/%m/%Y"),
            'due': datetime(2021, 3, 5).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        },
        {
            'id': '3',
            'name': 'Read a book',
            'created': datetime(2021, 2, 22).strftime("%d/%m/%Y"),
            'due': datetime(2021, 3, 1).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        },
        {
            'id': '4',
            'name': 'Buy a new bike',
            'created': datetime(2021, 2, 24).strftime("%d/%m/%Y"),
            'due': datetime(2021, 6, 1).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', context=context)

def completed_list_show(request):
    tasks = [
        {
            'id': '0',
            'name': 'Take a shower',
            'created': datetime(2021, 2, 20).strftime("%d/%m/%Y"),
            'due': datetime(2021, 2, 21).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', context=context)