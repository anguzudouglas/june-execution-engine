from fastapi.responses import HTMLResponse


def get_docs_html():

    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>June Python Sandbox API</title>

<style>

body {
    background: #020617;
    color: #e2e8f0;
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: auto;
    padding: 40px;
    line-height: 1.8;
}

h1 {
    font-size: 42px;
    color: #38bdf8;
}

h2 {
    color: #7dd3fc;
    margin-top: 60px;
}

h3 {
    color: #38bdf8;
}

p {
    color: #cbd5e1;
}

.card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 28px;
    margin-top: 25px;
}

pre {
    background: #020617;
    padding: 18px;
    border-radius: 12px;
    overflow-x: auto;
    border: 1px solid #1e293b;
    color: #f8fafc;
}

code {
    color: #facc15;
}

.endpoint {
    color: #4ade80;
    font-weight: bold;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th {
    background: #1e293b;
}

td, th {
    border: 1px solid #334155;
    padding: 14px;
    text-align: left;
}

ul li {
    margin-bottom: 10px;
}

.badge {
    display: inline-block;
    background: #1e293b;
    color: #38bdf8;
    padding: 6px 12px;
    border-radius: 999px;
    margin-right: 10px;
    margin-bottom: 10px;
    font-size: 14px;
}

.section-title {
    margin-top: 80px;
}

</style>

</head>

<body>

<h1>June Python Sandbox API</h1>

<p>
AI-focused Python execution environment for autonomous agents, LLM systems,
data science workloads, visualization, mathematical computation, and artifact generation.
</p>

<div class="badge">FastAPI</div>
<div class="badge">Python 3.11</div>
<div class="badge">AI Agent Ready</div>
<div class="badge">Data Science</div>
<div class="badge">Visualization</div>
<div class="badge">Sandboxed Execution</div>

<div class="card">

<h2>Overview</h2>

<p>
The June Python Sandbox API allows AI systems and developers to execute Python code securely
inside an isolated environment with preinstalled scientific and data analysis libraries.
</p>

<p>
The API supports:
</p>

<ul>
<li>Data analysis with Pandas and Polars</li>
<li>Mathematical computation using NumPy, SciPy, and SymPy</li>
<li>Machine learning workflows using Scikit-learn</li>
<li>Visualization and plotting</li>
<li>File generation (CSV, PNG, PDF, Excel, JSON)</li>
<li>Temporary artifact hosting</li>
<li>Structured error reporting for LLM reasoning</li>
</ul>

</div>

<div class="card">

<h2>Base URL</h2>

<pre>https://june-python-sanbox.onrender.com</pre>

</div>

<h2 class="section-title">Execution Architecture</h2>

<div class="card">

<pre>
Client / AI Agent
        ↓
POST /execute
        ↓
Request Validation
        ↓
Sandboxed Python Runtime
        ↓
Artifact Collection
        ↓
Structured JSON Response
        ↓
AI Agent Reasoning
</pre>

</div>

<h2 class="section-title">API Endpoints</h2>

<div class="card">

<h3 class="endpoint">POST /execute</h3>

<p>
Execute Python code inside the sandbox.
</p>

<h3>Request Body</h3>

<pre>
{
  "code": "print(2 + 2)",
  "timeout": 15,
  "files": []
}
</pre>

<h3>Request Fields</h3>

<table>

<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>

<tr>
<td>code</td>
<td>string</td>
<td>Python code to execute</td>
<td>Yes</td>
</tr>

<tr>
<td>timeout</td>
<td>integer</td>
<td>Execution timeout in seconds</td>
<td>No</td>
</tr>

<tr>
<td>files</td>
<td>array</td>
<td>Input files encoded as base64</td>
<td>No</td>
</tr>

</table>

</div>

<div class="card">

<h3 class="endpoint">GET /artifact/{artifact_id}/{filename}</h3>

<p>
Download generated artifacts.
</p>

<p>
Artifacts expire automatically after 24 hours.
</p>

</div>

<h2 class="section-title">Response Structure</h2>

<div class="card">

<h3>Successful Execution</h3>

<pre>
{
  "success": true,
  "status_code": 200,

  "execution_time": 0.42,

  "stdout": "analysis complete",
  "stderr": "",

  "artifacts": [],

  "error": null
}
</pre>

<h3>Execution Failure</h3>

<pre>
{
  "success": false,
  "status_code": 400,

  "stdout": "",
  "stderr": "Traceback...",

  "artifacts": [],

  "error": {
    "type": "RuntimeError",
    "message": "division by zero",
    "friendly_message":
      "The Python code raised an exception during execution."
  }
}
</pre>

</div>

<h2 class="section-title">Artifact System</h2>

<div class="card">

<p>
Generated files are automatically detected and returned to the client.
</p>

<h3>Supported Artifact Types</h3>

<ul>
<li>PNG</li>
<li>JPEG</li>
<li>PDF</li>
<li>CSV</li>
<li>Excel (.xlsx)</li>
<li>JSON</li>
<li>HTML</li>
<li>SVG</li>
</ul>

<h3>Delivery Modes</h3>

<table>

<tr>
<th>Mode</th>
<th>Description</th>
</tr>

<tr>
<td>inline</td>
<td>Small files returned directly as base64</td>
</tr>

<tr>
<td>url</td>
<td>Large files hosted temporarily with downloadable URL</td>
</tr>

</table>

<h3>Inline Artifact Example</h3>

<pre>
{
  "name": "chart.png",
  "delivery": "inline",
  "base64": "..."
}
</pre>

<h3>URL Artifact Example</h3>

<pre>
{
  "name": "report.pdf",
  "delivery": "url",
  "url":
    "https://june-python-sanbox.onrender.com/artifact/..."
}
</pre>

</div>

<h2 class="section-title">File Uploads</h2>

<div class="card">

<p>
Files can be uploaded using base64 encoding.
</p>

<h3>Upload Example</h3>

<pre>
{
  "files": [
    {
      "name": "sales.csv",
      "base64": "..."
    }
  ]
}
</pre>

<p>
Uploaded files are restored inside the execution workspace before code execution.
</p>

</div>

<h2 class="section-title">Installed Libraries</h2>

<div class="card">

<table>

<tr>
<th>Category</th>
<th>Libraries</th>
</tr>

<tr>
<td>Data Science</td>
<td>pandas, polars, numpy</td>
</tr>

<tr>
<td>Machine Learning</td>
<td>scikit-learn</td>
</tr>

<tr>
<td>Math</td>
<td>sympy, scipy</td>
</tr>

<tr>
<td>Visualization</td>
<td>matplotlib, seaborn, plotly</td>
</tr>

<tr>
<td>Excel</td>
<td>openpyxl</td>
</tr>

</table>

</div>

<h2 class="section-title">Visualization Examples</h2>

<div class="card">

<h3>Generate Chart</h3>

<pre>
{
  "code": "
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x, y)

plt.title('Sales')

plt.savefig('sales_chart.png')

print('chart generated')
"
}
</pre>

