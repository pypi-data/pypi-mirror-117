import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error,r2_score,precision_score, recall_score, f1_score
from scipy.stats import jarque_bera,kurtosis,skew
class Descent:
    def __init__(self,X:list,y:list,epoch:int,method='linear',theta=None,alpha=0.01,decimals=5) -> None:
        """Constructs an instance of 

        Args:
            X (list): The independent variables
            y (list): The dependent variable
            theta (list): The initialized weights/thetas for regression. Defaults to None
            alpha (float): The learning rate for the regression. Defaults to 0.01
            epoch (int): The number of iterations to be performed during regression
            decimals (int, optional): The number of decimal places till which the early stopping can be implpemented. Defaults to 5.

        Returns:
            None
        """       
        self.method = method
        if self.method.strip().lower() not in ['linear','logistic']:
            raise TypeError('Method should either be linear or logistic')
        self.X = np.array(X)
        self.y = np.array(y)
        self.theta = theta
        self.alpha = alpha
        self.epoch = epoch
        self.decimals = decimals
        self.m = self.y.size
        self.n = self.X.shape[1]
        if self.theta is None:
            self.theta = np.random.randn(self.n,1)
        try:
            assert self.y.shape == (self.m,1)
            assert self.X.shape == (self.m, self.n)
            assert self.theta.shape == (self.n, 1)
        except AssertionError:
            print('The dimensions are incorrect, please check your data')
    def fit(self)->tuple:
        """Perform gradient descent with specified parameters for linear as well as logistic regression

        Returns:
            tuple: A tuple containing history of costs, thetas and the epoch at which we stop
        """         
        past_cost = []
        past_theta = [self.theta]
        m = self.y.size
        n = self.X.shape[1]
        for i in range(self.epoch):
            if self.method.strip().lower() == 'linear':
                h_theta = np.dot(self.X,self.theta)
                error = h_theta-self.y
                cost = np.dot(error.T, error)/(2*m)
            elif self.method.strip().lower() == 'logistic':
                z_theta = np.dot(self.X, self.theta)
                h_theta = 1/(1+np.exp(-z_theta))
                error = h_theta-self.y
                cost = -np.mean((self.y*np.log10(h_theta))+((1-self.y)*np.log10(1-h_theta)))            
            past_cost.append(cost)
            diff = np.dot(self.X.T, error)/m
            self.theta = self.theta - (self.alpha*diff)
            past_theta.append(self.theta)
            if np.equal(np.round(past_theta[i],decimals=self.decimals),np.round(self.theta,decimals=self.decimals)).sum() == n:
                break
        return np.array(past_cost).reshape(-1,1), np.array(past_theta), i+1
    def predict(self, values:list)->tuple:
        """Performs predictions with the best theta available

        Args:
            values (list): The values on which you want to predict

        Returns:
            tuple: A tuple containing best theta and the array of predictions
        """        
        past_cost, past_theta, stop_epoch = self.fit()
        best_theta = past_theta[-1]
        if self.method.strip().lower() == 'linear':
            predictions = np.dot(values,best_theta)
        elif self.method.strip().lower() == 'logistic':
            preds = 1/(1+np.exp(-np.dot(values,best_theta)))
            predictions = np.array([1 if i>0.5 else 0 for i in preds])
        return best_theta, predictions
    @property
    def summary(self)->pd.DataFrame:
        """Prints a summary of the regression containing the following values 
        1) Skewness of residuals 
        2) Kurtosis of residuals 
        3) Jarque Bera score of the residuals 
        4) P-Value of the Jarque Bers scores 
        5) R Squared of the model 
        6) Adjusted R Squared of the model 
        7) Mean Squared Error of the regression

        Returns:
            pd.DataFrame: A DataFrame containing the summary statistics
        """        

        best_theta, predictions = self.predict(values=self.X)
        predictions = predictions.reshape(-1,1)
        residuals = self.y-predictions
        kurt = kurtosis(residuals)
        skewness = skew(residuals)
        jb, p_value = jarque_bera(residuals)
        params_names = ['Skewess(residuals)','Kurtosis(residuals)','Jarque Bera Coef','Jarque Bera p-value']
        params_list = [skewness,kurt,jb,p_value]
        if self.method.strip().lower() == 'linear':
            r_squared = r2_score(y_true=self.y, y_pred=predictions)
            mse = mean_squared_error(y_true=self.y, y_pred=predictions)
            adj_rsq = 1-((1-r_squared)*(self.m-1))/(self.m-self.n-1)
            params_names.extend(['R Squared','Adjusted R squared','MSE'])
            params_list.extend([r_squared,adj_rsq,mse])
        else:
            precision = precision_score(y_true=self.y, y_pred=predictions)
            recall = recall_score(y_true=self.y, y_pred=predictions)
            f1 = f1_score(y_true=self.y, y_pred=predictions)
            params_names.extend(['Precision','Recall','F1-Score'])
            params_list.extend([precision,recall,f1])
        summary_df = pd.DataFrame(index=params_names)
        summary_df['Values'] = params_list
        return summary_df
    def __repr__(self) -> str:
        return  f'''
This model has been initialized for 
Method -> {self.method}
X -> {self.X.shape}
y -> {self.y.shape}
Initial theta -> {self.theta.reshape(-1,)}
Learning Rate -> {self.alpha}
Iterations -> {self.epoch}
Decimal Places -> {self.decimals}
        '''

class Preprocess:
    def __init__(self,data):
        """Initializes all the mean and the standard deviation values for the given data 

        Args:
            data (np.array or pd.Series or pd.DataFrame): The data you wouuld like to transform 
        """        
        self.data = data
        self.mean = data.mean()
        self.std = data.std()
    def transform(self,add_ones=True)->np.array:
        """Normalizes the data according to the formula x_norm = (x-mean(x))/std(x)

        Args:
            add_ones (bool, optional): Whether you want to add ones for intercept or not. Defaults to True.

        Returns:
            np.array: an array of transformed data
        """        
        norm = (self.data - self.mean)/self.std
        if add_ones:
            ones = np.ones(shape=(self.data.shape[0],1))
            result = np.concatenate((ones,norm),axis=1)
            return result
        else:
            return norm
    def inverse_transform(self,inp):
        """Reverses the normalization by using the formula x = (x_norm*std(x))+mean(x)

        Args:
            inp (np.array or pd.Series or pd.DataFrame): The normalized data which you would like to convert to original data

        Returns:
            The converted data
        """        
        return (inp*self.std)+self.mean