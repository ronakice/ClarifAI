from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID = "hkKSvf7n30mCvE5wyU_FIPQ6LYWlplqwSRKUtMpC"
CLARIFAI_APP_SECRET = "j8pMBAmY-FQCQqK3Vmd_nU7dhXkLKo3kWlWFO5qF"
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
#Can train models too
model = app.models.get("general-v1.3")

#picture of an Occupy Wall Street Rally
result = model.predict_by_url(url="https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/12/10/1386666757262/Occupy-Wall-Street-Holds--008.jpg")
concept_list = result["outputs"][0]["data"]["concepts"]
for concept in concept_list:
    print(str(concept["value"]) + "\t"+ concept["name"])


print("Best Prediction is : " +  concept_list[0]["name"])
#picture of a cat
result = model.predict_by_url(url="https://github.com/ronakice/ClarifAI/blob/master/Images/chettlescat.jpg?raw=true")
concept_list = result["outputs"][0]["data"]["concepts"]
for concept in concept_list:
    print(str(concept["value"]) + "\t"+ concept["name"])
