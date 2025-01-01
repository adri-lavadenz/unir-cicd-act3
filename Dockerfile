FROM python:3.14.0a3-slim

RUN mkdir -p /opt/calc

WORKDIR /opt/calc

COPY .coveragerc .pylintrc pyproject.toml pytest.ini requires ./
COPY app ./app
COPY test ./test
COPY web ./web
RUN pip install -r requires
