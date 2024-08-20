FROM ubuntu:22.04

# Install Python3, pip3, java, blast+, bowtie2, multiqc
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    libfindbin-libs-perl \
    wget unzip \
    python3 python3-pip \
    default-jre \
    bowtie2 \
    libfontconfig1 libgl1 libx11-6 libx11-xcb1 libxcb-glx0 \
    ncbi-blast+ cmake && \
    pip3 install multiqc --no-cache-dir

# Install FastQC
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip &&\
    unzip fastqc_v0.12.1.zip && \
    rm fastqc_v0.12.1.zip
ENV PATH="$PATH:/FastQC"

# Install fastp
RUN wget http://opengene.org/fastp/fastp.0.23.4 && \
    mv fastp.0.23.4 fastp && \
    chmod a+x ./fastp && \
    mv fastp /usr/local/bin

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8