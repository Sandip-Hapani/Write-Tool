import os
import uvicorn

'''
This main file and we have to run this file and this application
runs on uvicorn server on 5000 port and has a five paraller process
that is refer as a worker.
'''

if __name__ == "__main__":
    uvicorn.run("server.api:app", host="0.0.0.0", port=8008, lifespan="on", reload=True)
