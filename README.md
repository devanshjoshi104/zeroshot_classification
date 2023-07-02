# zeroshot_classification

Zero-shot classification is a machine learning technique where a model is trained to classify examples into classes that it has never seen during the training phase. In other words, the model can generalize to unseen classes.

When you run the server  the zero-shot classification API is accessible at http://localhost:8000/classifier/classify/ via the POST method. You can send a JSON payload with the labels and text fields to classify the text.
Make sure you have Django and the Transformers library installed in your Python environment. You can install them using pip install django transformers.


make sure JSON should of the from
{
  "labels": ["travel", "food", "sports"],
  "text": [
    "I want to book a flight to Paris.",
    "What are the best restaurants in town?",
    "Who won the recent football match?"
  ]
}

