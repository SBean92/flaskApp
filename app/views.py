from flask import render_template
from app import app 
from systeminfo import systeminfo

@app.route('/')
def index():
    returnDict = {}
    returnDict['Assignment'] = '2'
    returnDict['Course'] = 'COMP30670'
    returnDict['System'] = systeminfo.getSystem()
    returnDict['Processor'] = systeminfo.getProcessor()
    returnDict['Machine'] = systeminfo.getMachine()
    returnDict['Network'] = systeminfo.getNetwork()
    return render_template("index.html", **returnDict)
