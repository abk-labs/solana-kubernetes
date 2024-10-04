.PHONY: lint test vet setup

test:
	go test ./pkg/...

setup: 
	./setup

lint:
	golangci-lint run ./pkg/...

vet:
	go vet ./pkg/...
