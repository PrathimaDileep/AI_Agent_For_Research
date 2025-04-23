from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_tokens=400):
    try:
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        summaries = [summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]["summary_text"] for chunk in chunks]
        return "\n".join(summaries)
    except Exception as e:
        return f"Summarization error: {str(e)}"