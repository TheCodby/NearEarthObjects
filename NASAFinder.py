import requests
import pandas as pd
minDate = input('''Min Date
Exp: 1900-01-01
''')
maxDate = input('''Min Date
Exp: 2100-01-01
''')
MaxDistance = input('''Max Distance
Exp: 0.2
''')
response = requests.get('https://ssd-api.jpl.nasa.gov/cad.api?des=433&date-min='+ minDate + '&date-max='+ maxDate + '&dist-max=' + MaxDistance)
res = response.json()
df3 = pd.DataFrame(res['data'], columns=res['fields'])
print(df3)
