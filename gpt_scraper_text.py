import json

if __name__ == '__main__':
    with open("data/rosenheim_url_summaries_2.json", "r") as f:
        url_summaries_json = json.load(f)

    with open("data/rosenheim_urls_summaries2.txt", "w") as f:
        for url_summary in url_summaries_json:
            f.write(url_summary["url"] + "\n")
            f.write(url_summary["answer"] + "\n")
            f.write("\n")