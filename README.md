# UNC_Analytics_Bootcamp_Capstone_2022
## Exploratory analysis of tick-borne illness in dogs

In this project, we explore data related to the geographic distribution and prevalence of tick species which carry pathogens that cause illness/disease in the US. We also look into data pertaining to veterinary symptom records and tick-borne illness testing in order to develop a model that could potentially predict the likelihood of a tick-borne illness before testing by analyzing the symptoms. The goal of this study is to ascertain whether there is a relationship between the recently recorded new migrations of ticks across the United States, and a higher number of tick-borne illness cases in dogs. 


### Overview of Project:

This will be a comparison of number of dogs that are inprocessed and outprocessed in animal shelters in Austin, Texas against the number of tick-borne illneses as reported by the CDC. From the analysis the goal is to see the correlation, if any, and to predict the likelihood of such diseases in other states.


### Description of technologies and communication protocols:

- The communication protocols selected are 'Slack' and 'Zoom' meetings; a Kanban board is being used to track issues as we progress to stay on task. 

- Tick data sourced from the CDC; Pet data sourced from a combination of animal shelter data in Austin, TX, various webpages detailing signs/symptoms of tick-borne illness in dogs, and some prior knowledge.

- Technologies:
    - PostrgresSQL 
    - Google Colab
        - Pandas and Scikit-Learn
    - Excel
        - VBA
    - Amazon AWS
    - Tableau
    

### Questions the team hopes to answer with the data

o	Has the population of ticks increased within the United States?

o	Can Machine-Learning be utilized to effectively predict a tick-borne illness diagnoses?

o	Are any symptoms in particular better indicators for potential tick-borne illness?


### Description of the data exploration phase of the project

- Explore data pertaining to tick prevalence in the different regions of the United States and how that has changed over the years. Looking at which species carry which pathogens (which in-turn causes particular illnesses). 
    - Sample Hypothesis: The changes in tick species migration effects the prevalence of certain tick-borne illnesses in areas where they were previously uncommon could lead to lack of treatment options to target the different illnesses (i.e. increased mortality rate)
- Explore data pertaining to tick-borne illnesses in dogs – looking particularly at the signs and symptoms. Also, looking at potential treatment options. 


### Description of the analysis phase of the project
- Can run statistical analysis on the symptoms and how they relate to the the illness (essentially t-testing & chi2 testing to see if certain symptoms are statistically significant in predicting tick-borne illness)


### Slides

--- Presentations are drafted in [Google Slides](https://docs.google.com/presentation/d/1Pb45MhAy0BsfN_zfLDYegSP01tUUemsadI_XG5e-pjA/edit?usp=sharing).

### Machine Learning Model 
- Description of preliminary data preprocessing
    - Data in table will need to be cleaned - removing columns that do not contribute to the model, changing some columns to have consistent units, changing colunms to only include continuous data (converting categorical data using the get_dummies method), and finally scaling the data
- Description of preliminary feature engineering and preliminary feature selection, including the decision-making process
    - The feature engineering is breifly touched on in the last point - by remoivng certain rows from the data  and changing their data types accordingly, we create the features for the model
        - Using Supervised model to predict Negative vs. Positive test – model will receive an input for each symptom in order to predict the test outcome. This will use data set that only includes dogs that were tested
        - Using Unsupervised model to predict Negative vs. Positive test – this model will receive an input from animals that were not tested to group them into “Possibly infected” and “Possibly uninfected”. 
- Description of how data was split into training and testing sets
    - Supervised: the Scikit-learn library will be used to split the data 75%-25% for our training - testing groups
- Explanation of model choice, including limitations and benefits
    - Limitations: Both include much categorical data – this could make the predictions weak because the discernment of the symptoms is mostly subjective.
    - Theoretical future study to correct for this: including more discrete data – possibly in the form of bloodwork values (i.e. chemistry panels, complete blood count(CBC), etc. - In vet practices, these tests would almost always be run along with the 4Dx test so the information should be readily available, just inaccessible within the scope of this project).
    
### Visualization

#### Entity Relational Database
![QuickDB Diagram](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/Visualizations/QuickDBD-Capstone%20(1).png)
o The Database Entity Relationship Diagram(ERD) was created as a preliminary step for the database portion. This allowed for a roadmap for the outcome of what our database would look like and how it would interact with the other moving parts of the project.

#### Density Map of Established Tick Records
![Density Map](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/Visualizations/texas_map.PNG)
o A map was created to show the categories of tick records per county in the United States. 

#### TickBorne dashboard
![Tickborne Dashboard](https://github.com/jobloom79/UNC_Analytics_Bootcamp_Capstone_2022/blob/customer_acceptance_test/Visualizations/Tickborne%20Dashboard.PNG)
o We pulled from our database the tick-borne illnesses against the 'FIPSCODE'(Federal Information Processing Standard), which is a uniquely id by geographical area and 'Animial ID' from each county. Then, a density map was created based on the categories of "Established", "No Record", and "Reported". 

### Individual Branches:
- Joe B. - JB_dev;
- Denis A. - dang_dev; 
- Nichelle F. - Nichelle_dev; 
- ChiChi U. - ML_dev_primary; 
- Courtney B. - database_dev_second
