name: Auto-update index.html

on:
  push:
    paths:
      - '*.strm'
      - 'update_index.py'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Regenerate index.html
        run: python update_index.py

      - name: Commit and push index.html if changed
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add index.html
          git diff --cached --quiet || git commit -m "Auto-update index.html"
          git push
