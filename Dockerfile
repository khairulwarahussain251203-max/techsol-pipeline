FROM openjdk:27-ea-oraclelinux10
WORKDIR /app
COPY hello.java .
RUN javac hello.java
CMD ["java", "hello"]
