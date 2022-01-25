# Data-Science-Projects

## Mini Projects:

## Linear Regression:
This is a univariate Linear Regression where we have implemneted the following:
1. DataSet- The bike sharing data is a small data set with 2 features Population and Profit - That is how much profit was made per population for bike sales.
2. Loading the dataset and libraries - matplotlib, pandas, numpy, seaborn and Axes3D from mpl_toolkits.mplot3d
3. Visualizing the Data with Scatterplot from seaborn with Population on X-axis and Profits on y-axis.
4. Implementing the Cost function from scratch using numpy.
    Compute the Cost  𝐽(𝜃)
    The objective of linear regression is to minimize the cost function

    𝐽(𝜃)=12𝑚∑𝑖=1𝑚(ℎ𝜃(𝑥(𝑖))−𝑦(𝑖))2

    where  ℎ𝜃(𝑥)  is the hypothesis and given by the linear model

    ℎ𝜃(𝑥)=𝜃𝑇𝑥=𝜃0+𝜃1𝑥1
    
5. Implementing the Gradient Descent Using numpy and visualizing the 3D plot to find the global minima.
   Minimize the cost function  𝐽(𝜃)  by updating the below equation and repeat unitil convergence
   𝜃𝑗:=𝜃𝑗−𝛼1𝑚∑𝑚𝑖=1(ℎ𝜃(𝑥(𝑖))−𝑦(𝑖))𝑥(𝑖)𝑗  (simultaneously update  𝜃𝑗  for all  𝑗 ).

6. Plotting the Convergence of the Gradient Descent
   Plot  𝐽(𝜃)  against the number of iterations of gradient descent

7. Training the Data with Linear Regression Fit line
8. Finding the Inference using the optimized  𝜃  values
   Example 1: Prediction of the Profit value for the population of 40000 = $8781.0
   Example 2: Prediction of the Profit Value for the population of 83000 = $60069.0
   
## Multiple Linear Regression:
This is a mini project to build Multiple Linear Regression using different librarier in python- matplotlib, pandas, numpy, seaborn and Scikit-Learn.
Scikitl-learn is used to calculate the regression, pandas for data management and seaborn for plotting. 
Dataset: Adverstising dataset that predict sales revenue based on advertising spending through media such as TV, radio, and newspaper 
Problem Statement: How does different advertsing features affect the overall sales?

Implemented as Follows:
1. Importing all the necessary libraries
2. Load the Dataset
3. Determining the relationshp between the features(TV, radio, newspaper) vs Response(sales). We have used sns.pairplot to visualize the data distribution for each feature          against sales. 
4. Multiple Linear Regression - Determining the co-efficient
    Here we are determining the intercept and co-efficient for each feature and visualizing the outcome on a confusion matrix for which sns.heatmap is used.
5. Feature selection: To determine which feature can be kept or elimintaed. Calculating the r2_score for the predicted value for 2 different scenarios.
    a. For features TV and radio. R square value here is 0.89719
    b. For features TV, radio and newspaper. R square value here is 0.89721
    As you can see including newspaper does not have any significant effect on the R-square value.
6. Model Evaluation Using Train/Test Split and Metrics:
    In this step we checking if train/test split with RMSE to see whether newspaper should be kept in the model or not. We are calculating the RMSE for 2 scenarios and               comparing:
    a. For features TV and radio.
    RMSE:  1.3879034699382888
    R^2:  0.9176214942248908
    
    b. For features TV, radio and newspaper. RMSE value here is 0.89721
    RMSE:  1.4046514230328953
    R^2:  0.9156213613792232
    
    As per the outcome you can see that the RMSE increases by adding newspaper and Rsquare value decreases. For the better working model we should increase the R^2 value and         decrease the RMSE value. The RMSE value is less in a when compared to b. The best fit line was better for a and Hence we should remove newspaper from our model prediction. 
7. Interaction effect: Here we are including the product of TV and radio as interaction value and calculating RMSE and R square.
    and got RMSE:  0.7011871137164326 and R^2:  0.9789736814681261. The model has a best fit line here since R square value is 97 and RMSE got reduced to a great extent.

   
## End to End Project:   
## Wiki WebScrapping Flask Project:
This is a basic web application that performs the following tasks:
1. Display a initial web page which asks to Enter a topic to be searched in Wiki.
2. Extract the summary from the wikipage for the topic that was entered and this summary is stored in MongoDB Atlas.
3. Extract the reference links on the page and store it in the MongoDB atlas as a list.
4. Extract the images (.png, .jpeg, .jpg etc.,), Convert them to base64 format and store it in MongoDB Atlas.
5. Display step 2-3 in the table format in the web page.
6. Deploy the application on Heroku.
https://wiki-scrapper-project.herokuapp.com/
