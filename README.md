# UNC_Analytics_Bootcamp_Capstone_2022
## Exploratory analysis of tick-borne illness in dogs

### Purpose
In this project, we explore data related to the geographic distribution and prevalence of tick species which carry pathogens that cause illness/disease in the US. We also look into veterinary data pertaining to symptom records and tick-borne illness testing. The goal of this study is to develop a model that could potentially predict the likelihood of a tick-borne illness before testing by analyzing the symptoms and ascertain whether there is a relationship between the recently recorded new migrations of ticks across the United States, and a higher number of tick-borne illness cases in dogs. 

- Questions the team hopes to answer with the data analysis:
    - Has the population of ticks increased within the United States?
    - Can Machine-Learning be utilized to effectively predict a tick-borne illness diagnoses?
    - Are any symptoms in particular better indicators for potential tick-borne illness?
    
![](Visualizations/Images/Tick-Identification.jpeg)

### Overview
1. Collect geographical data on tick species and veterinary data on tick-borne illness testing and diagnoses
2. Create a shared database to store data 
3. Use machine learning algorithms to make predictions based on data
4. Run statistical analysis on data
5. Create visualizations to display tick data and machine learning results

### Technologies Utilized
- Excel
    - VBA
- PostrgresSQL
- Amazon AWS
- Google Colab
    - Pandas and Scikit-Learn packages primarily
- R
- Tableau

(The requirements file has been created in order to import all the libraries and dependencies for this project located in the project root directory: [Requirements file](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/requirements.txt))

### Communication Protocols
The communication protocols selected are 'Slack' and 'Zoom' meetings; a Kanban board was used to track issues as we progressed to stay on task. 

