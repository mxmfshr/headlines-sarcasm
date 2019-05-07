def headline_processing(text, model):
    res = model.predict([text])[0]
    return "Sarcastic" if res else "Acclaim"
