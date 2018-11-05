import json
import time
import grpc
import scanemails_pb2
import scanemails_pb2_grpc
from concurrent import futures
import scanEmails

class ScanEmails(scanemails_pb2_grpc.ScanEmailsServicer):
    def GetScanEmailsData(self , req , context):
        link = req.query
        print(link)
        # r= scanEmails.getemails(link)
        for alll in scanEmails.getemails(link):
            print alll
            yield scanemails_pb2.ScanEmailsResponse(response=json.dumps(alll) )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    scanemails_pb2_grpc.add_ScanEmailsServicer_to_server(ScanEmails(),server)
    server.add_insecure_port('[::]:50061')
    server.start()
    print ("started fetching emails")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()

