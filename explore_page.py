import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data_gender(df):
    df = df.dropna()
    df = df.loc[df.gender !='Other']
    return df 

def gender_stacked_chart(df):
    # Calculate the total counts for each gender
    total_counts = df['gender'].value_counts()

    # Calculate the counts of diabetes for each gender
    diabetes_counts = df.groupby('gender')['diabetes'].value_counts().unstack().fillna(0)

    # Calculate proportions
    diabetes_proportions = diabetes_counts.div(total_counts, axis=0)

    # Create a bar chart for diabetes status by gender
    diabetes_proportions.plot(kind='bar', color=['lightblue', 'salmon'])
    plt.title('Proportion of Diabetes Status by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Proportion')
    plt.xticks(rotation=0)
    plt.legend(['No Diabetes', 'Diabetes'])
    plt.show()

def pie_chart_diabetes(df_copy):
    smoking_counts = df_copy['smoking_history'].value_counts()
    diabetes_counts = df_copy['diabetes'].value_counts()

    # Prepare data for pie chart
    smoking_labels = smoking_counts.index
    smoking_sizes = smoking_counts.values

    diabetes_labels = ['No Diabetes', 'Diabetes']
    diabetes_sizes = diabetes_counts.values
    plt.pie(smoking_sizes, labels=smoking_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Proportion of Diabetes Positive')

    # Create a pie chart for Diabetes Status
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    plt.pie(diabetes_sizes, labels=diabetes_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Proportion of Diabetes Status')

    plt.tight_layout()
    plt.show()
def clean_smoking_history(df):
    return df.loc[df.smoking_history !='No Info']


def show_explore_page():
    df = pd.read_csv('diabetes_prediction_dataset.csv')
    df_cleaned = clean_data_gender(df)
    df_cleaned = clean_smoking_history(df_cleaned)
    st.title("Grouped Histogram of Smoking Status by Disease Classification")

    # Create a figure for the histogram
    plt.figure(figsize=(10, 6))

    # Plot histograms for each disease classification
    for label, group_data in df_cleaned.groupby('diabetes'):
        plt.hist(group_data['smoking_history'], bins=3, alpha=0.5, label=f'{label}', edgecolor='black')

    # Add labels and title
    plt.xlabel('Smoking Status')
    plt.ylabel('Frequency')
    plt.title('Grouped Histogram of Smoking Status by Disease Classification')
    plt.xticks(rotation=45)
    plt.legend(title='Disease Classification')

    # Display the histogram in Streamlit
    st.pyplot(plt) 
    
    st.title("Diabetes Status by Gender")

    # Calculate the total counts for each gender
    total_counts = df_cleaned['gender'].value_counts()

    # Calculate the counts of diabetes for each gender
    diabetes_counts = df_cleaned.groupby('gender')['diabetes'].value_counts().unstack().fillna(0)

    # Calculate proportions
    diabetes_proportions = diabetes_counts.div(total_counts, axis=0)

    # Create a bar chart for diabetes status by gender
    fig, ax = plt.subplots()
    diabetes_proportions.plot(kind='bar', color=['lightblue', 'salmon'], ax=ax)
    ax.set_title('Proportion of Diabetes Status by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Proportion')
    ax.set_xticklabels(diabetes_proportions.index, rotation=0)
    ax.legend(['No Diabetes', 'Diabetes'])

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Heart Disease Counts by Gender and Diabetes Status")

# Calculate the counts
    counts = df_cleaned.groupby(['heart_disease', 'diabetes']).size().unstack(fill_value=0)
    counts.columns = ['No Diabetes', 'Diabetes']

    # Create a stacked bar chart
    fig, ax = plt.subplots()
    counts.plot(kind='bar', stacked=True, color=['lightblue', 'salmon'], ax=ax)
    ax.set_title('Count of Males and Females by Heart Disease')
    ax.set_xlabel('Heart Disease')
    ax.set_ylabel('Count')
    ax.set_xticklabels(counts.index, rotation=0)
    ax.legend(title='Diabetes Status')

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Blood Glucose Level Histogram")

    # Set the style of seaborn
    sns.set(style='whitegrid')

    # Create a histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df_cleaned['blood_glucose_level'], bins=30, kde=True, color='lightblue', stat='density', linewidth=0)

    # Add a title and labels
    plt.title('Histogram with Distribution Curve for Blood Glucose Level', fontsize=16)
    plt.xlabel('Blood Glucose Level', fontsize=14)
    plt.ylabel('Density', fontsize=14)

    # Display the histogram in Streamlit
    st.pyplot(plt)