# Import the json library so that we can handle json
import json

# Read json from products.json to the variable data
data = json.load(open("network_devices.json","r",encoding = "utf-8"))

# Create a variable that holds our whole text report
report = "-----------------------------------------------------------------------------------------" + "\n"

#DEL A
# 1: Läs in JSON-filen och visa företagsnamn och när data senast uppdaterades
report += "Company Name: " + data["company"] + "\n"

report += "Last updated: " + data["last_updated"] + "\n\n"

# 2: Lista alla enheter med status "offline" eller "warning"
report += "--- Devices with Problem ---" +"\n"
report += "-----------------------------------------------------------------------------------------" + "\n"


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


# 3: Räkna totalt antal enheter per typ (switch,router,access_point, etc.)

report += "\n" + "--- Total number of unit types ---" + "\n"
report += "-----------------------------------------------------------------------------------------" + "\n"

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

# 4: Visa alla enheter som har mindre än 30 dagars uptime

report += "\n" + "--- Units with low uptime (<30 Days) ---" + "\n"
report += "-----------------------------------------------------------------------------------------" + "\n"

for location in data["locations"]:
    for device in location["devices"]: 
        if device["uptime_days"] <= 30:
            report += location["site"].ljust(15) + " | " + device["hostname"].ljust(15) + " | " + str(device["uptime_days"]).ljust(3) + "Uptime days" + " | " + "Current status: " + device["status"] + "\n"

# 5: Beräkna total portanvändning för alla switchar (använt/totalt och procent)

# Problem i report uppkommer om företaget skulle uppgradera switcharna på lager, malmö och säkerhetskopia. Då blir formateringen "sne"

report += "\n" + "--- Port usage: Switches ---" + "\n"
report += "-----------------------------------------------------------------------------------------"
report += "\n" + "Site".ljust(15) + "Switchar".ljust(15) + "Used/Total".ljust(15) + "% Usage".ljust(15) + "\n"

huvudkontor_switches = 0

for location in data["locations"]:
    if location["site"] == "Huvudkontor":
        for device in location["devices"]:
            if device["type"] == "switch":
                huvudkontor_switches += 1

huvudkontor_total_ports = 0
huvudkontor_used_ports = 0

for location in data["locations"]:
    if location["site"] == "Huvudkontor":
        for device in location["devices"]:
            if device["type"] == "switch":
                huvudkontor_total_ports += device["ports"]["total"]
                huvudkontor_used_ports += device["ports"]["used"]

datacenter_switches = 0

for location in data["locations"]:
    if location["site"] == "Datacenter":
        for device in location["devices"]:
            if device["type"] == "switch":
                datacenter_switches += 1

datacenter_total_ports = 0
datacenter_used_ports = 0

for location in data["locations"]:
    if location["site"] == "Datacenter":
        for device in location["devices"]:
            if device["type"] == "switch":
                datacenter_total_ports += device["ports"]["total"]
                datacenter_used_ports += device["ports"]["used"]

malmo_switches = 0

for location in data["locations"]:
    if location["site"] == "Kontor Malmö":
        for device in location["devices"]:
            if device["type"] == "switch":
                malmo_switches += 1

malmo_total_ports = 0
malmo_used_ports = 0

for location in data["locations"]:
    if location["site"] == "Kontor Malmö":
        for device in location["devices"]:
            if device["type"] == "switch":
                malmo_total_ports += device["ports"]["total"]
                malmo_used_ports += device["ports"]["used"]

lager_switches = 0

for location in data["locations"]:
    if location["site"] == "Lager":
        for device in location["devices"]:
            if device["type"] == "switch":
                lager_switches += 1 

lager_total_ports = 0
lager_used_ports = 0

for location in data["locations"]:
    if location["site"] == "Lager":
        for device in location["devices"]:
            if device["type"] == "switch":
                lager_total_ports += device["ports"]["total"]
                lager_used_ports += device["ports"]["used"]

sakerhetskopia_switches = 0

