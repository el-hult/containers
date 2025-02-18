from transformers import pipeline
classifier = pipeline("sentiment-analysis")
ans =classifier("We are very happy to show you the 🤗 Transformers library.")
print(ans)
