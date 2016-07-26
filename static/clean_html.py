import sys

def clean_html(html_file):
    """Remove unnecessary tags from slides."""
    clean_file = (html_file.replace("<section><section><image>", "")
                           .replace("</image></section></section>", ""))
    return clean_file

if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as f:
            clean_file = clean_html(f.read())
        with open(sys.argv[1], "w") as f:
            f.write(clean_file)
        print("Successfully adjusted.")
    except IndexError:
        print("Provide name of the slide.")
