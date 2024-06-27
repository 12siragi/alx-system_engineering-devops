# Web Stack Debugging #4

This project involves debugging and optimizing a web server setup featuring Nginx to handle high traffic. The task requires the use of ApacheBench for benchmarking and Puppet for automating the configuration changes.

## Requirements

- **Environment**: Ubuntu 14.04 LTS
- **Puppet Version**: 3.4
- **puppet-lint Version**: 2.1.1

## Setup

1. Install Ruby:
    ```sh
    sudo apt-get install -y ruby
    ```

2. Install puppet-lint:
    ```sh
    gem install puppet-lint -v 2.1.1
    ```

## Files

- `0-the_sky_is_the_limit_not.pp`: Puppet manifest to fix the web server configuration.
- `benchmark_results.txt`: Initial and final benchmark results after applying the Puppet manifest.

## Usage

1. Run the initial benchmark:
    ```sh
    ab -c 100 -n 2000 http://localhost/
    ```

2. Apply the Puppet manifest:
    ```sh
    sudo puppet apply 0-the_sky_is_the_limit_not.pp
    ```

3. Run the benchmark again to verify the improvements:
    ```sh
    ab -c 100 -n 2000 http://localhost/
    ```

## Puppet Manifest Explanation

The Puppet manifest `0-the_sky_is_the_limit_not.pp` is designed to optimize the Nginx server configuration to handle higher traffic without failing requests. The specific changes are detailed in the comments within the manifest file.

## Initial Benchmark Results


