import os, csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


boss_csv = os.path.join ("..","**pyboss**","employee_data.csv")



with open(boss_csv, newline='') as csvfile:
           
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    csv_header = next(csvfile)
 
    new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    print(new_header)      

    empID = []
    Name = []
    SSN = []
    firstName = []
    lastName = []
    dob = []
    formattedDOB=[]
    formattedSSN = []
    state = []
    abbrState = []

           
    for row in csvreader:
            empID = row[0]
            Name = row[1]
            dob = row[2]
            SSN = row[3]
            state = row[4]
          
            firstName=row[1].split()[0]
            lastName=row[1].split()[1]

           
            dobYear = row[2].split("-")[0]
            dobMonth = row[2].split("-")[1]
            dobDay = row[2].split("-")[2]
            formattedDOB = dobMonth + "/" + dobDay + "/" + dobYear
            last4_ssn = row[3].split("-")[2]
            formattedSSN = "***-**-" + str(last4_ssn)
            state=row[4]
            abbrState = us_state_abbrev.get(state)            
                
            print(empID,firstName,lastName,formattedDOB,formattedSSN,abbrState)
           