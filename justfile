install:
    @poetry install
    @npm install

tw:
    @npx tailwindcss -i ./src/briancohan/static/css/tw-base.css -o ./src/briancohan/static/css/style.css --watch --minify

dev:
    poetry run flask --app briancohan run --host 0.0.0.0
