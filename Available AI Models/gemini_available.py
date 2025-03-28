import google.generativeai as genai

genai.configure(api_key="AIzaSyBPBDiI75MN2GoZGgFxjOmd5HE8C7LMtiA")

models = genai.list_models()
for model in models:
    print(model.name)
