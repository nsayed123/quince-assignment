
FROM openjdk:17-jdk-slim AS build
WORKDIR /app
COPY . /app
RUN  cd complete && ./gradlew clean build


FROM amazoncorretto:17-alpine3.14
VOLUME /tmp
WORKDIR /app
ARG DEPENDENCY=/app/complete/build
COPY --from=build ${DEPENDENCY}/libs /app/
ENTRYPOINT ["java","-jar","/app/rest-service-0.0.1-SNAPSHOT.jar"]