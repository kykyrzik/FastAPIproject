FROM python:3.10.12

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY certs/ certs/

RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./
COPY alembic.ini alembic.ini
RUN poetry install

WORKDIR opt/project

EXPOSE 8000

COPY . .

WORKDIR src/

CMD ["python", "-m src"]