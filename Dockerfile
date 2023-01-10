FROM ubuntu

COPY . /home/my_blog
WORKDIR /home/my_blog

ENV VIRTUAL_ENV=/opt/venv
RUN apt-get update && apt-get install -y python3 && apt install -y python3.10-venv && python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt

RUN pylint --errors-only app.py 
RUN bandit --exit-zero  app.py  


CMD ["python", "app.py"]
