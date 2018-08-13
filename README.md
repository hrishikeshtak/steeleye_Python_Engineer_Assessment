# steeleye_Python_Engineer_Assessment

#### Prerequisite
1. Already created an AWS S3 bucket
2. Create a new lambda function with Runtime: Python 3.6 and full permission to AWS S3 Bucket

#### How To Run
1. change Code entry type in Lambda Function to Upload a .zip file      

2. Upload a .zip file into lambda function
>> zip file contains dependency to run lambda_function like xlrd package, excel file ISO10383_MIC.xls and lambda_function.py

3. Create a test event with following entries       
>> 1. bucketname is mandatory to pass in event         
>> 2. excel_sheet_name and output_json_filename are optional            

{         
  "bucketname": "\<AWS S3 BucketName>",            
  "excel_sheet_name": "MICs List by CC",           
  "output_json_filename": "Hrishikesh_Python_Engineer_Assessment_output.json"         
}     

4. Save and Test

5. Output Json File "Hrishikesh_Python_Engineer_Assessment_output.json" is uploaded to AWS S3 bucket
