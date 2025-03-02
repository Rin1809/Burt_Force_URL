import requests
import threading
from bs4 import BeautifulSoup
import time
import re

results = {} 
count = 0 
found = False  
lock = threading.Lock() 

z = 400
y = 25163
w = 500

def check_chapter(x):
    global count, found
    if found:
        return  
    
    url = f"https://yurineko.net/read/{x}/{y}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

       
            image_url_pattern = re.compile(
                r"https://storage\.yurineko\.net/manga/\d+/chapters/\d+/\d+\.(jpg|png|jpeg)"
            )
            if image_url_pattern.search(str(soup)):
                with lock:
                    if not found:  
                        print(
                            f"Tìm thấy chương truyện: {url}"
                        )  
                        results[x] = f"Chương truyện đã tải hoàn chỉnh: {url}"
                        found = True  
                        return  

        else:
            print(f"Mã trạng thái {response.status_code} cho URL: {url}")

        with lock:
            count += 1
            if count % w == 0:  
                print(f"Đã duyệt {count} trang")

        time.sleep(3)  

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kiểm tra URL {url}: {e}")
        with lock:
            count += 1

def main():
    threads = []
    for x in range(3000, 4100):
        while threading.active_count() >= z: 
            time.sleep(1)
        thread = threading.Thread(target=check_chapter, args=(x,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if found:
       
        first_x = min(results.keys())
        print(f"/{first_x}/{y}")

if __name__ == "__main__":
    main()