### Data Sources
- Tick data sourced from the [CDC](https://www.cdc.gov/ticks/surveillance/TickSurveillanceData.html)
- Pet data sourced from a combination of [animal shelter data in TX](https://data.world/cityofaustin/9t4d-g238), various webpages detailing signs/symptoms of tick-borne illness in dogs, and some prior knowledge of veterinary practices.
    

### Data Exploration and Database Utilization
We began our data exploration with 3 types csv files:
- Tick survaillence datasets
- Animal shelter intake datasets
- Animal symptoms dataset

We started the data process by inspecting all the data ( categorizing the columns) and creating a ERD which we used to create and join our datasets into usable tables.

![QuickDB Diagram](/Visualizations/QuickDBD-Capstone%20(1).png)

The CSV files were imported into a database on PgAdmin, hosted on an Amazon AWS server, and aligned to a single table on the FIPSCode and State ids. Then, the tables were filtered to clean the data, which included removing columns from the tick data (data source) and the animal data (breed, color and name). These tables could then be used in training the models in machine learning. The tick tables were futher manipulated - differentiated by year - to create concise visualizations of tick migration in tableau.

### Machine Learning Model 
We tested both supervised and unsupervised algorithms to predict Negative vs. Positive test results. Our motivation for choosing the models that we did stemmed primarily from the type of data we had - specifically in the supervised models. The benefits of using the oversampling methods are that they are able to address imbalances in the data. Our data has more negative test results than positive - which reflects the frequencies seen in the real world - and so if we were to run our model without resampling, it would be biased towards the negative results and not be good at predicting positives. We decided against using undersampling models in order to prevent losing potentially important information. The RandomForest model is also a good model to use with imbalanced data and large datasets. For unsupervised learning, our primary goal was not only to make predictions and group the data points, but to use as a method to explore the data further.

The datasets were loaded into Google Colab through a connection to the SQL databese server. Once loaded, the data in table was cleaned further - removing columns that do not contribute to the model, changing some columns to have consistent units, changing colunms to only include continuous data (converting categorical data using the get_dummies method), and finally scaling the data. 

By remoivng certain rows from the data and changing their data types accordingly, we create the features for the models - those features being the symptoms.


#### Results:
_**Supervised**_

The features for these models were the symptoms columns in the data, and the Target was defined to be the test result (i.e. Negative or Positive). Within the data, we see many more negative tests than positive test, therefore the data is resampled and scaled for each model. Additionally, the data is split 75%-25% between the training and testing sets, as is default with the scikit-learn `train-test-split()` function.

*Naive Random Oversampling*

After the steps detailed previously are completed, we then were able to feed the data to the model from our training set and then have it make predictions for our test set. This model produced a balanced accuracy score of 0.956 (96.5%). Below depicts the confusion matix and classification table from this model.

|           |          |
|-----------|----------|
|![cm ROS]()|![class ROS]()|

We see here that the precision and sensitivity scores from this model are also very high.

*SMOTE Oversampling*

For the SMOTE model, we ran the same preprocessing steps and received a balanced accuracy score of 0.949 (95%). Below we show the confusion matrix and classifcation table.

|           |          |
|-----------|----------|
|![cm SMOTE]()|![class SMOTE]()|

Again, we have garnered very high precision and recall scores from this model.

*RandomForests*

Again, we followed similar proprocessing steps before running this model. We received an accuracy score of 1.0 (100%) and the confusion matrix and classification tables are shown below.

|           |          |
|-----------|----------|
|![cm RF]()|![class RF]()|

_**Unsupervised**_

The features for the model were created in the same steps detailed above.

*KMeans*




- Using Unsupervised model to predict Negative vs. Positive test – this model will receive an input from animals that were not tested to group them into “Possibly infected” and “Possibly uninfected”. 
- Description of how data was split into training and testing sets
    - Supervised: the Scikit-learn library will be used to split the data 75%-25% for our training - testing groups
- Explanation of model choice, including limitations and benefits
    - Limitations: Both include much categorical data – this could make the predictions weak because the discernment of the symptoms is mostly subjective.
    - Theoretical future study to correct for this: including more discrete data – possibly in the form of bloodwork values (i.e. chemistry panels, complete blood count(CBC), etc. - In vet practices, these tests would almost always be run along with the 4Dx test so the information should be readily available, just inaccessible within the scope of this project).

### Statistical Analysis


![Stats Results Plot](/Statistics/Test_result_prediction.png)
    
#### Third Segment - Machine Learning objective questions
Description of data preprocessing
- First, columns in the dataset that did not hold pertinent information for the analysis were dropped - animal id, state, sex, animal type, breed class, and color.
- Next, created a mask variable to filter out all the rows where the patients was 'Not Tested'
- Changed values in RR column to be all numerical
- Finally, 'age' column values needed to be changed into a number format
    - converted all ages to years

Description of feature engineering and the feature selection, including the decision-making process
- Feature selection set as the remaining columns after the preprocessing steps - age, weight, temp, HR, RR, MM, CRT, Mentation, and the other signs/symptoms.
    - These columns were chosen based off of what is known about how tick-borne diseases/illnesses manifest as physical symptoms
- The target variable was set to the column that details whether the patient tested 'Positive' or "Negative'
- Used the padas 'get_dummies' method to encode categorical data into numerical data
    - this created many more columns - from 18 to 47

Description of how data was split into training and testing sets
- Used the sklearn model_selection method 'train_test_split' to split data 
    - Deault 75% - 25% split
- The data was also scaled to account for the larger feature values

Explanation of model choice, including limitations and benefits
- Chose to use Oversampling models to compensate for the imbalance in the data - data favors negative tests (statistically more negative tests are seen in practice)
    - Benefits: By evening out the data, we can mitigate the chances for the model to be skewed towards the more populous event.
    - Limitations: By duplicating events int he minority group, we risk increasing the liklihood of overfitting in the model.

Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)
- In segment 2, one the naive oversampling method was tested. Here we have re-run the naive oversampling model with a new set of data that has more variation
- Additionally, we run the SMOTE oversampling model in this segment to compare the peformance results.

Description of how they have trained the model thus far, and any additional training that will take place
- The training data is fit to a logistic regression model
    - We use this model because our goal is for the model to classify inputs into two groups. The logisstic regression model is best for classifications.

Description of current accuracy score
- The accuracy score for these models were 96% (RandomeOverSampling) and 95% (SMOTE).

So far - at this point in the testing - the machine learning models are proving effective to answer our original questions
    
### Visualization
#### Entity Relational Database

o The Database Entity Relationship Diagram(ERD) was created as a preliminary step for the database portion. This allowed for a roadmap for the outcome of what our database would look like and how it would interact with the other moving parts of the project.

#### Density Map of Established Tick Records
![Density Map](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/Visualizations/texas_map.PNG)
o A map was created to show the categories of tick records per county in the United States. 

#### TickBorne dashboard

[Tableau Dashboard](https://public.tableau.com/app/profile/joseph.bloomfield/viz/Tableaudashboard_16673515630850/TickDashboard#1)

o We pulled from our database the tick-borne illnesses against the 'FIPSCODE'(Federal Information Processing Standard), which is a unique id by geographical area and 'Animial ID' from each county. Then, a density map was created based on the categories of "Established", "No Record", and "Reported". 

After further analysis and data cleaning we were able to use tickborne illnesses found by county with a positive and negative test value. the dashboard was updated to reflect the tickborne illness vs the number of ticks acroos the U.S. and specifically in texas

### Slides

--- Presentations are drafted in [Google Slides](https://docs.google.com/presentation/d/1Pb45MhAy0BsfN_zfLDYegSP01tUUemsadI_XG5e-pjA/edit?usp=sharing).

![Dashboard screnshot](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/Visualizations/Tickborne%20Dashboard.PNG)


### Recommendation for future analysis:
Potential research revolving around the migration of ticks and the many reasons that migration  may occur; examples including deforestation and climate change issues.
Future analysis concerning other strains of tick-borne diseases as it pertains to canines; also look into the existence of such tick-borne diseases in other animal populations.

### Items the team would have done differently:
To look into procuring animal shelter data from other states and counties.
Research other animals and how they have been affected throughout the years by these specific tick-borne diseases.


### Individual Branches:
- Joe B. - JB_dev;
- Denis A. - dang_dev; 
- Nichelle F. - Nichelle_dev; 
- ChiChi U. - ML_dev_primary; 
- Courtney B. - database_dev_second
