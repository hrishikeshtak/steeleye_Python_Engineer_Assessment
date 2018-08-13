# steeleye_Python_Engineer_Assessment

#### Prerequisite
1. Already created an AWS S3 bucket with full permission to AWS lambda function

#### How To Run
1. Upload a .zip file into lambda function
>> zip file contains dependency to run lambda_function like xlrd package, excel file ISO10383_MIC.xls and lambda_function.py

2. Create a test event with following entries
>> lambda_function assumes that AWS S3 bucket is created with permissions to lambda function
>> bucketname is mandatory to pass in event
>> excel_sheet_name and output_json_filename are optional
{
  "bucketname": "<AWS S3 BucketName>",
  "excel_sheet_name": "MICs List by CC",
  "output_json_filename": "Hrishikesh_Python_Engineer_Assessment_output"
}
3. Save and Test