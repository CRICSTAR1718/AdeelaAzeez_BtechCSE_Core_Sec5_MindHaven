from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.http import require_http_methods
from myapp.models import Events, JournalEntry 
from datetime import datetime
import logging
import traceback
import json

logger = logging.getLogger(__name__)

# Create your views here.

def homePage(request):
    return render(request,"firstpage.html")

def nj(request):
    return render(request,"newjournal.html")

def blogweb(request):
    return render(request,"sirblogwebsite.html")

def Account(request):
    return render(request,"account.html")
def Sign(request):
    return render(request,"signup.html")
def log(request):
    return render(request,"login.html")

@ensure_csrf_cookie
def journal(request):
    return render(request, "journalexisting.html")

# def moodtracker(request):
#     return render(request,"moodtracker.html")


def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'moodtracker.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

@require_http_methods(["GET"])
def get_journal_entries(request):
    try:
        entries = JournalEntry.objects.all().order_by('-date')
        entries_data = [{
            'id': entry.id,
            'date': entry.date.strftime('%Y-%m-%d'),
            'content': entry.content
        } for entry in entries]
        return JsonResponse({'entries': entries_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def add_journal_entry(request):
    try:
        data = json.loads(request.body)
        date = datetime.strptime(data.get('date'), '%Y-%m-%d').date()
        content = data.get('content')
        
        if not content:
            return JsonResponse({'error': 'Content is required'}, status=400)
            
        entry = JournalEntry.objects.create(
            date=date,
            content=content
        )
        
        return JsonResponse({
            'status': 'success',
            'entry': {
                'id': entry.id,
                'date': entry.date.strftime('%Y-%m-%d'),
                'content': entry.content
            }
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_journal_entry(request, entry_id):
    try:
        entry = JournalEntry.objects.get(id=entry_id)
        entry.delete()
        return JsonResponse({'status': 'success'})
    except JournalEntry.DoesNotExist:
        return JsonResponse({'error': 'Entry not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)