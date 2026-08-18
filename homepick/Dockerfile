# 1. Build Stage
FROM gradle:8.5-jdk21 AS builder
WORKDIR /app
COPY gradle gradle
COPY build.gradle settings.gradle gradlew ./
COPY src src
RUN chmod +x ./gradlew
RUN ./gradlew bootJar -x test

# 2. Run Stage
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]