# LLM Biographer

Automatically writes you a webpage describing your many accomplishments,
between 10%-90% of which are actually true.

## Why?

https://nicholas.carlini.com/writing/2025/llms-write-my-bio.html

## Demo?

https://nicholas.carlini.com/writing/2025/llm-bio/2024-12-25-o1-mini.html

## Usage

Edit `config.py` and pick the model you want, and edit your name.

```bash
python3 write_bio.py > bio.html
# Optionally, edit eratum.json to comment on any flaws
python3 add_caution.py > output.html
```

## License

GPL v3