import requests
from lxml import html
import base64
import re
import time
def safe_decode(data):
    # 补足长度以满足base64解码要求
    padding = '=' * (4 - len(data) % 4)
    data += padding
    try:
        return base64.b64decode(data).decode('utf-8')
    except Exception as e:
        print(f"Error decoding data: {e}")
        return None

def safe_encode(data):
    try:
        byte_data = data.encode('utf-8')
        encoded_data = base64.b64encode(byte_data)
        return encoded_data.decode('utf-8')
    except Exception as e:
        print(f"Error encoding data: {e}")
        return None

def extract_remarks(url):
    # 使用正则表达式匹配 'remarks=' 后面的内容直到下一个 '&'
    regex = r'remarks=(.*?)&'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None

def process_url(url, max_retries=3, retry_delay=5):
    retries = 0
    while retries <= max_retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            tree = html.fromstring(response.text)
            a_tag = tree.xpath("//div[@class='header']/a")[0]
            link = a_tag.get("href")

            # 验证链接是否有效
            if not link.startswith('http'):
                raise ValueError("Invalid URL format")

            # 下载文件内容
            with requests.get(link, stream=True, timeout=10) as r:
                r.raise_for_status()
                file_content = r.content
                return file_content
        except Exception as e:
            print(f"An error occurred: {e}")
            retries += 1
            if retries > max_retries:
                print("Maximum retries exceeded.")
                return None
            time.sleep(retry_delay)

def transform_data(data):
    transformed_data = ""
    data = safe_decode(data)
    # print(data)
    
    # 获取所有行的列表
    lines = data.strip().split('\n')
    
    for i, line in enumerate(lines):
        if line.startswith("ssr://"):
            encoded_line = line.replace("ssr://", "").replace("-", "+").replace("_", "/")
            decoded_line = safe_decode(encoded_line)
            remarks = extract_remarks(decoded_line)
            txt=safe_decode(remarks.replace("-", "+").replace("_", "/"))
            xx=safe_encode(txt.replace("[TG]@MFJD666","")+"[TG]阡 风")
            if remarks:
                decoded_line = decoded_line.replace(remarks, xx).replace("+", "-").replace("/", "_")
                print(decoded_line)
                transformed_line = safe_encode(decoded_line)
                transformed_line = "ssr://" + transformed_line
                
                # 只有当不是最后一行时才添加换行符
                if i < len(lines) - 1:
                    transformed_data += transformed_line + "\n"
                else:
                    transformed_data += transformed_line
        else:
            # 同样检查是否为最后一行
            if i < len(lines) - 1:
                transformed_data += line + "\n"
            else:
                transformed_data += line

    return safe_encode(transformed_data)

# 主程序入口
if __name__ == "__main__":
    url = "https://jc.guanxi.cloudns.be/"
    file_content = process_url(url)
    if file_content is not None:
        # 将文件内容解码为字符串
        data = file_content.decode('utf-8')
        transformed_data = transform_data(data)
        with open('guanxi.txt', 'w', encoding='utf-8') as file:
            file.write(transformed_data)
    else:
        print("Failed to download the file.")