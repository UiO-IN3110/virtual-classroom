import virtual_classroom.utils as utils

# Name of spreadsheet on Google sheets (You should change this to correct value)
spreadsheet_name = "Sign up form for INF3331/INF43331 (2018) (Responses)"

# Download parse, return contents and save it in default place
try:
    csv_str = utils.download_google_spreadsheet(spreadsheet_name)  # Should prompt for login info if default not set
    utils.create_students_file_from_csv(csv_str=csv_str, output_filename="Attendance/students_base.txt")
except Exception as e:
    print("An error occured - exiting")
    print(e)
    import sys
    sys.exit()
   


