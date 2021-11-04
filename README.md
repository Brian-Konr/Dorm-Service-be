# Dorm_Service_Backend

## Setup
進入 Dorm_Service_Backend 後：
1. 創建虛擬環境 
    - (windows)：python3 -m venv dorm_service
    - (macOS) : python3 -m venv dorm_service
2. 進入虛擬環境
    - (windows)：dorm_service/Scripts/activate
    - (macOS) : source dorm_service/Scripts/activate
3. 安裝所需套件：pip install -r requirements.txt

### Run the server
進入 Dorm_Service_Backend 後：
1. 進入虛擬環境
    - (windows)：dorm_service/Scripts/activate
    - (macOS) : source dorm_service/Scripts/activate
2. cd App
3. uvicorn main:app --reload
4. uvicorn 會替 FastAPI 開啟 server，接著上 localhost:8000/docs，如果可以看到 APIs 就成功了！(所謂的起後端？

### About connecting to local postgresql
現階段的連線都是用 Localhost <br>
所以沒有辦法共用一個 postgresql 更新資料<br>
現階段先麻煩大家連線到自己的 local host。
前置作業如下：<br>
1. 要先在自己的 postgresql new database (取名為 dorm_service)
2. 將 Dorm_Service_Backend/App/database.py 內的 engine 改成自己的密碼
