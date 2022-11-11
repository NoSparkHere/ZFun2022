FROM golang:1.19-alpine AS builder

WORKDIR /usr/src/app
COPY . .
RUN go build -ldflags="-s -w" -v -o /usr/local/bin/app

FROM alpine AS runner

COPY --from=builder /usr/local/bin/app /
CMD ["/app"]
