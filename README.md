### This script uses the OpenCage Geocoding API to convert shopping centre addresses into geographic coordinates (latitude and longitude), then appends the results to a CSV file.

### What It Does
	•	Reads addresses from Shopping centres (population, competitors).csv
	•	Geocodes each address using OpenCage API
	•	Adds latitude and longitude columns
	•	Outputs results to output_file.csv

 ### Setup
	1.	Get a free API key from opencagedata.com
	2.	Replace the API_KEY in the script with your key


### Input:
  123 High Street, UK

### Output:
  123 High Street, UK, 51.5074, -0.1278

### Results saved in output_file.csv.


