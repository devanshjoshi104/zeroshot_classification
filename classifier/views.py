from django.http import JsonResponse
from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

def classify_text(request):
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.POST.dict()

        # Extract labels and text from the JSON data
        labels = data.get('labels')
        text = data.getlist('text')

        # Perform zero-shot classification for each text
        results = []
        for t in text:
            result = classifier(t, labels)
            results.append({
                'text': result['sequence'],
                'predicted_label': result['labels'][0],
                'score': result['scores'][0]
            })

        # Prepare the response JSON
        response = {
            'results': results
        }

        # Return the response JSON
        return JsonResponse(response)

    # Return an error response for other HTTP methods
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
