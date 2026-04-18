import os
import platform

analyst_name = input("Enter analyst name: ")
department = input("Enter department: ")

print("\n" + "="*40)
print("System Profile Report")
print("="*40)
print("Analyst:", analyst_name)
print("Department:", department)
print("Hostname:", platform.node())
print("Operating System:", platform.system(), platform.release())
print("Current User:", os.getlogin())
print("="*40)
print("Report generated successfully!")