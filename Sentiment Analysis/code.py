import csv
import numpy as np
from fractions import Fraction
from sklearn import metrics
import re
from collections import Counter

#Reading data from dataset csv

print("Commencing training from train dataset...")
# Read in the training data.
with open("dataset.csv", 'r') as file:
  view = list(csv.reader(file))
  reviews=[]
  for j in view:
      if j[0]=="train":
          reviews.append(j[1:])

print("Size of Train Dataset: "+ str(len(reviews)) + "\n")
negative_text = " ".join([r[0].lower() for r in reviews if r[1] == str("neg")])
positive_text = " ".join([r[0].lower() for r in reviews if r[1] == str("pos")])
negative_counts = Counter(re.split("\s+", negative_text))
positive_counts = Counter(re.split("\s+", positive_text))
positive_review_count=len([r for r in reviews if r[1] == str("pos")])
negative_review_count=len([r for r in reviews if r[1] == str("neg")])
prob_positive = positive_review_count / len(reviews)
prob_negative = negative_review_count / len(reviews)


#Training from dataser where we take all the probability of words into account.
def Training(text, counts, class_prob, class_count):
    lst=[]
    text_counts = Counter(re.split("\s+", text))
    for word in text_counts:
      aa=text_counts.get(word)
      bb=counts.get(word,0) + 1
      cc= sum(counts.values()) + class_count
      lst.append(float(aa*Fraction(bb,cc)))
    prediction = np.prod(np.array(lst))
    return prediction * class_prob

#here we input text and use the model we trained to get to know the of review are positive or negative of any text.
def Testing(text, Training):
    negative_prediction = Training(text, negative_counts, prob_negative, negative_review_count)
    positive_prediction = Training(text, positive_counts, prob_positive, positive_review_count)
    if negative_prediction > positive_prediction:
      return "neg"
    return "pos"

with open("dataset.csv", 'r') as file:
     est = list(csv.reader(file))
     test=[]
     for j in est:
         if j[0]=="test":
              test.append(j[1:])

print("Training completed.\n")
decide=input("Press 1 for predicting from data set. Press 2 for writing own review for prediction ")
#this takes input and we can also write live reviews which will help in determining positive or negative

if decide=="2":
    a=True
    print("*Press 2 to escape*")
    while a:
        new=input("")
        if new == "2":
            a=False
        else:
            print(Testing(new,Training))
elif decide=="1":
    print("Predicting from test dataset...")
    print("Size of Test Dataset: "+ str(len(test)) + "\n")
    predictions = [(Testing(r[0], Training)) for r in test]
    actual = [(r[1]) for r in test]
    print("Obtaining recognition rate\n")
    for i in range(len(predictions)):
        if predictions[i]=="pos":
            predictions[i]=1
        else:
            predictions[i]=-1

    for i in range(len(actual)):
        if actual[i]=="pos":
            actual[i]=1
        else:
            actual[i]=-1
    #using matrices and prediction and actual data in the particular format to determine the recognition rate.
    fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
    print("Recognition rate is: {0}".format(metrics.auc(fpr, tpr)))



