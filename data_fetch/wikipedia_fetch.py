import wikipedia

def get_wikipedia_summary(topic, sentences=10):
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except Exception as e:
        return f"Error fetching Wikipedia data: {str(e)}"
