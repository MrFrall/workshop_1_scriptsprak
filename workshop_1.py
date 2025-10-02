# Import the json library so that we can handle json
import json

# Read json from products.json to the variable data
data = json.load(open("network_devices.json","r",encoding = "utf-8"))

# Create a variable that holds our whole text report
report = "\n"

#DEL A
#Läs in JSON-filen och visa företagsnamn och när data senast uppdaterades
report += "Company Name: " + data["company"] + "\n"

report += "Last updated: " + data["last_updated"] + "\n\n"

#Lista alla enheter med status "offline" eller "warning"
report += "--- Devices with Problem ---" +"\n\n"

report += "--- Status: Offline --- " + "\n"
for location in data["locations"]:
   for device in location["devices"]:
    if device["status"] == "offline":
       report += location["site"].ljust(15) + " | " + device["hostname"].ljust(15) + " | " + device["type"].ljust(15) + " | " + device["ip_address"].ljust(15) + "\n"

report += "\n" + "--- Status: Warning --- " + "\n"
for location in data["locations"]:
   for device in location["devices"]:
    if device["status"] == "warning":
       report += location["site"].ljust(15) + " | " + device["hostname"].ljust(15) +" | " + device["type"].ljust(15) + " | " + device["ip_address"].ljust(15) + "\n"


#Räkna totalt antal enheter per typ (switch,router,access_point, etc.)

report += "\n" + "--- Total number of unit types ---" + "\n\n"

switch_count = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device["type"] == "switch":
            switch_count += 1

router_count = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device["type"] == "router":
            router_count += 1

access_point_count = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device["type"] == "access_point":
            access_point_count += 1

firewall_count = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device["type"] == "firewall":
            firewall_count += 1

load_balancer_count = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device["type"] == "load_balancer":
            load_balancer_count += 1

report += "Switch:".ljust(15) + str(switch_count).rjust(15) + " st" +"\n"
report += "Router:".ljust(15) + str(router_count).rjust(15) + " st" +"\n"
report += "Access Point:".ljust(15) + str(access_point_count).rjust(15) + " st" +"\n"
report += "Firewall:".ljust(15) + str(firewall_count).rjust(15) + " st" +"\n"
report += "Load Balancer:".ljust(15) + str(load_balancer_count).rjust(15) + " st" +"\n"



report += "\n\n"
# loop through the location list 
for location in data["locations"]:

    # add the site/'name' of the location to the report
    report += "\n" + location["site"] + "\n"

    # add a list of the host names of the devices 
    # on the location to the report
    for device in location["devices"]:
      report += "  " + device["hostname"] + "\n"

# write the report to text file
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)