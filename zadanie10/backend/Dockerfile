FROM golang:latest
ENV GOPATH /go

WORKDIR /app

COPY . .

RUN go build -o main .

EXPOSE 8080
CMD ["./main"]
