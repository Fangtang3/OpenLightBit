import uvicorn
from fastapi import FastAPI, Response

import botfunc

app = FastAPI()


@app.get("/bot/data/get/six")
async def six(response: Response):
    response.status_code = 200
    data = await botfunc.select_fetchall("SELECT uid, count FROM six ORDER BY count DESC ")
    return {"status": 200, "data": data}


if __name__ == '__main__':
    tongtong_khapi_url = botfunc.khbit_api_custom_address('khbit-api-ip')
    tongtong_khapi_port = botfunc.khbit_api_custom_address('khbit-api-port')
    uvicorn.run("botapi:app", port={tongtong_khapi_port}, host='{tongtong_khapi_url}', reload=True)