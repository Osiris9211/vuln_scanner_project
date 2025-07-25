import os
from flask import Flask, render_template, request, send_file, url_for
from core.scanner import AdvancedScanner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url'].strip()
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url

    login_url = request.form.get("login_url")
    username = request.form.get("username")
    password = request.form.get("password")

    auth_creds = None
    if login_url and username and password:
        auth_creds = {
            "login_url": login_url,
            "data": {"username": username, "password": password}
        }

    scanner = AdvancedScanner(url, auth_creds=auth_creds)
    results, report_path = scanner.run()

    # Pass only filename (no directories) to the template
    report_filename = os.path.basename(report_path)
    return render_template('results.html', url=url, results=results, report_filename=report_filename)

@app.route('/download/<path:filename>')
def download_report(filename):
    base_dir = os.path.expanduser('~/scanner_reports')
    full_path = os.path.join(base_dir, filename)

    # Security check: ensure the requested file is under base_dir
    if not os.path.commonpath([os.path.abspath(full_path), os.path.abspath(base_dir)]) == os.path.abspath(base_dir):
        return "Invalid file path", 400

    if os.path.exists(full_path):
        return send_file(full_path, as_attachment=True)
    else:
        return "Report not found.", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)

"""
Web Vulnerability Scanner
Developed by Osiris9211
GitHub: https://github.com/Osiris9211
LinkedIn: https://www.linkedin.com/in/osiris9211

© 2025 Osiris9211 - All rights reserved.
"""
