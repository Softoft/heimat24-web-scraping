if __name__ == '__main__':
    with open("data/toulon_new_15_11_3.csv") as file:
        text = file.read()

    urls = text.split(",")

    unique_urls = list(set(urls))

    with open("data/toulon_urls_unique.txt", "w") as file:
        for url in unique_urls:
            file.write(url + "\n")