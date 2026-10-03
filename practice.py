import psutil

resources = {
    "CPU": psutil.cpu_percent(),
    "Memory": psutil.virtual_memory().percent,
    "Disk": psutil.disk_usage('/').percent
}

def check_resource(name, usage):
    if usage >= 80:
        return f"<p style='color:red'>WARNING: {name} is too high! ({usage}%)</p>"
    else:
        return f"<p style='color:green'>OK: {name} is normal ({usage}%)</p>"

html = "<html><body><h1>Server Monitor</h1>"

for key, value in resources.items():
    html += check_resource(key, value)

html += "</body></html>"

with open('/app/output/index.html', 'w') as f:
    f.write(html)

print("Report generated!")
