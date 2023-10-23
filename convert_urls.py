import re


def filter_rosenheim_urls(urls):
    return [url for url in urls if re.match(r".*www\.rosenheim\.de.*", url)]


def read_all():
    with open("data/rosenheim_urls", "r") as f:
        urls = f.readlines()
        urls = [url.strip().replace('"', "") for url in urls]
    return urls


def write_all_rosenheim_urls_to_file(urls):
    with open("data/all_rosenheim_urls", "w") as f:
        for url in filter_rosenheim_urls(urls):
            f.write(url)


def write_rosenheim_urls():
    urls = read_all()
    write_all_rosenheim_urls_to_file(urls)


def get_all_rosenheim_first_path(urls):
    rosenheim_urls = filter_rosenheim_urls(urls)
    return list(set(list(map(lambda url: url.split("/")[3], rosenheim_urls))))


if __name__ == '__main__':
    print("\n".join(get_all_rosenheim_first_path(read_all())))
