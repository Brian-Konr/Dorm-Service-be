# Dorm_Service_Backend

## Setup
我是創建虛擬環境 然後在裡面作 pip install。
不太確定你們需不需要重新 install，如果需要的話，要 install 的 list 如下：
python -m pip install --upgrade pip 用作更新 pip 到最新版本
pip install uvicorn
pip install fastapi
pip install sqlalchemy
pip install psycopg2-binary

## Run the server
1. 進入虛擬環境
2. uvicorn main:app --reload
3. uvicorn 會替 FastAPI 開啟 server，接著上 localhost:8000/docs，如果可以看到 APIs 就成功了！(所謂的起後端？

## Postgresql
現階段的連線是用我自己的帳號
不確定如果你們使用我的帳號密碼進去後更改 table 我這邊會不會也改到？
如果不行的話應該可以再解決
我的帳號密碼：
帳：(沒設定，就是初始的)
密：adgj123456
