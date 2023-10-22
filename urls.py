import re

if __name__ == '__main__':
    with open("rosenheim_urls", "r") as f:
        urls = f.readlines()

    with open("all_rosenheim_urls", "w") as f:
        for url in urls:
            if re.match(r".*www\.rosenheim\.de.*", url):
                f.write(url)
