CREATE OR REPLACE DATABASE Nobel_Prizes;

CREATE OR REPLACE SCHEMA Nobel_Prizes.Nobel_Cleaned_Data;

CREATE OR REPLACE TABLE Nobel_Prizes.Nobel_Cleaned_Data.Prize_Winners(
    Recipient_Name VARCHAR,
    Birth_Country VARCHAR,
    Affiliated_Institute VARCHAR,
    Year_Prize_Awarded NUMBER,
    Prize_Category VARCHAR,
    Motivation VARCHAR
);