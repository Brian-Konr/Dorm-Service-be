# Dorm_Service_Backend

## Setup

### Postgresql
現階段的連線都是用 Localhost <br>
所以沒有辦法共用一個 postgresql 更新資料<br>
現階段先麻煩大家連線到自己的 local host。
前置作業如下：<br>
1. 要先在自己的 postgresql new database (取名為 dorm_service)
2. 將 Dorm_Service_Backend/database.py 內的 engine 改成自己的密碼

### Create Database
至於 server 我是創建虛擬環境 然後在裡面 pip install requirements。<br>
不太確定你們需不需要重新 install，如果需要的話，要 install 的 list 如下：<br>
* python -m pip install --upgrade pip 用作更新 pip 到最新版本
* pip install uvicorn
* pip install fastapi
* pip install sqlalchemy
* pip install psycopg2-binary

完成後請先 cd 到 Dorm_Service_Backend 並在 terminal 執行以下指令：python create_db.py<br>
執行完成後可以去 Postgresql 確認在 dorm_service 這個 database 內是否已經創建了一個 items table<br>
創建完成後就可以 run server 了！

## Run the server
1. 進入虛擬環境：dorm_service-env/Scripts/activate
2. uvicorn main:app --reload
3. uvicorn 會替 FastAPI 開啟 server，接著上 localhost:8000/docs，如果可以看到 APIs 就成功了！(所謂的起後端？
