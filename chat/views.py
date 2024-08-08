from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
def chat_view(request):
    return render(request, 'chat/chat.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message', '')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            message = response.choices[0].message['content']
            return JsonResponse({'message': message})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
