import argparse
import requests
import yaml
import csv
from prettytable import PrettyTable
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

def load_fingerprints():
    with open("fingerprints.yml", "r") as f:
        fingerprints = yaml.safe_load(f)
    return fingerprints


def check_cms(url, fingerprints):
    if not url.startswith("http"):
        url = "http://" + url
    response = requests.get(url)
    for cms, rules in fingerprints.items():
        for rule in rules:
            if rule in response.content.decode("utf-8"):
                return cms
    return "unknown"


def check_from_file(file_path, fingerprints):
    result = {}
    with open(file_path, "r") as f:
        for line in f:
            url = line.strip()
            cms = check_cms(url, fingerprints)
            result[url] = cms
    return result


def check_from_url(url, fingerprints):
    return check_cms(url, fingerprints)


@app.route('/api', methods=['GET'])
def api():
    query = request.args.get('query', '')
    output = request.args.get('output', 'json')
    result = {}
    if query:
        fingerprints = load_fingerprints()
        if query.startswith('http'):
            result[query] = check_from_url(query, fingerprints)
        else:
            result = check_from_file(query, fingerprints)

    if output == 'xml':
        response = app.response_class(
            response=result_to_xml(result),
            mimetype='application/xml'
        )
    else:
        response = jsonify(result)

    return response


def result_to_xml(result):
    xml = []
    for k, v in result.items():
        xml.append(f'<url>{k}</url><cms>{v}</cms>')
    return f'<result>{"".join(xml)}</result>'


def result_to_csv(result):
    fieldnames = ["URL", "CMS"]
    output = []
    for url, cms in result.items():
        output.append({"URL": url, "CMS": cms})
    return output, fieldnames


def result_to_html(result):
    table = PrettyTable()
    table.field_names = ["URL", "CMS"]
    for url, cms in result.items():
        table.add_row([url, cms])
    return table.get_html_string()


def main():
    fingerprints = load_fingerprints()
    table = PrettyTable()
    table.field_names = ["URL", "CMS"]
    for url in urls:
        cms = check_cms(url, fingerprints)
        table.add_row([url, cms])
    print(table)






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Specify the URL to be queried")
    parser.add_argument("-f", "--file", help="Specify the file to be queried")
    parser.add_argument("-A", "--api", action='store_true', help="Enable API")
    parser.add_argument("-m", "--output-format", help="Output file format")
    parser.add_argument("-c", "--output-file", help="Output file name")

    args = parser.parse_args()

    if args.api:
        app.run(host='0.0.0.0', port='891')
    elif args.target:
        fingerprints = load_fingerprints()
        cms = check_from_url(args.target, fingerprints)
        if args.output_format:
            if args.output_format == "csv":
                if args.output_file:
                    with open(args.output_file, "w") as f:
                        f.write("URL,CMS\n")
                        f.write(f"{args.target},{cms}\n")
                else:
                    print("Please specify the output file name")
            elif args.output_format == "html":
                if args.output_file:
                    with open(args.output_file, "w") as f:
                        f.write("<html><body><table>")
                        f.write("<tr><th>URL</th><th>CMS</th></tr>")
                        f.write(f"<tr><td>{args.target}</td><td>{cms}</td></tr>")
                        f.write("</table></body></html>")
                else:
                    print("Please specify the output file name")
            else:
                print("Unsupported output file format")
        else:
            table = PrettyTable()
            table.field_names = ["URL", "CMS"]
            table.add_row([args.target, cms])
            print(table)
    elif args.file:
        fingerprints = load_fingerprints()
        result = check_from_file(args.file, fingerprints)
        if args.output_format:
            if args.output_format == "csv":
                if args.output_file:
                    with open(args.output_file, "w") as f:
                        f.write("URL,CMS\n")
                        for k, v in result.items():
                            f.write(f"{k},{v}\n")
                else:
                    print("Please specify the output file name")

            elif args.output_format == "html":
                if args.output_file:
                    with open(args.output_file, "w") as f:
                        f.write("<html><body><table>")
                        f.write("<tr><th>URL</th><th>CMS</th></tr>")
                        for k, v in result.items():
                            f.write(f"<tr><td>{k}</td><td>{v}</td></tr>")
                        f.write("</table></body></html>")
                else:
                    print("Please specify the output file name")

            else:
                print("Unsupported output file format")
        else:
            table = PrettyTable()
            table.field_names = ["URL", "CMS"]
            for k, v in result.items():
                table.add_row([k, v])
            print(table)
    else:
        print("Please specify the URL to be queried using -t, or specify the file to be queried using -f.")

