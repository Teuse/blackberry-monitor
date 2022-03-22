FROM i386/ubuntu:bionic

RUN apt-get update && \
	apt-get install -y build-essential git cmake autoconf libtool pkg-config libboost-all-dev

ENV TZ=Europe/Berlin

WORKDIR /repo

RUN --mount=type=bind,target=/repo,rw \
	cmake . && make

CMD ["./air_quality"]
