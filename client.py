import json
import time
import grpc
import scanemails_pb2
import scanemails_pb2_grpc

def run():
    channel = grpc.insecure_channel(target = "localhost:50061")
    stub=scanemails_pb2_grpc.ScanEmailsStub(channel)
    res = stub.GetScanEmailsData(scanemails_pb2.ScanEmailsQuery(query="https://www.nti.org/"))
    for r in res:
        print(r.response)

    
if __name__ == "__main__":
    run()