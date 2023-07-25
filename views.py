from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def grapejs(request, page_id):
    page_instance = get_object_or_404(Page, pk=page_id)
    print(page_instance)
    return render(request, 'front/grapejs.html', {'page_instance': page_instance})


@csrf_exempt
def save_page(request, page_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        page_instance = Page.objects.get(pk=page_id)  # Get the specific Page instance to update
        page_instance.content = json.dumps(data)  # Save the JSON content to the model field
        page_instance.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