</div>

<h2 class="section-title">Data Analysis Examples</h2>

<div class="card">

<h3>Analyze CSV Dataset</h3>

<pre>
{
  "code": "
import pandas as pd

df = pd.read_csv('sales.csv')

print(df.describe())

df.to_csv('summary.csv')
",

  "files": [
    {
      "name": "sales.csv",
      "base64": "..."
    }
  ]
}
</pre>

</div>

<h2 class="section-title">Error Handling</h2>

<div class="card">

<table>

<tr>
<th>Status Code</th>
<th>Meaning</th>
</tr>

<tr>
<td>200</td>
<td>Execution successful</td>
</tr>

<tr>
<td>400</td>
<td>Runtime or syntax error</td>
</tr>

<tr>
<td>408</td>
<td>Execution timeout</td>
</tr>

<tr>
<td>500</td>
<td>Internal sandbox failure</td>
</tr>

</table>

<h3>Timeout Example</h3>

<pre>
{
  "success": false,
  "status_code": 408,

  "error": {
    "type": "TimeoutError",
    "message": "Execution exceeded 15 seconds."
  }
}
</pre>

</div>

<h2 class="section-title">Security Restrictions</h2>

<div class="card">

<p>
Dangerous modules are blocked to prevent system access and abuse.
</p>

<h3>Blocked Imports</h3>

<pre>
os
subprocess
socket
ctypes
multiprocessing
requests
shutil
</pre>

<p>
Network access and operating system access are disabled.
</p>

</div>

<h2 class="section-title">LLM Integration Guide</h2>

<div class="card">

<p>
Recommended workflow for AI agents:
</p>

<pre>
1. Generate Python code
2. Send POST request to /execute
3. Parse structured JSON response
4. Inspect stdout/stderr
5. Download artifacts if present
6. Retry or refine code if execution failed
</pre>

<h3>Recommended Retry Strategy</h3>

<ul>
<li>Retry syntax errors after code correction</li>
<li>Retry timeouts with optimized computation</li>
<li>Inspect stderr for debugging</li>
<li>Use generated artifacts for follow-up reasoning</li>
</ul>

</div>

<h2 class="section-title">Resource Limits</h2>

<div class="card">

<table>

<tr>
<th>Limit</th>
<th>Value</th>
</tr>

<tr>
<td>Execution Timeout</td>
<td>15 seconds</td>
</tr>

<tr>
<td>Artifact Expiry</td>
<td>24 hours</td>
</tr>

<tr>
<td>Network Access</td>
<td>Disabled</td>
</tr>

<tr>
<td>Persistent Sessions</td>
<td>Not yet supported</td>
</tr>

</table>

</div>

<h2 class="section-title">Best Practices</h2>

<div class="card">

<ul>
<li>Save generated outputs using explicit filenames</li>
<li>Always inspect stderr when execution fails</li>
<li>Prefer CSV exports for structured datasets</li>
<li>Use matplotlib.savefig() for charts</li>
<li>Use timeout carefully for large computations</li>
<li>Keep execution logic deterministic</li>
</ul>

</div>

<h2 class="section-title">Platform Roadmap</h2>

<div class="card">

<ul>
<li>Execution sessions</li>
<li>Persistent kernels</li>
<li>WebSocket streaming</li>
<li>Interactive playground</li>
<li>Async execution queues</li>
<li>Notebook-style workflows</li>
<li>Agent SDKs</li>
<li>Execution metadata tracking</li>
<li>Package installation sandbox</li>
<li>Multi-runtime execution</li>
</ul>

</div>

<div class="card">

<h2>Health Check</h2>

<pre>GET /</pre>

<p>
Returns API documentation and platform information.
</p>

</div>

</body>
</html>
"""
