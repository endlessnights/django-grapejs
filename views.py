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


def save_exported_content(request, page_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        html_content = data.get('html_content', '')
        css_content = data.get('css_content', '')

        try:
            page_instance = Page.objects.get(pk=page_id)
            page_instance.html_content = html_content
            page_instance.css_content = css_content
            page_instance.save()

            return JsonResponse({'success': True})
        except Page.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Page not found.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
