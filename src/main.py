#%%
import zipfile
from pathlib import Path
import glob


# get last update file in drirectory
notion_zip_path = Path("/home/hattajr/personal/project/notion-to-gh/notion_zip") #Path(__file__).parent.parent
list_of_paths = notion_zip_path.glob('*.zip')
zip_file_new = max(list_of_paths, key=lambda p: p.stat().st_ctime)

with zipfile.ZipFile(zip_file_new, 'r') as zip_ref:
    zip_ref.extractall(notion_zip_path.parent)


list_html = Path("/home/hattajr/personal/project/notion-to-gh").glob('*.html')
html_last = max(list_html, key=lambda p: p.stat().st_ctime)
target_filename = Path(html_last.parent,"index.html")
html_last.rename(target_filename)

