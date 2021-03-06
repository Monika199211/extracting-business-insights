# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(path)

def visual_summary(type_, df, col):
    """Summarize the Data using Visual Method.
    
    This function accepts the type of visualization, the data frame and the column to be summarized.
    It displays the chart based on the given parameters.
    
    Keyword arguments:
    type_ -- visualization method to be used
    df -- the dataframe
    col -- the column in the dataframe to be summarized
    """
    df[col].value_counts().plot(kind=type_)
visual_summary('bar',df,"banking_crisis")  
    




def central_tendency(type_, df, col):
    """Calculate the measure of central tendency.
    
    This function accepts the type of central tendency to be calculated, the data frame and the required column.
    It returns the calculated measure.
    
    Keyword arguments:
    type_ -- type of central tendency to be calculated
    df -- the dataframe
    col -- the column in the dataframe to do the calculations
    
    Returns:
    cent_tend -- the calculated measure of central tendency
    """
    cent_tend= df[col].apply(type_)
    return cent_tend

central_tendency('mean',df,'exch_usd')


    
    


def measure_of_dispersion(type_, df, col):
    """Calculate the measure of dispersion.
    
    This function accepts the measure of dispersion to be calculated, the data frame and the required column(s).
    It returns the calculated measure.
    
    Keyword arguments:
    type_ -- type of central tendency to be calculated
    df -- the dataframe
    col -- the column(s) in the dataframe to do the calculations, this is a list with 2 elements if we want to calculate covariance
    
    Returns:
    disp -- the calculated measure of dispersion
    """
    disp=df[col].apply(type_)
    print(disp)
measure_of_dispersion("std",df,"exch_usd")



def calculate_correlation(type_, df, col1, col2):
    """Calculate the defined correlation coefficient.
    
    This function accepts the type of correlation coefficient to be calculated, the data frame and the two column.
    It returns the calculated coefficient.
    
    Keyword arguments:
    type_ -- type of correlation coefficient to be calculated
    df -- the dataframe
    col1 -- first column
    col2 -- second column
    
    Returns:
    corr -- the calculated correlation coefficient
    """
    from scipy.stats import pearsonr
    newdf=df[[col1,col2]]
    pearsoncorr=newdf.corr(method=type_)
    print(pearsoncorr)
calculate_correlation("pearson",df,"exch_usd","inflation_annual_cpi")
    


def calculate_probability_discrete(data, event):
    """Calculates the probability of an event from a discrete distribution.
    
    This function accepts the distribution of a variable and the event, and returns the probability of the event.
    
    Keyword arguments:
    data -- series that contains the distribution of the discrete variable
    event -- the event for which the probability is to be calculated
    
    Returns:
    prob -- calculated probability fo the event
    """
    prob=len(df[df[data]==event])/len(df[data])
    print(prob)
calculate_probability_discrete("banking_crisis","no_crisis")





p_a=len(df[df.banking_crisis=="crisis"])/len(df.banking_crisis)
p_b=len(df[df.systemic_crisis == 1])/len(df.systemic_crisis)
df1=df[df.systemic_crisis == 1]
p_a_b=len(df1[df1.banking_crisis=="crisis"])/len(df1.banking_crisis)

def event_independence_check(prob_event1, prob_event2, prob_event1_event2):
    """Checks if two events are independent.
    
    This function accepts the probability of 2 events and their joint probability.
    And prints if the events are independent or not.
    
    Keyword arguments:
    prob_event1 -- probability of event1
    prob_event2 -- probability of event2
    prob_event1_event2 -- probability of event1 and event2
    """
    result=prob_event1_event2==prob_event1
    print(result)
event_independence_check(p_a,p_b,p_a_b)
    


prob_=[]
def bayes_theorem(df, col1, event1, col2, event2):
    """Calculates the conditional probability using Bayes Theorem.
    
    This function accepts the dataframe, two columns along with two conditions to calculate the probability, P(B|A).
    You can call the calculate_probability_discrete() to find the basic probabilities and then use them to find the conditional probability.
    
    Keyword arguments:
    df -- the dataframe
    col1 -- the first column where the first event is recorded
    event1 -- event to define the first condition
    col2 -- the second column where the second event is recorded
    event2 -- event to define the second condition
    
    Returns:
    prob -- calculated probability for the event1 given event2 has already occured
    """
filt11 = (df['systemic_crisis'] == 1) #& (df['currency_crises'] == 1) & (df['inflation_crises'] == 1)
filt22 = (df['currency_crises'] == 1)
filt33 = (df['inflation_crises'] == 1)

prob_ = []
temp = df[filt11]['banking_crisis'].value_counts()[0]/len(df[filt11])
prob_.append(temp)
temp = df[filt22]['banking_crisis'].value_counts()[1]/len(df[filt22])
prob_.append(temp)
temp = df[filt33]['banking_crisis'].value_counts()[1]/len(df[filt33])
prob_.append(temp)
print('The value of Prob_ is: {}'.format(prob_))





# Load the dataset


# Using the visual_summary(), visualize the distribution of the data provided.
# You can also do it at country level or based on years by passing appropriate arguments to the fuction.



# You might also want to see the central tendency of certain variables. Call the central_tendency() to do the same.
# This can also be done at country level or based on years by passing appropriate arguments to the fuction.


# Measures of dispersion gives a good insight about the distribution of the variable.
# Call the measure_of_dispersion() with desired parameters and see the summary of different variables.



# There might exists a correlation between different variables. 
# Call the calculate_correlation() to check the correlation of the variables you desire.



# From the given data, let's check the probability of banking_crisis for different countries.
# Call the calculate_probability_discrete() to check the desired probability.
# Also check which country has the maximum probability of facing the crisis.  
# You can do it by storing the probabilities in a dictionary, with country name as the key. Or you are free to use any other technique.



# Next, let us check if banking_crisis is independent of systemic_crisis, currency_crisis & inflation_crisis.
# Calculate the probabilities of these event using calculate_probability_discrete() & joint probabilities as well.
# Then call event_independence_check() with above probabilities to check for independence.



# Calculate the P(A|B)



# Finally, let us calculate the probability of banking_crisis given that other crises (systemic_crisis, currency_crisis & inflation_crisis one by one) have already occured.
# This can be done by calling the bayes_theorem() you have defined with respective parameters.



# Code ends


