
FROM openjdk:27-ea-oraclelinux10
WORKDIR /app
COPY hello.java .
RUN javac hello.java
# Add this line to open the port
EXPOSE 8080
CMD ["java", "hello"]
