OUTPUT_BASE = 'output'
OUTPUT_IMG = OUTPUT_BASE + '/img'
OUTPUT_CSV = OUTPUT_BASE + '/csv'
REGISTERS_FILE = '/registers.csv'
IMAGE_LIST = ['auditTrailImage', 'photoIDFaceCrop', 'idScanBackImage', 'photoIDBackCrop']
HEADER = ['identificador', 'nombre', 'apellido', 'nrodoc', 'fecha', 'resultado']
VARIABLES = {"externalDatabaseRefID": 1,
             "data": 1,
             "callData.epochSecond": 1,
             "faceScanSecurityChecks.faceScanLivenessCheckSucceeded": 1
             }
