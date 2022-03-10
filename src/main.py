#%%
import zipfile
from pathlib import Path
import glob
import shutil

file_dir = Path(__file__).parent

# remove the previous noton directory contain "muha"


def remove_prev_dir(contain_str="*uhammad*"):
    main_path = Path(file_dir.parent)
    prev_dir_name = main_path.glob(contain_str)
    for dir_name in prev_dir_name:
        shutil.rmtree(dir_name)


# get last update file in drirectory
def extract_new_zip():
    notion_zip_path = Path(
        file_dir.parent, "notion_zip"
    )  # Path(__file__).parent.parent
    list_of_paths = notion_zip_path.glob("*.zip")
    zip_file_new = max(list_of_paths, key=lambda p: p.stat().st_ctime)
    print(f"new_file:{zip_file_new}")
    with zipfile.ZipFile(zip_file_new, "r") as zip_ref:
        zip_ref.extractall(notion_zip_path.parent)


def rename_html():
    list_html = file_dir.parent.glob("*.html")
    html_last = max(list_html, key=lambda p: p.stat().st_ctime)
    target_filename = Path(html_last.parent, "index.html")
    html_last.rename(target_filename)


def main():
    remove_prev_dir()
    extract_new_zip()
    rename_html()


if __name__ == "__main__":
    main()
# %%
