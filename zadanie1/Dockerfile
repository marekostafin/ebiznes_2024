FROM ubuntu:22.04

WORKDIR /tmp

#Instalowanie narzędzi pomocniczych
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y wget
RUN apt-get install -y zlib1g-dev

# Instalowanie pythona 3.8
RUN wget https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tgz
RUN tar xzf Python-3.8.18.tgz
RUN /tmp/Python-3.8.18/configure --enable-optimizations
RUN make install

# Usuwanie plików instalacyjnych
RUN cd / && \
    rm -rf /tmp/Python-3.8.18*

# Instalowanie OpenJDK-8
RUN apt-get install -y openjdk-8-jdk

# # Instalowanie Kotlina
RUN apt-get install -y kotlin

# Instalowanie Gradle'a
RUN apt-get install -y unzip
RUN wget https://services.gradle.org/distributions/gradle-8.6-bin.zip
RUN unzip gradle-8.6-bin.zip
RUN mv gradle-8.6 /opt/gradle/
ENV GRADLE_HOME=/opt/gradle
ENV PATH=$PATH:$GRADLE_HOME/bin

RUN useradd -ms /bin/bash mostafin
RUN adduser mostafin sudo

VOLUME /home/mostafin

WORKDIR /app

# Tworzenie projektu z Gradle'm
COPY build.gradle /app/
RUN gradle build

# Dodawanie programu Hello World
COPY HelloWorld.java /app/
RUN javac HelloWorld.java

CMD [ "java", "HelloWorld"]