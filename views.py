from django.shortcuts import render, redirect, get_object_or_404

def grapejs(request, page_id):
    page_instance = get_object_or_404(Page, pk=page_id)
    print(page_instance)
    return render(request, 'front/grapejs.html', {'page_instance': page_instance})
