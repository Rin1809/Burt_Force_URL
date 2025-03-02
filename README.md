# ⚡️ Burt Force URL Checker

<details>
<summary>🇻🇳 Tiếng Việt</summary>

## Giới thiệu

Dự án này là một công cụ Python đơn giản để kiểm tra hàng loạt URL (brute-force) nhằm tìm các chương truyện tranh trên một trang web cụ thể (yurineko.net trong code gốc). Nó sử dụng đa luồng (multithreading) để tăng tốc quá trình kiểm tra.

## 🚀 Cách Cài Đặt và Chạy

1.  **Clone Repository:**

    ```bash
    git clone https://github.com/Rin1809/Burt_Force_URL.git
    cd <tên_thư_mục_dự_án>
    ```

2.  **Tạo và Kích Hoạt Môi Trường Ảo:**

    Môi trường ảo giúp cô lập các thư viện Python cần thiết cho dự án, tránh xung đột với các dự án khác.  `run.bat` đã được cung cấp để tự động hóa quá trình này.

    *   Chạy `run.bat`. File này sẽ tự động kiểm tra, tạo (nếu cần), và kích hoạt môi trường ảo, sau đó chạy script `Tool.py`.
    *   Nếu bạn muốn thực hiện thủ công (không khuyến khích, trừ khi bạn biết rõ mình đang làm gì):

        ```bash
        # Tạo môi trường ảo (chỉ cần làm một lần)
        python -m venv moitruongao
        # Kích hoạt môi trường ảo
        # Trên Windows:
        moitruongao\Scripts\activate
        # Trên macOS và Linux:
        source moitruongao/bin/activate
        ```

3.  **Cài Đặt Thư Viện:**

    Nếu bạn đã chạy `run.bat`, bước này đã được thực hiện tự động. Nếu bạn thực hiện thủ công, hãy chạy:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Chạy Ứng Dụng:**

    ```bash
    python Tool.py  # Nếu bạn đã kích hoạt môi trường ảo thủ công
    ```

    Hoặc, đơn giản hơn, chỉ cần chạy `run.bat`.

## ⚙️ Cách Chỉnh Sửa và Tùy Chỉnh

### Thay Đổi Trang Web Mục Tiêu

Để kiểm tra một trang web khác, bạn cần thay đổi các phần sau trong `Tool.py`:

1.  **`url` trong hàm `check_chapter`:**

    Thay đổi định dạng URL này để phù hợp với cấu trúc URL của trang web bạn muốn kiểm tra.  Ví dụ:

    ```python
    url = f"https://example.com/manga/{x}/chapter/{y}"  # Thay đổi phần này
    ```

2.  **`headers` (Quan trọng):**

   Nhiều trang web yêu cầu headers (thông tin bổ sung trong yêu cầu) để tránh bị chặn hoặc giới hạn truy cập. Thêm headers vào chỗ này, quan trọng nhất là `User-Agent`. Ví dụ:
    ```python
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            # Thêm các header khác nếu cần
        }

    ```
     *  `User-Agent`:  Giả lập trình duyệt để trang web không chặn bot.  Bạn có thể tìm User-Agent của trình duyệt bạn đang dùng bằng cách tìm kiếm "my user agent" trên Google.

