from django.shortcuts import render

# Create your views here.
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_pdf_summaries(request):
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'summary_data.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
