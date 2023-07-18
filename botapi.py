#    OpenLightBit-KuoHuBit
#    Copyright (C) 2023  Emerald-AM9
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    tongtong_khapi_url = botfunc.lbit_conf('api-ip')
    tongtong_khapi_port = botfunc.lbit_conf('api-port')
    uvicorn.run("botapi:app", port={tongtong_khapi_port}, host='{tongtong_khapi_url}', reload=True)