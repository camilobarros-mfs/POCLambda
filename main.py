# This is a sample Python script.
import csv
import os
from datetime import datetime
import base64
import constants

from pymongo import MongoClient

from register import Register



client = MongoClient()


def delete_files():
    for f in os.listdir(constants.OUTPUT_CSV):
        os.remove(os.path.join(constants.OUTPUT_CSV, f))
    for f in os.listdir(constants.OUTPUT_IMG):
        os.remove(os.path.join(constants.OUTPUT_IMG, f))


def create_output():
    if not os.path.exists(constants.OUTPUT_BASE):
        os.makedirs(constants.OUTPUT_CSV)
        os.makedirs(constants.OUTPUT_IMG)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    now = datetime.now()


    inicio = now.strftime("%H:%M:%S")

    create_output()
    file = open(constants.OUTPUT_CSV+constants.REGISTERS_FILE, 'w')
    writer = csv.writer(file)
    header = constants.HEADER
    writer.writerow(header)

    client = MongoClient(os.environ['URI'])
    db = client[os.environ['DATABASE']]
    collection = db[os.environ['COLLECTION']]

    data = collection.find(filter=None, limit=0,
                           projection=constants.VARIABLES)
    for reg in data:
        register = Register('', '', '', '', '', '')
        register.id = reg.get("externalDatabaseRefID")

        for key in reg.get("data"):

            if key == "autoExtractedOCRData":
                if "firstName" in reg.get("data")[key]:
                    register.name = reg.get("data")[key]["firstName"]
                elif "lastName" in reg.get("data")[key]:
                    register.last_name = reg.get("data")[key]["lastName"]
                elif "idNumber" in reg.get("data")[key]:
                    register.document = reg.get("data")[key]["idNumber"]
            elif key in constants.IMAGE_LIST:
                image_data = reg.get("data")[key]
                with open(constants.OUTPUT_IMG+'/'+register.id+'-'+key+'.png', 'wb') as fh:
                    fh.write(base64.b64decode(image_data))

        epoch_time = reg.get("callData")["epochSecond"]
        register.date = datetime.fromtimestamp(epoch_time)
        if "faceScanSecurityChecks" in reg:
            register.result = reg.get("faceScanSecurityChecks")["faceScanLivenessCheckSucceeded"]
        printLine = [register.id, register.name, register.last_name, register.document, register.date, register.result]
        writer.writerow(printLine)

    end = datetime.now()

    print("Inicio =", inicio)
    fin = end.strftime("%H:%M:%S")

    print("Fin =", fin)
    file.close()
    client.close()

    delete_files()

