from flask import Flask, request, jsonify, current_app
#from apscheduler.schedulers.background import BackgroundScheduler
from utils.sap_itsm_utils import *
from controls.bus001 import *
from controls.itsec001 import *
from controls.mc_mm_p003 import *
from controls.mc_mm_p006 import *
from controls.mc_sd_s002 import *
from bson import json_util
import sys

os.environ["Deployment"] = "DEV"

print("Deployment is set as --> ",os.environ["Deployment"])

def BUS001(server):
    # Implement your logic for the BUS001 function here
    control1 = BussCtrl_001(server)
    # This is just a placeholder function for demonstration purposes
    print("Running BUS001 function")
    
    control1.bus001Execute()

def ITSEC_001():
    # Implement your logic for the BUS001 function here
    control2 = ITSEC001()
    # This is just a placeholder function for demonstration purposes
    print("Running ITSEC001 function")
    
    control2.itsecExecute()

def MCMMP033():
    # Implement your logic for the BUS001 function here
    control3 = MC_MM_P003()
    # This is just a placeholder function for demonstration purposes
    print("Running MCMMP033 function")
    
    control3.p003Execute()

def MCMMP006():
    # Implement your logic for the BUS001 function here
    control4 = MC_MM_P006()
    # This is just a placeholder function for demonstration purposes
    print("Running MCMMP006 function")
    
    control4.p006Execute()

def MCSDS002():
    # Implement your logic for the BUS001 function here
    control5 = MC_SD_S002()
    # This is just a placeholder function for demonstration purposes
    print("Running MCSDS002 function")
    
    control5.s002Execute()

def job_function(control,server):

    print(control)
    print(os.environ["Deployment"])
    print("server chosen:",server)
    if control == 'BUS001':
        BUS001(server)
        return jsonify(message="BUS001 function scheduled successfully")
    elif control == 'ITSEC001':
        ITSEC_001()
        return jsonify(message="ITSEC001 function scheduled successfully")
    elif control == 'MCMMP033':
        MCMMP033() 
        return jsonify(message="MCMMP033 function scheduled successfully")
    elif control == 'MCMMP006':
        MCMMP006()   
        return jsonify(message="MCMMP006 function scheduled successfully")
    elif control == 'MCSDS002':
        MCSDS002()   
        return jsonify(message="MCSDS002 function scheduled successfully")
    else:
        print(f"Unknown control: {control}")

if __name__=="__main__":
    job_function(sys.argv[1],sys.argv[2])
    

