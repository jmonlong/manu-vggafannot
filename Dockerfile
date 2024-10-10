from mambaorg/micromamba

WORKDIR /build

COPY build/environment.yml .

RUN micromamba env create --file environment.yml

# Can't activate the environment without sourcing shell hooks, but it wouldn't
# apply inside the container if activated here anyway.
#RUN micromamba activate manubot
