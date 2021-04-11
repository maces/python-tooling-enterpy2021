FROM python:3.9.4

RUN mkdir /python_tooling_enterpy_2021


COPY build/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


# RUN pip3 install micropipenv[toml]
# COPY pyproject.toml /pyproject.toml
# COPY poetry.lock /poetry.lock
# RUN micropipenv install

WORKDIR /python_tooling_enterpy_2021
# EXPOSE <port>
# COPY .env /python_tooling_enterpy_2021/.env
COPY python_tooling_enterpy_2021 /python_tooling_enterpy_2021
