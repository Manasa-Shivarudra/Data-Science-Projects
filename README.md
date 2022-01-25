# Data-Science-Projects

## Linear Regression:
This is a univariate Linear Regression where we have implemneted the following:
1. The bike sharing data is a small data set with 2 features Population and Profit - That is how much profit was made per population for bike sales.
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
   
# End to End Project:   
## Wiki WebScrapping Flask Project:
This is a basic web application that performs the following tasks:
1. Display a initial web page which asks to Enter a topic to be searched in Wiki.
2. Extract the summary from the wikipage for the topic that was entered and this summary is stored in MongoDB Atlas.
3. Extract the reference links on the page and store it in the MongoDB atlas as a list.
4. Extract the images (.png, .jpeg, .jpg etc.,), Convert them to base64 format and store it in MongoDB Atlas.
5. Display step 2-3 in the table format in the web page.
6. Deploy the application on Heroku.
https://wiki-scrapper-project.herokuapp.com/
