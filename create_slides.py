import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_name', type=str, help='Name of the jupyter notebook.')
args = parser.parse_args()


def clean_html(html_file):
    """Remove unnecessary tags from slides."""
    clean_file = (html_file.replace('<section><section><image>', '')
                  .replace('</image></section></section>', ''))
    return clean_file


def main():
    """Convert the notebook to slides and then do some cleaning."""
    try:
        output = subprocess.check_output(
            ['jupyter', 'nbconvert', args.file_name, '--to', 'slides', '--reveal-prefix', 'reveal.js-3.1.0',
             '--config', 'static/slides_config.py'], stderr=subprocess.STDOUT).decode('utf-8')
        print(output.rstrip())

        slide_name = output.split(' ')[-1].rstrip()
        with open(slide_name, 'r') as f:
            clean_file = clean_html(f.read())
        with open(slide_name, 'w') as f:
            f.write(clean_file)
        print('Successfully adjusted.')
    except IndexError:
        print('Provide name of the slide.')


main()
