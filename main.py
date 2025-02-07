from sqlalchemy import text
import uvicorn
from fastapi import APIRouter, Depends, FastAPI
from database import get_db
from sqlalchemy.orm import Session
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from apis.blockchain_test import router1
from apis.check_balance import router2


app = FastAPI()
app.include_router(router1)
app.include_router(router2)

# create table using SQL function
@app.get("/create-table")
async def create_table(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(
            text(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL
                    );
                '''
            )
            
        )
        await db.commit()  # Commit the transaction
        return {"message": "Table created successfully"}

    except Exception as e:
        print(e)
        return {"error": str(e)}


# loop = asyncio.get_event_loop()
# if loop.is_running():
#     # If the loop is already running, use it to run the coroutine
#     loop.create_task(create_table())
# else:
#     # If no loop is running, use asyncio.run()
#     asyncio.run(create_table())

@app.get('/')
async def root():
    return {'message': 'Hello World'}




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host= '127.0.0.1', port=5000)
    
    
# server {
#         server_name 51.20.40.100 franklinpublisher.com;
#         server_name 51.20.40.100
#         location / {
#                 proxy_pass http://127.0.0.1:8000;
#         proxy_http_version 1.1;
#         proxy_set_header Upgrade $http_upgrade;
#         proxy_set_header Connection 'upgrade';
#         proxy_set_header Host $host;
#         proxy_cache_bypass $http_upgrade;
#         }


#     # SSL settings
#         listen 443 ssl;
#     ssl_certificate /etc/letsencrypt/live/franklinpublisher.com/fullchain.pem; # managed by Certbot
#     ssl_certificate_key /etc/letsencrypt/live/franklinpublisher.com/privkey.pem;                
#  # managed by Certbot
# }
# server {
#     if ($host = franklinpublisher.com) {
#         return 301 https://$host$request_uri;
#     } # managed by Certbot


#         server_name 51.20.40.100 franklinpublisher.com;


#         listen 80;
#     return 404; # managed by Certbot


# }




