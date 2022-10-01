import time

import requests

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Make an API call.
url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict)

lons = [response_dict["iss_position"]["longitude"]]
lats = [response_dict["iss_position"]["latitude"]]
instant = response_dict["timestamp"]

instance = time.ctime(instant)

print(instance)

# Prints the list.
print(lons, lats)

# Map the position.
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": 10,
        },
    }
]
my_layout = Layout(title="ISS Position")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="iss.html")
