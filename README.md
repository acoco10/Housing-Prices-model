# Housing-Prices-model
Linear regression model for housing prices

Business Problem

	Using a dataset that includes various features from homes in Kings County Seattle from 2014 until 2015, construct a model which predicts their prices. 

Process

	First exploratory data analysis (EDA) was performed to determine significant predictors of selling price for homes in the region. During this process T-tests, Anova tests, correlation matrices and data visualization were used. The view from the home, whether or not a home had a basement and whether a property was on the waterfront were all significant determinants of a higher average price. The correlation for price was strongest for square footage. Zip Code was used as a proxy for information on neighborhood determinants for price. With zip code and square footage using a multiple linear regression model, about 70% of the variation in housing prices was explained. The model was further fine tuned with view, the overall condition of the house, whether or not it was a waterfront property, when the house was sold and the number of bathrooms and bedrooms. 

![lat_long_data_viz](https://user-images.githubusercontent.com/61987208/96942363-f144af80-14a2-11eb-8637-770cacabc484.png)


	The resulting model explained about 85% of the variance in price with and R squared of .856. Then a test-train split was made to calculate root mean squared error. The model was off by about 70,000 on average but was bad at predicting expensive houses. 

