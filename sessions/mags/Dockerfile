# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:20.04

# ------------- Docker contains tools for MAGs practical:
# - checkm_v1.2.3
# - prodigal
# - samtools
# - bcftools
# - BWA
# - Metabat2
# - htslib
# - newick utils
# custom scripts:
# - complenetess_vs_contamination.py
# ---------------------------------------------------------

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
COPY completeness_vs_contamination.py /usr/local/bin/
RUN chmod +x /usr/local/bin/completeness_vs_contamination.py

# newick
RUN apt-get update  && \
    apt-get install -y flex bison
RUN git clone https://github.com/tjunier/newick_utils.git
RUN cd newick_utils \
    && autoreconf -fi \
    && ./configure \
    && make \
    && make install \
    && export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib \
    && echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >> /etc/bash.bashrc
    #&& sudo ldconfig

# checkm1 requirements
RUN pip3 install pysam
## Install hmmer
########
ADD http://eddylab.org/software/hmmer/hmmer-3.2.tar.gz /usr/local/hmmer-3.2.tar.gz
RUN tar xvf /usr/local/hmmer-3.2.tar.gz -C /usr/local/ \
    && chmod 777 -R /usr/local/hmmer-3.2 \
    && cd /usr/local/hmmer-3.2 \
    && ./configure \
    && make \
    && make check \
    && make install \
    && cd easel \
    && make install \
    && rm /usr/local/hmmer-3.2.tar.gz

## Install PPlacer
########
RUN apt-get update; apt-get install -y unzip
ADD https://github.com/matsen/pplacer/releases/download/v1.1.alpha19/pplacer-linux-v1.1.alpha19.zip /usr/local/pplacer-linux-v1.1.alpha19.zip
RUN unzip /usr/local/pplacer-linux-v1.1.alpha19.zip -d /usr/local/ \
    && chmod -R 777 /usr/local/pplacer-Linux-v1.1.alpha19 \
    && ln -s /usr/local/pplacer-Linux-v1.1.alpha19/guppy /usr/local/bin/ \
    && ln -s /usr/local/pplacer-Linux-v1.1.alpha19/pplacer /usr/local/bin/ \
    && ln -s /usr/local/pplacer-Linux-v1.1.alpha19/rppr /usr/local/bin/ \
    && rm /usr/local/pplacer-linux-v1.1.alpha19.zip
