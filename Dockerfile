FROM golang:1.23 as builder
LABEL maintainer="schizo99@gmail.com"

# Create guestuser.
RUN adduser --disabled-password --gecos '' guest


ENV GO111MODULE=on

COPY . /app

WORKDIR /app

RUN go mod download

# Install the package
# RUN go install -v ./...
RUN CGO_ENABLED=0 GOOS=linux go build -mod=readonly -v -o server

FROM alpine

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /app/server /server
EXPOSE 8080

USER guest

# Run the executable
CMD ["/server"]
