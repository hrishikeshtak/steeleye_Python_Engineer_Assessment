import boto3
import json
import sys
import xlrd

from collections import OrderedDict


class ExcelAssignment():
    """ Read excel sheet and store as a list of dict
    """
    def __init__(self,
                 excel_filename=None,
                 excel_sheet_name=None):
        # initialize filename and sheetname
        self.excel_filename = excel_filename
        self.excel_sheet_name = excel_sheet_name
        self.result_data = list()

    def read_excel_data(self):
        """ Read excel data
        """
        try:
            # Open a workbook
            workbook = xlrd.open_workbook(self.excel_filename,
                                          on_demand=True)
            # Loads only current sheets to memory
            return workbook.sheet_by_name(self.excel_sheet_name)
        except Exception as err:
            print(f"Unable to read excel file: {self.excel_filename}, "
                  f"Reason: {err}")
            sys.exit(1)

    def convert_excel_to_list_of_dict(self):
        """ Convert Excel data to List of Dict
        """
        excel_data = self.read_excel_data()
        # Excel data 1st row is a key to dictionary
        keys = [key.value for key in excel_data.row(0)]
        for row_index in range(1, excel_data.nrows):
            """ Iterate over excel data row by row and
            prepare OrderedDict to maintain order of data
            while writing to json
            """
            result_dict = OrderedDict()
            try:
                # get column from excel sheet
                columns = ([column_value.value for column_value in
                            excel_data.row(row_index)])
                # prepare dict with columns data
                result_dict.update(zip(keys, columns))
                # append dict to list
                self.result_data.append(result_dict)
            except Exception as err:
                print(f"Unable to read data from excel file: "
                      f"{self.excel_filename}, Reason: {err}")
                sys.exit(1)
        # return list of dict to upload json data
        return self.result_data


def lambda_handler(event, context):
    # validate event
    if not event.get("bucketname"):
        return ("Please provide bucketname in Event")
    # get boto3 resource for s3
    s3 = boto3.resource("s3")

    # take object of class ExcelAssignment
    excel = ExcelAssignment(excel_filename="ISO10383_MIC.xls",
                            excel_sheet_name=event.get(
                                "excel_sheet_name", "MICs List by CC"))
    result_data = excel.convert_excel_to_list_of_dict()

    bucket_name = event.get('bucketname')
    output_json_filename = event.get(
                'output_json_filename',
                'Hrishikesh_Python_Engineer_Assessment_output.json')
    # upload json result_data to s3 bucket
    s3.Bucket(bucket_name).put_object(
        Key=output_json_filename,
        Body=json.dumps(result_data, indent=4))
    msg = (f"Result Data uploaded to S3 bucket: {bucket_name}"
           f", Output Json filename: {output_json_filename}")
    return msg
