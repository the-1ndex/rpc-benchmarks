# Solana RPC Benchmarking suite

A small test suite to see how fast an RPC service is.

## How to run?
Install the locust library, run locust, and open http://localhost:8089
```sh
pip install locust
git clone repo
cd rpc-benchmark
# Use gma for benchmarking getMultipleAccounts and gpa for getProgramAccounts
locust --tags gpa
```

## Public RPC servers to test with

* https://demo.theindex.io
* https://ssc-dao.genesysgo.net
* https://solana-api.projectserum.com
* https://api.mainnet-beta.solana.com (This endpoint doesn't accept `getProgramAccounts` requests)

