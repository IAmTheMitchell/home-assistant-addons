ARG BUILD_FROM
FROM $BUILD_FROM

# Working directory
WORKDIR /app

# Allow PIP to install packages outside venv
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Copy data for add-on
COPY run.sh .
COPY renogybtaddon.py .

# Add Cyrils Renogy BT script
ADD https://github.com/cyrils/renogy-bt/archive/refs/heads/bleak.zip cyrils_renogy-bt.zip
RUN unzip cyrils_renogy-bt.zip -d .
RUN mv renogy-bt-bleak/renogybt /app/renogybt
RUN rm cyrils_renogy-bt.zip

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    python3-dev \
    py-pip

RUN python3 -m venv venv
RUN venv/bin/pip3 install -r renogy-bt-bleak/requirements.txt
RUN . venv/bin/activate

RUN rm -rf renogy-bt-bleak

RUN chmod a+x run.sh

CMD [ "./run.sh" ]