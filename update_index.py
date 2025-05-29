import os

def get_strm_files():
    return [f for f in os.listdir('.') if f.endswith('.strm')]

def make_link(filename):
    from urllib.parse import quote
    return f'<li><a href="{quote(filename)}">{filename}</a></li>'

def update_index():
    files = get_strm_files()
    links = "\n".join([make_link(f) for f in sorted(files)])
    html = f"""<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
</head>
<body>
<hr>
<ul>
{links}
</ul>
<hr>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    update_index()
