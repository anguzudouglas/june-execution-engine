from fastapi.responses import HTMLResponse


def get_docs_html():

    return """
<!DOCTYPE html>
<html>
<head>
    <title>Python Sandbox API</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            max-width: 1000px;
            margin: auto;
            padding: 40px;
            line-height: 1.6;
        }

        h1, h2, h3 {
            color: #38bdf8;
        }

        pre {
            background: #1e293b;
            padding: 16px;
            border-radius: 10px;
            overflow-x: auto;
        }

        code {
            color: #facc15;
        }

        .card {
            background: #111827;
            padding: 20px;
            border-radius: 14px;
            margin-bottom: 20px;
            border: 1px solid #1e293b;
        }

        .endpoint {
            color: #4ade80;
            font-weight: bold;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        td, th {
            border: 1px solid #334155;
            padding: 12px;
        }

        th {
            background: #1e293b;
        }
    </style>
</head>

<body>

<h1>Python Sandbox API</h1>

<p>
AI-focused Python execution environment for:
</p>

<ul>
    <li>Mathematics</li>
    <li>Data science</li>
    <li>Visualization</li>
    <li>CSV analysis</li>
    <li>Machine learning</li>
    <li>Artifact generation</li>
</ul>

<div class="card">

<h2>Base URL</h2>

<pre>https://june-python-sanbox.onrender.com</pre>

</div>

<div class="card">

<h2>POST /execute</h2>

<p class="endpoint">
POST /execute
</p>

<p>
Execute Python code safely inside the sandbox.
</p>

<h3>Request Body</h3>

<pre>{
  "code": "print(2 + 2)",
  "timeout": 15,
  "files": [],
  "session_id": null
}</pre>

<h3>Fields</h3>

<table>
<tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
</tr>

<tr>
    <td>code</td>
    <td>string</td>
    <td>Python code to execute</td>
</tr>

<tr>
    <td>timeout</td>
    <td>integer</td>
    <td>Execution timeout in seconds</td>
</tr>

<tr>
    <td>files</td>
    <td>array</td>
    <td>Optional uploaded files in base64</td>
</tr>

<tr>
    <td>session_id</td>
    <td>string/null</td>
    <td>Optional execution session</td>
</tr>

</table>

</div>

<div class="card">

<h2>Success Response</h2>

<pre>{
  "success": true,
  "status_code": 200,
  "execution_time": 0.42,

  "stdout": "4",
  "stderr": "",

  "artifacts": [],

  "error": null
}</pre>

</div>

<div class="card">

<h2>Error Response</h2>

<pre>{
  "success": false,
  "status_code": 400,

  "stdout": "",
  "stderr": "ZeroDivisionError",

  "artifacts": [],

  "error": {
    "type": "RuntimeError",
    "message": "division by zero",
    "friendly_message":
      "The Python code raised an exception during execution."
  }
}</pre>

</div>

<div class="card">

<h2>Artifacts</h2>

<p>
Generated files are returned either:
</p>

<ul>
    <li>Inline base64 (small files)</li>
    <li>Temporary URL (large files)</li>
</ul>

<h3>Inline Artifact</h3>

<pre>{
  "name": "chart.png",
  "delivery": "inline",
  "base64": "..."
}</pre>

<h3>URL Artifact</h3>

<pre>{
  "name": "report.pdf",
  "delivery": "url",
  "url": "https://june-python-sanbox.onrender.com/artifact/..."
}</pre>

</div>

<div class="card">

<h2>GET /artifact/{artifact_id}/{filename}</h2>

<p class="endpoint">
GET /artifact/{artifact_id}/{filename}
</p>

<p>
Download generated files.
</p>

<p>
Artifacts automatically expire after 24 hours.
</p>

</div>

<div class="card">

<h2>Supported Libraries</h2>

<ul>
    <li>numpy</li>
    <li>pandas</li>
    <li>matplotlib</li>
    <li>sympy</li>
    <li>scipy</li>
    <li>scikit-learn</li>
    <li>plotly</li>
    <li>seaborn</li>
    <li>polars</li>
    <li>openpyxl</li>
</ul>

</div>

<div class="card">

<h2>Security Restrictions</h2>

<p>
Blocked imports:
</p>

<pre>
os
subprocess
socket
requests
multiprocessing
ctypes
</pre>

</div>

<div class="card">

<h2>Example: Generate Chart</h2>

<pre>{
  "code": "
import matplotlib.pyplot as plt

plt.plot([1,2,3], [4,5,6])

plt.savefig('chart.png')

print('done')
"
}</pre>

</div>

<div class="card">

<h2>Example: CSV Analysis</h2>

<pre>{
  "code": "
import pandas as pd

df = pd.read_csv('sales.csv')

print(df.describe())
",
  "files": [
    {
      "name": "sales.csv",
      "base64": "..."
    }
  ]
}</pre>

</div>

<div class="card">

<h2>Status Codes</h2>

<table>

<tr>
    <th>Code</th>
    <th>Meaning</th>
</tr>

<tr>
    <td>200</td>
    <td>Execution successful</td>
</tr>

<tr>
    <td>400</td>
    <td>Code/runtime error</td>
</tr>

<tr>
    <td>408</td>
    <td>Execution timeout</td>
</tr>

<tr>
    <td>500</td>
    <td>Internal server error</td>
</tr>

</table>

</div>

</body>
</html>
"""
