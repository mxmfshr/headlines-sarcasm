from joblib import load

def predict(text):
    res = model.predict([text])[0]
    return "Sarcastic" if res else "Acclaim"

model = load('model.pkl')
print('ready')
while True:
  text = input()
  print(predict(text))