3. **Regular Expression (Regex) `image_url_pattern`:**

    Thay đổi biểu thức chính quy này để khớp với URL của hình ảnh chương truyện trên trang web mục tiêu.  Đây là phần quan trọng để xác định xem một chương truyện có tồn tại hay không.

    ```python
    image_url_pattern = re.compile(
        r"https://example\.com/images/manga/\d+/chapter\d+/\d+\.(jpg|png|jpeg)" # Thay đổi phần này
    )
    ```
   *   `\d+`:  Khớp với một hoặc nhiều chữ số (ví dụ: 1, 23, 456).
   *   `\.`: Khớp với dấu chấm (`.`).
   *   `(jpg|png|jpeg)`:  Khớp với một trong các phần mở rộng file ảnh.
    *   **Cách kiểm tra Regex:**  Sử dụng các trang web như [https://regex101.com/](https://regex101.com/) để kiểm tra và điều chỉnh biểu thức chính quy của bạn.

4.  **`BeautifulSoup` (nếu cần):**

    Nếu cấu trúc HTML của trang web mục tiêu khác biệt, bạn có thể cần điều chỉnh cách bạn sử dụng `BeautifulSoup` để trích xuất thông tin.  Tuy nhiên, trong trường hợp này, chúng ta đang dựa vào Regex để tìm URL ảnh, nên thường không cần thay đổi phần này.

### Các Biến Số Quan Trọng (`x`, `y`, `z`, `w`)

*   **`x`**:  Biến số đại diện cho ID của chương truyện (ví dụ: `3000`, `3001`, `3002`,...).
    *   **`range(3000, 4100)` trong hàm `main()`:**  Xác định phạm vi của `x` mà bạn muốn kiểm tra.  Thay đổi các giá trị này để quét một khoảng ID chương khác.
*   **`y`**:  Biến số đại diện cho ID của truyện tranh.  Bạn cần tìm ID này trên trang web mục tiêu.
*   **`z`**:  Số lượng luồng (threads) tối đa chạy đồng thời.  Giá trị cao hơn có thể tăng tốc độ kiểm tra, nhưng cũng có thể gây quá tải cho máy tính của bạn hoặc bị trang web chặn.  Điều chỉnh giá trị này một cách cẩn thận.  Giá trị an toàn thường nằm trong khoảng 20-100.
*   **`w`**:  Số lượng URL được kiểm tra trước khi in ra thông báo "Đã duyệt ... trang".  Điều này chỉ để theo dõi tiến trình và không ảnh hưởng đến logic của chương trình.

### Ví dụ Tùy Chỉnh

Giả sử bạn muốn kiểm tra trang web `https://example.com` với cấu trúc URL như sau:

*   URL truyện: `https://example.com/manga/<manga_id>/`
*   URL chương: `https://example.com/manga/<manga_id>/chapter/<chapter_id>/`
*   URL ảnh: `https://example.com/images/<manga_id>/<chapter_id>/<image_number>.jpg`
*   Manga ID: `12345`
*   Chapter ID bạn muốn quét: từ `1` đến `100`
*   Sử dụng 50 luồng đồng thời.
*   In thông báo sau mỗi 20 URL.

Bạn sẽ thay đổi `Tool.py` như sau:

```python
import requests
import threading
from bs4 import BeautifulSoup
import time
import re

results = {}
count = 0
found = False
lock = threading.Lock()

z = 50  # Số luồng đồng thời
y = 12345  # Manga ID
w = 20  # In thông báo sau mỗi 20 URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

def check_chapter(x):
    global count, found
    if found:
        return

    url = f"https://example.com/manga/{y}/chapter/{x}/" # Thay đổi URL
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        image_url_pattern = re.compile(
            r"https://example\.com/images/\d+/\d+/\d+\.jpg" # Thay đổi Regex
        )
        if image_url_pattern.search(str(soup)):
            with lock:
                if not found:
                    print(f"Tìm thấy chương truyện: {url}")
                    results[x] = f"Chương truyện đã tải hoàn chỉnh: {url}"
                    found = True
                    return
        with lock:
            count += 1
            if count % w == 0:
                print(f"Đã duyệt {count} trang")
        time.sleep(1)  # Giảm thời gian chờ xuống 1 giây (tùy chọn)

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kiểm tra URL {url}: {e}")
        with lock:
            count += 1



def main():
    threads = []
    for x in range(1, 101):  # Quét từ chương 1 đến 100
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

```
</details>

<details>
<summary>🇬🇧 English</summary>

## Introduction

This project is a simple Python tool to brute-force check URLs for manga chapters on a specific website (yurineko.net in the original code). It utilizes multithreading to accelerate the checking process.

## 🚀 Installation and Running

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Rin1809/Burt_Force_URL.git
    cd <project_directory_name>
    ```

2.  **Create and Activate a Virtual Environment:**

    A virtual environment isolates the Python libraries required for the project, preventing conflicts with other projects. `run.bat` is provided to automate this process.

    *   Run `run.bat`. This file will automatically check, create (if needed), and activate the virtual environment, and then run the `Tool.py` script.
    *   If you prefer to do it manually (not recommended unless you know what you're doing):

        ```bash
        # Create the virtual environment (only need to do this once)
        python -m venv moitruongao
        # Activate the virtual environment
        # On Windows:
        moitruongao\Scripts\activate
        # On macOS and Linux:
        source moitruongao/bin/activate
        ```

3.  **Install Dependencies:**

    If you ran `run.bat`, this step is already done automatically. If you're doing it manually, run:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**

    ```bash
    python Tool.py  # If you activated the virtual environment manually
    ```

    Or, more simply, just run `run.bat`.

## ⚙️ How to Edit and Customize

### Changing the Target Website

To check a different website, you need to modify the following parts in `Tool.py`:

1.  **`url` in the `check_chapter` function:**

    Change this URL format to match the URL structure of the website you want to check.  For example:

    ```python
    url = f"https://example.com/manga/{x}/chapter/{y}"  # Modify this part
    ```

2.  **`headers` (Important):**

    Many websites require headers (additional information in the request) to prevent being blocked or rate-limited. Add headers here, the most important one is `User-Agent`. Example:

    ```python
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        # Add other headers if necessary
    }
    ```
     *  `User-Agent`:  Simulates a browser so the website doesn't block the bot. You can find your browser's User-Agent by searching "my user agent" on Google.

3.  **Regular Expression (Regex) `image_url_pattern`:**

    Modify this regular expression to match the URL of the manga chapter image on the target website. This is crucial for determining if a chapter exists.

    ```python
    image_url_pattern = re.compile(
        r"https://example\.com/images/manga/\d+/chapter\d+/\d+\.(jpg|png|jpeg)"  # Modify this part
    )
    ```

    *   `\d+`:  Matches one or more digits (e.g., 1, 23, 456).
    *   `\.`:  Matches a dot (`.`).
    *   `(jpg|png|jpeg)`:  Matches one of the image file extensions.
    *   **How to test Regex:**  Use websites like [https://regex101.com/](https://regex101.com/) to test and adjust your regular expression.

4.  **`BeautifulSoup` (if needed):**

    If the HTML structure of the target website is significantly different, you might need to adjust how you use `BeautifulSoup` to extract information. However, in this case, we're relying on Regex to find image URLs, so you usually don't need to change this part.

### Important Variables (`x`, `y`, `z`, `w`)

*   **`x`**:  Variable representing the chapter ID (e.g., `3000`, `3001`, `3002`,...).
    *   **`range(3000, 4100)` in the `main()` function:**  Defines the range of `x` you want to check. Change these values to scan a different range of chapter IDs.
*   **`y`**:  Variable representing the manga ID.  You need to find this ID on the target website.
*   **`z`**:  The maximum number of threads running concurrently.  A higher value can increase the checking speed, but it can also overload your computer or get you blocked by the website. Adjust this value carefully.  A safe value is usually between 20-100.
*   **`w`**:  The number of URLs checked before printing the "Đã duyệt ... trang" (Checked ... pages) message. This is just for monitoring progress and doesn't affect the program's logic.

### Customization Example

(See the Vietnamese section for the full example code.  The explanation is the same.)

</details>

<details>
<summary>🇯🇵 日本語</summary>

## はじめに

このプロジェクトは、特定のウェブサイト（元のコードではyurineko.net）のマンガのチャプターをブルートフォースでチェックするためのシンプルなPythonツールです。マルチスレッドを使用してチェックプロセスを高速化します。

## 🚀 インストールと実行

1.  **リポジトリをクローン:**

    ```bash
    git clone https://github.com/Rin1809/Burt_Force_URL.git
    cd <プロジェクトディレクトリ名>
    ```

2.  **仮想環境の作成とアクティブ化:**

    仮想環境は、プロジェクトに必要なPythonライブラリを分離し、他のプロジェクトとの競合を防ぎます。`run.bat`はこのプロセスを自動化するために提供されています。

    *   `run.bat`を実行します。このファイルは自動的に仮想環境をチェック、作成（必要な場合）、アクティブ化し、`Tool.py`スクリプトを実行します。
    *   手動で行う場合（何をしているかわからない限り推奨しません）：

        ```bash
        # 仮想環境を作成（一度だけ行う必要があります）
        python -m venv moitruongao
        # 仮想環境をアクティブ化
        # Windowsの場合:
        moitruongao\Scripts\activate
        # macOSおよびLinuxの場合:
        source moitruongao/bin/activate
        ```

3.  **依存関係のインストール:**

    `run.bat`を実行した場合、この手順はすでに自動的に行われています。手動で行う場合は、以下を実行します。

    ```bash
    pip install -r requirements.txt
    ```

4.  **アプリケーションの実行:**

    ```bash
    python Tool.py  # 仮想環境を手動でアクティブ化した場合
    ```

    または、より簡単に、`run.bat`を実行するだけです。

## ⚙️ 編集とカスタマイズの方法

### ターゲットWebサイトの変更

別のWebサイトをチェックするには、`Tool.py`の次の部分を変更する必要があります。

1.  **`check_chapter`関数内の`url`:**

    このURL形式を、チェックしたいWebサイトのURL構造に合わせて変更します。例：

    ```python
    url = f"https://example.com/manga/{x}/chapter/{y}"  # この部分を変更
    ```

2.  **`headers`（重要）:**

    多くのWebサイトでは、ブロックされたりレート制限されたりするのを防ぐために、ヘッダー（リクエスト内の追加情報）が必要です。ここにヘッダーを追加します。最も重要なのは`User-Agent`です。例：
    ```python
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        # 必要に応じて他のヘッダーを追加
    }
    ```

    *   `User-Agent`:  Webサイトがボットをブロックしないように、ブラウザをシミュレートします。Googleで「my user agent」を検索すると、ブラウザのUser-Agentを見つけることができます。

3.  **正規表現（Regex）`image_url_pattern`:**

    この正規表現を、ターゲットWebサイトのマンガのチャプター画像のURLに一致するように変更します。これは、チャプターが存在するかどうかを判断するために非常に重要です。

    ```python
    image_url_pattern = re.compile(
        r"https://example\.com/images/manga/\d+/chapter\d+/\d+\.(jpg|png|jpeg)"  # この部分を変更
    )
    ```

    *   `\d+`:  1つ以上の数字に一致します（例：1、23、456）。
    *   `\.`:  ドット（`.`）に一致します。
    *   `(jpg|png|jpeg)`:  いずれかの画像ファイル拡張子に一致します。
    *   **正規表現のテスト方法:**  [https://regex101.com/](https://regex101.com/) のようなWebサイトを使用して、正規表現をテストおよび調整します。

4.  **`BeautifulSoup`（必要な場合）:**

    ターゲットWebサイトのHTML構造が大幅に異なる場合は、情報を抽出するために`BeautifulSoup`の使用方法を調整する必要がある場合があります。ただし、この場合は画像URLを見つけるために正規表現に依存しているため、通常はこの部分を変更する必要はありません。

### 重要な変数（`x`、`y`、`z`、`w`）

*   **`x`**:  チャプターIDを表す変数（例：`3000`、`3001`、`3002`、...）。
    *   **`main()`関数内の`range(3000, 4100)`:**  チェックする`x`の範囲を定義します。これらの値を変更して、異なるチャプターIDの範囲をスキャンします。
*   **`y`**:  マンガIDを表す変数。ターゲットWebサイトでこのIDを見つける必要があります。
*   **`z`**:  同時に実行されるスレッドの最大数。値を大きくするとチェック速度が向上する可能性がありますが、コンピュータに過負荷がかかったり、Webサイトによってブロックされたりする可能性もあります。この値は慎重に調整してください。安全な値は通常20〜100の間です。
*   **`w`**:  「Đã duyệt ... trang」（...ページをチェックしました）メッセージを出力する前にチェックされるURLの数。これは進行状況を監視するためだけであり、プログラムのロジックには影響しません。

### カスタマイズの例

(完全なコード例については、ベトナム語のセクションを参照してください。説明は同じです。)

</details>
