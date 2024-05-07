ARG BUILD_FROM
FROM $BUILD_FROM

# Working directory
WORKDIR /data

# Allow PIP to install packages outside venv
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Copy data for add-on
COPY run.sh /
COPY renogybtaddon.py /

# Add Cyrils Renogy BT script
ARG CYRILS_VERSION=3.2
ADD https://github.com/cyrils/renogy-bt/archive/refs/tags/v${CYRILS_VERSION}.tar.gz /cyrils_renogy-bt.tar.gz
RUN tar -xvzf /cyrils_renogy-bt.tar.gz -C /
RUN mv /renogy-bt-${CYRILS_VERSION} /renogy-bt
RUN rm /cyrils_renogy-bt.tar.gz

RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3 \
        python3-dev \
        python3-pip \
        libdbus-glib-1-dev \
        libgirepository1.0-dev \
        libcairo2 \
        libcairo2-dev \
        python3-dbus \
        libdbus-1-3 \
        libdbus-1-dev \
        libglib2.0-dev \
    \
    && pip3 install --no-cache-dir -r /renogy-bt/requirements.txt \
    && apt-get purge -y --auto-remove \
        build-essential \
        python3-dev 

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]