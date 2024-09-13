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

RUN pip3 install checkm-genome
RUN pip3 install checkm2
RUN pip3 install newick
RUN pip3 install figtree

## Install Metabat
########
ENV METABAT2_VERSION=2.17
ENV METABAT2_HASH=1087553d61dcb0b6a18897b1e8d908e57f7e5e34
ADD https://bitbucket.org/berkeleylab/metabat/get/${METABAT2_HASH}.tar.gz /usr/local/metabat-binary.tar.gz
RUN mkdir -p /usr/local/metabat \
    && tar xvf /usr/local/metabat-binary.tar.gz --strip-components=1 -C /usr/local/metabat \
    && chmod 777 -R /usr/local/metabat \
    #&& /usr/local/metabat/contigOverlaps
    && ln -s /usr/local/metabat/metabat* /usr/local/bin/ \
    && ln -s /usr/local/metabat/runMetaBat.sh /usr/local/bin/ \
    && ln -s /usr/local/metabat/*.pl /usr/local/bin/ \
    && ln -s /usr/local/metabat/jgi_summarize_bam_contig_depths /usr/local/bin/ \
    && rm /usr/local/metabat-binary.tar.gz

RUN apt update && apt install -y bwa prodigal samtools bcftools

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

COPY complenetess_vs_contamination.py /usr/local/bin/
RUN chmod +x /usr/local/bin/complenetess_vs_contamination.py