for location in data["locations"]:
    if location["site"] == "Säkerhetskopia":
        for device in location["devices"]:
            if device["type"] == "switch":
                sakerhetskopia_switches += 1

sakerhetskopia_total_ports = 0
sakerhetskopia_used_ports = 0

for location in data["locations"]:
    if location["site"] == "Säkerhetskopia":
        for device in location["devices"]:
            if device["type"] == "switch":
                sakerhetskopia_total_ports += device["ports"]["total"]
                sakerhetskopia_used_ports += device["ports"]["used"]

#Procentuträkningar

procent_huvudkontor_swport = (huvudkontor_used_ports / huvudkontor_total_ports) * 100
procent_datacenter_swport = (datacenter_used_ports) / (datacenter_total_ports) * 100
procent_malmo_swport = (malmo_used_ports / malmo_total_ports) * 100
procent_lager_swport = (lager_used_ports / lager_total_ports) * 100
procent_sakerhetskopia_swport = (sakerhetskopia_used_ports / sakerhetskopia_total_ports) * 100

report += "Huvudkontor".ljust(15) + str(huvudkontor_switches) + "st".ljust(14) + str(huvudkontor_used_ports) + " / " + str(huvudkontor_total_ports) + str(round(procent_huvudkontor_swport, 1)).rjust(10) + "%" 
if procent_huvudkontor_swport > 80:
     report += " - Warning few ports remaining" + "\n"
else:
    report += "\n"
report += "Datacenter".ljust(15) + str(datacenter_switches) + "st".ljust(14) + str(datacenter_used_ports) + " / " + str(datacenter_total_ports) + str(round(procent_datacenter_swport, 1)).rjust(10) + "%" 
if procent_datacenter_swport > 80:
    report += " - Warning few ports remaining" + "\n"
else:
    report += "\n"
report += "Kontor Malmö".ljust(15) + str(malmo_switches) + "st".ljust(14) + str(malmo_used_ports) + " / " + str(malmo_total_ports) + str(round(procent_malmo_swport, 1)).rjust(12) + "%" 
if procent_malmo_swport > 80:
    report += " - Warning few ports remaining" + "\n"
else:
    report += "\n"
report += "Lager".ljust(15) + str(lager_switches) + "st".ljust(14) + str(lager_used_ports) + " / " + str(lager_total_ports) + str(round(procent_lager_swport, 1)).rjust(12)+ "%" 
if procent_lager_swport > 80:
    report += " - Warning few ports remaining" + "\n"
else:
    report += "\n"
report += "Säkerhetskopia".ljust(15) + str(lager_switches) + "st".ljust(14) + str(sakerhetskopia_used_ports) + " / " + str(sakerhetskopia_total_ports) + str(round(procent_sakerhetskopia_swport, 1)).rjust(12) + "%" 
if procent_sakerhetskopia_swport > 80:
    report += " - Warning few ports remaining" + "\n"
else:
    report += "\n"

report += "\n"

# 6: Lista alla unika VLAN som används i nätverket

report += "--- Unique Vlans in network ---" + "\n"
report += "-----------------------------------------------------------------------------------------" + "\n"

unique_vlans = set()

for location in data["locations"]:
    for device in location["devices"]:
        if "vlans" in device:
            for vlan in device["vlans"]:
                unique_vlans.add(vlan)

sorted_vlans = sorted(unique_vlans)
report += "Total number of Vlans: " + str(len(sorted_vlans)) + "\n"
report += "Individual Vlans: " + str(sorted_vlans) + "\n"


# 7: Skapa en översikt per lokation (antal enheter, antal online/offline)

report += "\n" + "--- Statistics per location ---" + "\n"
report += "-----------------------------------------------------------------------------------------" + "\n"

huvudkontor_units = 0

for location in data["locations"]:
    if location["site"] == "Huvudkontor":
        for device in location["devices"]:
            huvudkontor_units += 1

huvudkontor_status_online = 0
huvudkontor_status_offline = 0
huvudkontor_status_warning = 0

