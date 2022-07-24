FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /symspellpy
WORKDIR /symspellpy
RUN python3 -m pip install . && chmod +x fuzz/fuzz_spellcheck.py