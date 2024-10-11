import numpy as np
X=[]
y=[]

def traing():
    training_data = np.loadtxt(r"C:\Users\LENOVO\PycharmProjects\FakeNewsDetection\dataset.txt", dtype=str, delimiter=",")
    for record in training_data:
        print(record)

        if record[0] != '':
            try:
                lis = []
                lis.append(float(record[0]))
                lis.append(float(record[1]))
                lis.append(float(record[2]))
                lis.append(float(record[3]))
                lis.append(float(record[4]))



                X.append(lis)
                y.append(record[5])
            except:
                pass

traing()
algo=[]
accuracylist=[]
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay


from sklearn.model_selection import train_test_split


from sklearn.ensemble import RandomForestClassifier


import matplotlib.pyplot as plt


data_set=None



clf = RandomForestClassifier(max_depth=2, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
def rftrain(X,y):
    print("started")

    clf.fit(X, y)



    rf_predictions = clf.predict(X_test)


    count=0
    for i in range(0,len(y_test)):

        if rf_predictions[i]==y_test[i]:
            count=count+1


    print("=====RFC=======")

    acc=count/len(y_test)
    print("Accuracy=============")
    print(acc)
    algo.append("RF")
    accuracylist.append(acc)
    cm = confusion_matrix(y_test, rf_predictions)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=clf.classes_)
    disp.plot()

    plt.show()


    print(cm)

rftrain(X, y)

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

knn_predictions = neigh.predict(X_test)


count=0
for i in range(0,len(y_test)):

    if knn_predictions[i]==y_test[i]:
        count=count+1
print("====KNN=====")
acc=count/len(y_test)
print("Accuracy=============")
print(acc)
cm = confusion_matrix(y_test, knn_predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=neigh.classes_)
disp.plot()

plt.show()

algo.append("KNN")
accuracylist.append(acc)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=0)
lr .fit(X, y)
lr_predict= lr.predict((X_test))

count=0
for i in range(0,len(y_test)):

    if lr_predict[i]==y_test[i]:
        count=count+1
print("====LR=====")
acc=count/len(y_test)
print("Accuracy=============")
print(acc)
cm = confusion_matrix(y_test, lr_predict)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=lr.classes_)
disp.plot()

plt.show()

algo.append("LR")
accuracylist.append(acc)



from sklearn import tree
dtc = tree.DecisionTreeClassifier()
dtc = clf.fit(X, y)

tree_predict= dtc.predict(X_test)

count=0
for i in range(0,len(y_test)):

    if tree_predict[i]==y_test[i]:
        count=count+1
print("====Decision Tree=====")
acc=count/len(y_test)
print("Accuracy=============")
print(acc)
cm = confusion_matrix(y_test, tree_predict)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=dtc.classes_)
disp.plot()

plt.show()
algo.append("DT")
accuracylist.append(acc)




from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()


gnb = gnb.fit(X, y)
naive_prediction=gnb.predict(X_test)

count=0
for i in range(0,len(y_test)):

    if naive_prediction[i]==y_test[i]:
        count=count+1
print("====Naive Bayes=====")
acc=count/len(y_test)
print("Accuracy=============")
print(acc)
cm = confusion_matrix(y_test, naive_prediction)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=gnb.classes_)
disp.plot()

plt.show()

algo.append("NB")
accuracylist.append(acc)


print(cm)
print("SVM")
from sklearn import svm

clf = svm.SVC()
clf.fit(X, y)


svm_prediction=clf.predict(X_test)

count=0
for i in range(0,len(y_test)):

    if svm_prediction[i]==y_test[i]:
        count=count+1
print("====SVM=====")
acc=count/len(y_test)
print("Accuracy=============")
print(acc)
cm = confusion_matrix(y_test, svm_prediction,labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=clf.classes_)
disp.plot()

plt.show()
algo.append("SVM")
accuracylist.append(acc)



def predict_function(f):
    rf_predictions = clf.predict(f)
    print (rf_predictions[0])
    return rf_predictions[0]



print("algorithm", algo)
print("accuracy",accuracylist)



import matplotlib.pyplot as plt
import numpy as np
x = np.array(algo)
y = np.array(accuracylist)

plt.bar(x,y)
plt.show()






