import subprocess

def run_python(file_name):
    result = subprocess.run(
        ["python", file_name],
        capture_output=True,
        text=True,
        timeout = 30,
    )
    return result.stdout, result.stderr
