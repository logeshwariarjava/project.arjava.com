from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/{endpoint:path}", methods=["GET","POST","PUT","DELETE"])
async def dynamic_api(request: Request, endpoint: str):

    host = request.headers.get("host")

    return {
        "host": host,
        "endpoint": endpoint
    }