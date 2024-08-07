ARG BUILD_FROM
FROM $BUILD_FROM

# Working directory
WORKDIR /app

# Allow PIP to install packages outside venv
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    python3-dev \
    py-pip \
    bluez 

# Copy files for add-on
COPY run.sh .

# Add Cyrils Renogy BT script
ADD https://github.com/IAmTheMitchell/renogy-bt/archive/refs/heads/main.zip renogy-bt-main.zip
RUN unzip renogy-bt-main.zip -d .
RUN mv renogy-bt-main/* /app

RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt
RUN . venv/bin/activate

RUN chmod a+x run.sh

CMD [ "./run.sh" ]