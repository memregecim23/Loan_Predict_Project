import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfloan = pd.read_csv("Loan.csv")
dfloan.head()
dfloan.info()
dfloan.describe()
dfloan.isnull().sum()

dfloan["year"] = pd.to_datetime(dfloan["ApplicationDate"]).dt.year
dfloan["month"] = pd.to_datetime(dfloan["ApplicationDate"]).dt.month
dfloan["day"] = pd.to_datetime(dfloan["ApplicationDate"]).dt.day
dfloan.info()
dfloan.drop(["ApplicationDate"], axis=1, inplace=True)
dfloan.info()

dfloan["EmploymentStatus"].value_counts() #3 adet unique değer one-hot encoder
dfloan["EducationLevel"].value_counts() # 5 adet unique değer ordinal encoder
dfloan["MaritalStatus"].value_counts()  # 4 adet unique değer one-hot encoder
dfloan["HomeOwnershipStatus"].value_counts() # 4 adet unique değer ordinal encoder
dfloan["LoanPurpose"].value_counts() # 5 adet unique değer one-hot encoder

dfencoded = pd.get_dummies(dfloan,columns=["LoanPurpose","EmploymentStatus","MaritalStatus"])
dfencoded.info()

dfloan["EducationLevel"].value_counts()
from sklearn.preprocessing import OrdinalEncoder
education_level = [["High School","Associate","Bachelor","Master","Doctorate"]]
ordinal = OrdinalEncoder(categories=education_level)
dfencoded["Educationlevelencoded"] = ordinal.fit_transform(dfencoded[["EducationLevel"]])
dfencoded["Educationlevelencoded"] = dfencoded["Educationlevelencoded"].astype(int)
dfencoded.drop("EducationLevel", axis=1, inplace=True)

dfloan["HomeOwnershipStatus"].value_counts()
status_level = [["Other","Rent","Mortgage","Own"]]
ordinal2 = OrdinalEncoder(categories=status_level)
dfencoded["HomeOwnershipStatusencode"] = ordinal2.fit_transform(dfencoded[["HomeOwnershipStatus"]])
dfencoded["HomeOwnershipStatusencode"] = dfencoded["HomeOwnershipStatusencode"].astype(int)
dfencoded.drop("HomeOwnershipStatus", axis=1, inplace=True)
dfencoded.info()
dfencoded.describe()
dfencoded.corr()["LoanApproved"].sort_values()

drop_list = [
    "EmploymentStatus_Unemployed",
    "TotalLiabilities",
    "LoanPurpose_Other",
    "month",
    "CreditCardUtilizationRate",
    "MaritalStatus_Widowed",
    "NumberOfCreditInquiries",
    "year",
    "LoanPurpose_Debt Consolidation",
    "NumberOfOpenCreditLines",
    "LoanPurpose_Home",
    "MaritalStatus_Married",
    "day",
    "DebtToIncomeRatio",
    "MaritalStatus_Single",
    "CheckingAccountBalance",
    "SavingsAccountBalance",
    "NumberOfDependents",
    "UtilityBillsPaymentHistory",
    "LoanPurpose_Auto",
    "JobTenure",
    "EmploymentStatus_Employed",
    "MaritalStatus_Divorced",
    "LoanPurpose_Education",
    "EmploymentStatus_Self-Employed",
    "PaymentHistory",
    "HomeOwnershipStatusencode",
    "AnnualIncome",
    "RiskScore"
]
existing_drop_list = [col for col in drop_list if col in dfencoded.columns]
X = dfencoded.drop(existing_drop_list, axis=1)

y = dfencoded["LoanApproved"]
if "LoanApproved" in X.columns:
    X = X.drop("LoanApproved", axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)

X_train.info()

import lightgbm as lgb
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
lgbm = lgb.LGBMClassifier(verbosity=-1,is_unbalance=True)
lgbm.fit(X_train, y_train)
y_pred = lgbm.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(report)
print(matrix)
print(accuracy)

from sklearn.model_selection import RandomizedSearchCV
param = {
    "n_estimators": [100, 300, 500, 1000],
    "max_depth": [3, 5, 7, -1],
    "learning_rate": [0.01, 0.05, 0.1, 0.3],
    "num_leaves": [15, 31, 63, 127],
    "min_child_samples": [5, 10, 20],
    "subsample": [0.6, 0.8, 1.0],
    "colsample_bytree": [0.6, 0.8, 1.0]
}

grid = RandomizedSearchCV(estimator=lgbm,param_distributions=param,cv=5,scoring="accuracy",n_jobs=-1,verbose=1,n_iter=100)
grid.fit(X_train,y_train)
y_predgrid = grid.predict(X_test)

matrixgrid = confusion_matrix(y_test, y_predgrid)
reportgrid = classification_report(y_test, y_predgrid)
accuracygrid = accuracy_score(y_test, y_predgrid)
print(report)
print(matrix)
print(accuracygrid)

model = grid.best_estimator_

import joblib
model_dosya = "loan_model.pkl"
joblib.dump(model,model_dosya)
print("Model başarıyla oluşturuldu")

