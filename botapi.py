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
    mica_app_khapi_url = botfunc.khbit_api_custom_address('khbit-api-ip')
    mica_app_khapi_prt = botfunc.khbit_api_custom_address('khbit-api-port')
    uvicorn.run("botapi:app", port={mica_app_khapi_prt}, host='{mica_app_khapi_url}', reload=True)
