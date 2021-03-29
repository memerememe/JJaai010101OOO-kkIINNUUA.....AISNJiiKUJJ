from pathlib import Path
import zipfile
import requests
import wget
from tqdm import tqdm
import platform
import os
platformname = platform.system()
if(platformname=="Windows"):
    trueorfalse = Path('chrome-win').is_dir()
    trueorfalse2 = Path('chromedriver_win32').is_dir()

    if(trueorfalse==True and trueorfalse2==True):
        pass
    else:
        
        block_size = 1024 #1 Kibibyte
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2FLAST_CHANGE?&alt=media"
        r = requests.get(url)

        number = str(r.content)
        f1 = number.replace("b'","")
        f2  = f1.replace("'","")
        print("Obtaining dependencies")
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F"+f2+"%2Fchrome-win.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chrome-win.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F"+f2+"%2Fchromedriver_win32.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chromedriver_win32.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        print("Unzipping dependencies, please wait.")
        with zipfile.ZipFile("chrome-win.zip","r") as zip_ref:
            zip_ref.extractall("chrome-win")
        with zipfile.ZipFile("chromedriver_win32.zip","r") as zip_ref:
            zip_ref.extractall("driver")
        if os.path.exists("chrome-win.zip"):
            os.remove("chrome-win.zip")
        if os.path.exists("chromedriver-win32.zip"):
            os.remove("chromedriver-win32.zip")
        print("Complete.")
elif(platformname=="Linux"):
    trueorfalse = Path('chrome-linux').is_dir()
    trueorfalse2 = Path('chromedriver_linux').is_dir()

    if(trueorfalse==True and trueorfalse2==True):
        pass
    else:
        
        block_size = 1024 #1 Kibibyte
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2FLAST_CHANGE?&alt=media"
        r = requests.get(url)

        number = str(r.content)
        f1 = number.replace("b'","")
        f2  = f1.replace("'","")
        print("Obtaining dependencies")
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F"+f2+"%2Fchrome-linux.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chrome-linux.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F"+f2+"%2Fchromedriver_linux64.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chromedriver_linux.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        print("Unzipping dependencies, please wait.")
        with zipfile.ZipFile("chrome-linux.zip","r") as zip_ref:
            zip_ref.extractall("chrome-linux")
        with zipfile.ZipFile("chromedriver_linux.zip","r") as zip_ref:
            zip_ref.extractall("driver")
        if os.path.exists("chrome-linux.zip"):
            os.remove("chrome-linux.zip")
        if os.path.exists("chromedriver-linux.zip"):
            os.remove("chromedriver-linux.zip")
        print("Complete.")
elif(platformname=="Darwin"):
    trueorfalse = Path('chrome-macos').is_dir()
    trueorfalse2 = Path('chromedriver_macos').is_dir()

    if(trueorfalse==True and trueorfalse2==True):
        pass
    else:
        
        block_size = 1024 #1 Kibibyte
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Mac%2FLAST_CHANGE?&alt=media"
        r = requests.get(url)

        number = str(r.content)
        f1 = number.replace("b'","")
        f2  = f1.replace("'","")
        print("Obtaining dependencies")
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Mac%2F"+f2+"%2Fchrome-mac.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chrome-macos.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        url = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Mac%2F"+f2+"%2Fchromedriver_mac64.zip?&alt=media"
        r = requests.get(url)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        content = r.content
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open('chromedriver_macos.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        print("Unzipping dependencies, please wait.")
        with zipfile.ZipFile("chrome-macos.zip","r") as zip_ref:
            zip_ref.extractall("chrome-macos")
        with zipfile.ZipFile("chromedriver_macos.zip","r") as zip_ref:
            zip_ref.extractall("driver")
        if os.path.exists("chrome-macos.zip"):
            os.remove("chrome-macos.zip")
        if os.path.exists("chromedriver-macos.zip"):
            os.remove("chromedriver-macos.zip")
        print("Complete.")
