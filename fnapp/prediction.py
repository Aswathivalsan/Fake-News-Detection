import numpy as np
X=[]
y=[]
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
def traing():
    training_data = np.loadtxt(r"C:\Users\LENOVO\PycharmProjects\FakeNewsDetection\dataset.txt", dtype=str, delimiter=",")
    for record in training_data:


        if record[0] != '':
            try:
                lis = []
                lis.append(float(record[0]))
                lis.append(float(record[1]))
                lis.append(float(record[2]))


                X.append(lis)
                y.append(record[5])
            except:
                pass

traing()
algo=[]
accuracylist=[]

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier




data_set=None







X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree


rf = RandomForestClassifier(max_depth=2, random_state=0)
knn = KNeighborsClassifier(n_neighbors=3)
dt = tree.DecisionTreeClassifier()



ensemble_model = VotingClassifier(estimators=[
    ('random_forest', rf),
    ('decision_tree', dt),
    ('knn', knn)
], voting='hard')

ensemble_model.fit(X, y)


Y_pred = ensemble_model.predict(X_test)


accuracy = accuracy_score(y_test, Y_pred)
print(f"Ensemble model accuracy: {accuracy:.2f}")


def predict_fakenews_fn(r):
    print(r[0],"====================")

    rr = ensemble_model.predict([r])
    print(rr[0],"=================")
    if  str(rr[0])=="0":
        if r[0]>0.39:
            return "Real"
        else:
            return "Fake"
    else:
        print("else")
        return "Real"
