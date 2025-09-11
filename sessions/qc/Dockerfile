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

# Download SILVA-SSU MAPseq files
RUN mkdir /SILVA-SSU && \
    cd  /SILVA-SSU && \
    wget https://ftp.ebi.ac.uk/pub/databases/metagenomics/pipelines/tool-dbs/silva-ssu/silva-ssu_138.1.tar.gz && \
    tar -xzvf silva-ssu_138.1.tar.gz && \
    rm silva-ssu_138.1.tar.gz

# Install seqkit
RUN wget https://github.com/shenwei356/seqkit/releases/download/v2.10.1/seqkit_linux_amd64.tar.gz && \
    tar -xzvf seqkit_linux_amd64.tar.gz && \
    mv seqkit /usr/local/bin && \
    rm seqkit_linux_amd64.tar.gz

# Install MAPseq
RUN wget https://github.com/meringlab/MAPseq/releases/download/v2.1.1b/mapseq-2.1.1b.tar.gz && \
    tar -xzvf mapseq-2.1.1b.tar.gz && \
    mv build/ MAPseq && \
    rm mapseq-2.1.1b.tar.gz
ENV PATH="$PATH:/MAPseq/bin"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8