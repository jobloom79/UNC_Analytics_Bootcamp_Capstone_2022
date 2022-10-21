# UNC_Analytics_Bootcamp_Capstone_2022

## Exploratory analysis of tick-borne illness in dogs
In this project, we explore data related to the geographic distribution and prevalence of tick species which carry pathogens that cause illness/disease in the US. We also look into data pertaining to veterinary symptom records and tick-illness testing in order to develop a model that could potentially predict the likelihood of a tick-illness before testing by analyzing the symptoms. The goal of this study is to ascertain whether there is a relationship between the recently recorded new migrations of ticks across the US, and a higher number of tick-borne illness cases in dogs. 
### Overview of Project:
---This will be a comparison of number of dogs that is inprocessed and outprocessed in animal shelters in Austin Texas against the number of Tick Born illneses as reported by the CDC. From the analysis the goal is to see the correlation if any and be able to predict the likelihood of such diseases in other states.

### Description of technologies and communication protocols:
---The communication protocols selected are 'Slack' and 'Zoom' meetings. Also a Kanban board is being used to track issues as we progress to stay on task. 
-Tick data sourced from the CDC; Pet data sourced from a combination of animal shelter data, various webpages detailing signs/symptoms of tick-borne illness in dogs, and some prior knowledge.

---For technologies it was decided to use 'PostrgresSQL' for our database and we will connect the database to 'Google Colab' to run a predicted model to determine the outcome of our comparisons.

### Questions the team hopes to answer with the data
o	Has the prevalence of ticks increased around the US?

o	Can Machine-Learning be utilized to effectively predict tick-borne illness diagnoses?

o	Are any symptoms in particular better indicators for potential tick-borne illness?

#### Description of the data exploration phase of the project
o	Explore data pertaining to tick prevalence in the different regions of the US and how that has changed over the years. Looking at which species carry which
    pathogens (which in-turn causes particular illnesses). 
    ---Sample Hypothesis: The changes in tick species migration effects the prevalence of certain tickborne illnesses in areas where they were previously uncommon
    could lead to lack of treatment options to target the different illnesses (i.e. increased mortality rate)
o	Explore data pertaining to tick-borne illnesses in dogs – looking particularly at the signs and symptoms. Also, looking at potential treatment options. 
    Description of the analysis phase of the project
    ---Can run statistical analysis on the symptoms and how they relate to the the illness (essentially t-testing & chi2 testing to see if certain symptoms are
    statistically significant in predicting tick-borne illness)

Slides

    ---Presentations are drafted in Google Slides.
o	Description of preliminary feature engineering and preliminary feature selection, including the decision-making process
    (Potentially: )
    Using Supervised model to predict Negative vs. Positive test – model will take in information for each of the symptoms in order to predict the test outcome. 
    This will be using data set that only includes dogs that were tested
    Using Unsupervised model to predict Negative vs. Positive test – this model will use the information from animals that were not tested  to group them into
    “Possibly infected” and “Possibly uninfected”. 

o	Description of how data was split into training and testing sets
    For Supervised - 
o	Explanation of model choice, including limitations and benefits
    Limitations: Both include much categorical data – this could make the predictions weak because the discernment of the symptoms is mostly subjective
o	Theoretical future study to correct for this: including more discrete data – possibly in the form of bloodwork values (i.e. chemistry panels, complete blood count
    (CBC), etc) [In vet practices, these tests would almost always be run along with the 4Dx test so the information should be readily available, just inaccessible
    within the scope of this project.]
    
Visualization
o The Database Entity Relationship Diagram(ERD) was created as a preliminary step to for the database portion. This allowed for a roadmap for the outcome of what our database would look like and how it would interact with the other moving parts of the project [QuickDB Diagram]!
o We pulled from our Database the tick borne illnesses against the 'FIPSCODE' and 'animial id' in each county and created a density map based on the categories of "Established", "No Record", and "Reported" as described below [Tickborne Dashboard]!
o


### Individual Branches:
- Joe B. - JB_dev;
- Denis A. - dang_dev; 
- Nichelle F. - Nichelle_dev; 
- ChiChi U. - ML_dev_primary; 
- Courtney B. - database_dev_second
