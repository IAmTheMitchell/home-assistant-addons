ARG BUILD_FROM
FROM $BUILD_FROM

# Working directory
WORKDIR /app

# Allow PIP to install packages outside venv
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Copy files for add-on
COPY . .

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    python3-dev \
    py-pip 

RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt
RUN . venv/bin/activate

RUN chmod a+x run.sh

CMD [ "./run.sh" ]