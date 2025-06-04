print("Hello, World!")# Re-import necessary modules after code state reset
import zipfile
from pathlib import Path

# Define file contents for multiple lessons
lessons = {
    "lesson1.html": """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Lesson 1: Declare Yourself</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #f3e5f5;
      font-family: 'Courier New', monospace;
      padding: 20px;
    }
    #lesson {
      background-color: #2a1a40;
      border-left: 5px solid #9b59b6;
      padding: 15px;
      margin-bottom: 20px;
      border-radius: 8px;
    }
    textarea, button, #output {
      width: 100%;
      margin-top: 10px;
      font-family: 'Courier New', monospace;
    }
    textarea {
      height: 100px;
      background: #111;
      color: #fff;
      border-radius: 5px;
      padding: 10px;
    }
    button {
      background-color: #8e44ad;
      color: white;
      padding: 10px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
    #output {
      background: #222;
      color: #a8e6a1;
      padding: 10px;
      border-left: 4px solid #27ae60;
      border-radius: 5px;
    }
  </style>
</head>
<body>
<div id="lesson">
  <h2>Lesson 1: Declare Yourself</h2>
  <p>Declare a variable named <code>pet</code> and assign it a string value. Then use <code>console.log(pet);</code>.</p>
</div>
<textarea id="codeInput">let pet = "fox";\nconsole.log(pet);</textarea>
<button onclick="runCode()">Run Code</button>
<div id="output"></div>
<script>
function runCode() {
  const code = document.getElementById('codeInput').value;
  const output = document.getElementById('output');
  const logs = [];
  const console = { log: msg => logs.push(String(msg)) };
  try {
    const fn = new Function('console', code);
    fn(console);
    output.textContent = logs.length ? logs.join('\\n') : "No output.";
  } catch (err) {
    output.textContent = "Error: " + err.message;
  }
}
</script>
</body>
</html>
""",
    "index.html": """<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Code Lessons</title></head><body><h1>JavaScript Lessons</h1><ul><li><a href='lesson1.html'>Lesson 1: Declare Yourself</a></li></ul></body></html>"""
}

# Path to the zip file
zip_path = "/mnt/data/javascript_lessons.zip"

# Create the zip file
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for filename, content in lessons.items():
        # Write each file into the zip
        filepath = Path("/mnt/data") / filename
        with open(filepath, "w") as f:
            f.write(content)
        zipf.write(filepath, arcname=filename)

zip_path