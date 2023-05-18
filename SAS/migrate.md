# Qualification questions
For SAS Stats/ML
- How many SAS models running in production? 
- What kind of model do you have?  regressions, decision trees, Neural Nets, time series forecasting, etc
- Is there any MLOps or some model governance?
 - How often do you update them (re-train, evaluate,etc)
 - Are they running in batch (monthly, daily, hourly)? 
- Are they integrated to some app?
- How the data is prepared/transformed to be used in the models? 


# Strategy
insight from https://www.databricks.com/blog/2022/09/07/four-steps-migrate-sas-data-warehouse-lakehouse.html

## Step 1: Analyze
Before starting the migration, you should assess the scope and identify priorities.
- Which datasets do they use? Or, if your cloud data governance dictates column level restrictions, such as for PII data - which specific columns are in use?
- Which types of user-written, custom transformations are in use? How much code is it?Swhich ones are unique?
- What are the dependencies between the jobs?

Use [SAS Content Assessment](https://go.documentation.sas.com/doc/en/sasadmincdc/v_032/contentassessment/titlepage.htm) 
  - have a great high-level overview of what's inside your environment. 
  - **LIMIT**: it doesn't provide number of lines of user written code, columns nor their metadata etc.
## Step 2: Prepare
moving to a Lakehouse, you need two crucial pieces: your data in the cloud and a framework that your data engineers will use to build data pipelines.

Data
 
Framwork: comprises your modern ETL toolkit and helper libraries/functions.
- TBD
