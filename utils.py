import os
import re
import random
import requests 


def get_img_from_pattern(text):
    pattern = pattern = r"https://preview\.redd\.it/[^\"]+"
    # search all matches in text
    matches = re.findall(pattern, text)
    # return list of matches
    return matches

def post_process_urls(urls):
    # remove empty strings
    urls = [url for url in urls if len(url) > 0]
    # replace \\u0026 with &
    urls = [url.replace("\\u0026", "&") for url in urls]
    # replace &amp; with &
    urls = [url.replace("&amp;", "&") for url in urls]
    # replace \\ with /
    urls = [url.replace("\\", "/") for url in urls]

    max_size = {}
    for url in urls:
        if "blur=" in url:
            continue

        filename = url.split("?")[0].split("/")[-1]
        
        filesize = 0
        if "width=" in url:
            filesize = int(url.split("?")[1].split("&")[0].replace("width=", ""))

        if filename in max_size and filesize < max_size[filename]['size']:
            continue
        max_size[filename] = {'size': filesize, 'url': url}

    last_urls = [url['url'] for url in max_size.values()]

    return last_urls


def download_images_from_url(urls):
    os.makedirs("images", exist_ok=True)

    # download images from urls
    for url in urls:
        filename = url.split("?")[0].split("/")[-1]
        
        print(f"Downloading {url} in images/{filename}")
        r = requests.get(url, allow_redirects=True, timeout=100)
        
        # check status, content-type and size
        if r.status_code == 200:
            with open(f"images/{filename}", "wb") as f:
                f.write(r.content)
        else:
            print(f"Failed to download {url}")