for location in data["locations"]:
    if location["site"] == "Huvudkontor":
        for device in location["devices"]:
            if device["status"] == "online":
                huvudkontor_status_online += 1
            elif device["status"] == "offline":
                huvudkontor_status_offline += 1
            elif device["status"] == "warning":
                huvudkontor_status_warning += 1


datacenter_units = 0

for location in data["locations"]:
    if location["site"] == "Datacenter":
        for device in location["devices"]:
            datacenter_units += 1

datacenter_status_online = 0
datacenter_status_offline = 0
datacenter_status_warning = 0

for location in data["locations"]:
    if location["site"] == "Datacenter":
        for device in location["devices"]:
            if device["status"] == "online":
                datacenter_status_online += 1
            elif device["status"] == "offline":
                datacenter_status_offline += 1
            elif device["status"] == "warning":
                datacenter_status_warning += 1

malmo_units = 0

for location in data["locations"]:
    if location["site"] == "Kontor Malmö":
        for device in location["devices"]:
            malmo_units += 1

malmo_status_online = 0
malmo_status_offline = 0
malmo_status_warning = 0

for location in data["locations"]:
    if location["site"] == "Kontor Malmö":
        for device in location["devices"]:
            if device["status"] == "online":
                malmo_status_online += 1
            elif device["status"] == "offline":
                malmo_status_offline += 1
            elif device["status"] == "warning":
                malmo_status_warning += 1

lager_units = 0

for location in data["locations"]:
    if location["site"] == "Lager":
        for device in location["devices"]:
            lager_units += 1

lager_status_online = 0
lager_status_offline = 0
lager_status_warning = 0

for location in data["locations"]:
    if location["site"] == "Lager":
        for device in location["devices"]:
            if device["status"] == "online":
                lager_status_online += 1
            elif device["status"] == "offline":
                lager_status_offline += 1
            elif device["status"] == "warning":
                lager_status_warning += 1

sakerhetskopia_units = 0

for location in data["locations"]:
    if location["site"] == "Säkerhetskopia":
        for device in location["devices"]:
            sakerhetskopia_units += 1

sakerhetskopia_status_online = 0
sakerhetskopia_status_offline = 0
sakerhetskopia_status_warning = 0

for location in data["locations"]:
    if location["site"] == "Säkerhetskopia":
        for device in location["devices"]:
            if device["status"] == "online":
                sakerhetskopia_status_online += 1
            elif device["status"] == "offline":
                sakerhetskopia_status_offline += 1
            elif device["status"] == "warning":
                sakerhetskopia_status_warning += 1

report += "Huvudkontor (Stockholm):" + "\n" + "Units: " + str(huvudkontor_units) + " | Online: " + str(huvudkontor_status_online) + " | Offline: " + str(huvudkontor_status_offline)+ " | Warning: " + str(huvudkontor_status_warning) + "\n\n"
report += "Datacenter: (Stockholm)" + "\n" + "Units: " + str(datacenter_units) + " | Online: " + str(datacenter_status_online) + " | Offline: " + str(datacenter_status_offline) + " | Warning: " + str(datacenter_status_warning) + "\n\n"
report += "Kontor Malmö: (Malmö)" + "\n" + "Units: " + str(malmo_units) + " | Online: " + str(malmo_status_online) + " | Offline: " + str(malmo_status_offline) + " | Warning: " + str(malmo_status_warning) + "\n\n"
report += "Lager: (Göteborg)" + "\n" + "Units: " + str(lager_units) + " | Online: " + str(lager_status_online) + " | Offline: " + str(lager_status_offline) + " | Warning: " + str(lager_status_warning) + "\n\n"
report += "Säkerhetskopia: (Umeå)" + "\n" + "Units: " + str(sakerhetskopia_units) + " | Online: " + str(sakerhetskopia_status_online) + " | Offline: " + str(sakerhetskopia_status_offline) + " | Warning: " + str(sakerhetskopia_status_warning) + "\n\n"


# write the report to text file
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)