from mambaorg/micromamba

WORKDIR /build

COPY build/environment.yml .

RUN micromamba env create --file environment.yml

RUN micromamba activate manubot
