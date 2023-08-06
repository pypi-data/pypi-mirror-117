This code has two classes <br>
1. Preprocess - For preprocessing and normalizing the data 
2. Descent - For performing the gradient descent

# Descent Class 

## Constructor
```python
def __init__(self,X:list,y:list,epoch:int,method='linear',theta=None,alpha=0.01,decimals=5) -> None:
# Usage 
# Goal - to construct a linear regression for specified hyperparameters
gd = Descent(X=X_norm, y=y_norm, epoch=5000,alpha=0.01)
```
Constructs the Descent instance with the specified hyperparameters<br>
Parameters:<br>
1. X (list): The independent variables
2. y (list): The dependent variable
3. epoch (int): The number of iterations to be performed during regression
4. Method (str, optional): The method by which you would like to solve the gradient descent problem. Defaults to 'linear'
5. theta (list): The initialized weights/thetas for regression. Defaults to None
6. alpha (float): The learning rate for the regression. Defaults to 0.01
7. decimals (int, optional): The number of decimal places till which the early stopping can be implpemented. Defaults to 5.

## Fit function 
```python
def fit(self)->tuple:
# Goal - to calibrate the linear regression model 
pastCost,pastTheta,stopEpoch = gd.fit()
```
Calibrates the coefficient for gradient descent <br>
Returns:<br>
1. pastCost - The history of costs incurred by the model while performing the iterations 
2. pastTheta - The history of thetas calculated by the model while performing the iterations 
3. stopEpoch - The epoch at which the gradient descent model converged for the specified decimal places 

## Predict function 
```python
def predict(self, values:list)->tuple:
# Goal - to predict the coefficients for the test set 
bestTheta, preds = gd.predict(X_test)
```
Predicts the output for the specified values 
Parameters<br>
1. values - The values for which you would like to perform the predictions 
Returns<br>
1. bestTheta - The optimised value for theta after gradient descent 
2. predictions - The predictions for those values 

# Attributes
``` python
@property
def summary(self)->pd.DataFrame:
```
Prints the summary of the regression along with the necessary descriptive statistics<br>
Returns the following metrics 
1. Skewness of residuals 
2. Kurtosis of residuals
3. Jarque Bera Coefficient 
4. Jarque Bera p-value

If the model is linear, it also returns 

*  R Squared 
* Adjusted R Squared
* Mean Squared Error 

If the model is logistic, it also returns 

* Precision 
* Recall 
* F1 Score 

# Preprocess class

## Constructor 
```python 
def __init__(self,data):
# Goal - to create a preprocess instance for x
X_scaler = Preprocess(X)
```
Stores the mean and standard deviation of the data for future transformations 

## transform function 
```python
def transform(self,add_ones=True)->np.array:
# Goal - to normalize the ddata and concatenate ones in the begining 
X1 = X_scaler.transform(add_ones=True)
```
Normalizes the inputs by using the formula x_norm = (x-mean(x))/std(x)<br>
Arguments:
1. add_ones (bool, optional): Whether you want to add ones for intercept or not. Defaults to True.<bradd >
Returns the normalized data

## inverse_transform function 
```python 
def inverse_transform(self,inp):
#goal - to invert the transformation on the data 
x_rescaled = X_scaler.inverse_transform()
```
Reverses the normalization by using the formula x = (x_norm*std(x))+mean(x)<br>
Arguments
1. inp (np.array or pd.Series or pd.DataFrame): The normalized data which you would like to convert to original data

Returns the converted data