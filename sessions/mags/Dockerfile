# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:20.04

# Set the environment to non-interactive to avoid user interaction during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    wget \
    git \
    build-essential \
    python3 \
    python3-pip \
    openjdk-8-jdk \
    zlib1g-dev \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    cmake

# Checkm
RUN pip3 install checkm-genome
# Checkm2
RUN pip install CheckM2
# newick


# Install tools
RUN apt-get update -y && apt-get install -y bwa prodigal samtools bcftools

## Install Metabat2
########
RUN apt-get update  && \
    apt-get install -y libgomp1 libhts3 autoconf libboost-all-dev curl libhts-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

ENV METABAT2_VERSION=2.17
ENV METABAT2_HASH=1087553d61dcb0b6a18897b1e8d908e57f7e5e34
ADD https://bitbucket.org/berkeleylab/metabat/get/${METABAT2_HASH}.tar.gz /usr/local/metabat-binary.tar.gz
RUN mkdir -p /usr/local/metabat \
    && tar xvf /usr/local/metabat-binary.tar.gz --strip-components=1 -C /usr/local/metabat \
    && chmod 777 -R /usr/local/metabat \
    && rm /usr/local/metabat-binary.tar.gz \
    && cd /usr/local/metabat \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j8 \
    && make install \
    && cd .. \
    && rm -rf build

## Install htslib
########
ENV HTSLIB_VERSION=1.20
ADD https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 /usr/local/htslib.tar.bz2
RUN tar xvjf /usr/local/htslib.tar.bz2 -C /usr/local/ \
     && chmod 777 -R /usr/local/htslib-${HTSLIB_VERSION} \
     && cd /usr/local/htslib-${HTSLIB_VERSION} \
     && ./configure \
     && make \
     && make install \
     && rm /usr/local/htslib.tar.bz2

# Custom scripts
COPY complenetess_vs_contamination.py /usr/local/bin/
RUN chmod +x /usr/local/bin/complenetess_vs_contamination.py