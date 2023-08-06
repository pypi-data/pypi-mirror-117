from datetime import time
from flask import Flask
from teska_monitor import telemetry

app = Flask(__name__)


TEMPLATE ="""
<h1>Monitoring</h1>
<p><strong>Boot Time: </strong>{time} </p>
<p><strong>CPU Temperature: </strong>{temp}°C</p>
<p><strong>CPU Usage: </strong>{cpu}%</p>
<p><strong>Disk Usage: </strong>{disk} %</p>
<p><strong>Total Memory: </strong>{total} GB</p>
<p><strong>Virtual Memory: </strong>{mem}%</p>

"""

@app.route("/")
def index():
   
    # telper = telemetry.get_cpu_percent()
    # telper = str(telper)

    # telmem = telemetry.get_virtual_memory()
    # telmem = str(telmem)    
   
    data = telemetry.get_all()

    total = data["total_memory"]
    total_gb = round(total / 1024 / 1024 / 1024, 2)
    
    return TEMPLATE.format(
        cpu=data["cpu_usage"],
        temp=data["cpu_temperature"], 
        mem=data["virtual_memory"], 
        total=total_gb, 
        disk=data["disk_usage"],
        time=data["boot_time"]
    )


@app.route("/json")
def show_json():
    # telper = telemetry.get_cpu_percent()  
    # telmem = telemetry.get_virtual_memory()  
    # output = {"cpu_usage": telper, "Virtueller Ram": telmem}

    output = telemetry.get_all()

    return output

if __name__=="__main__":
    app.run(debug = True)    