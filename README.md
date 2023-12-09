# Hash Bruteforce Tool

## Overview

This Python script is a simple command-line tool designed for brute-forcing hashes. It supports the following hash algorithms: SHA-512, SHA-256, SHA-1, and MD5.

## Features

- Brute-forces hashed passwords using a dictionary attack.
- Supports SHA-512, SHA-256, SHA-1, and MD5 hash algorithms.
- Allows users to input a hash and an optional salt for the bruteforce process.
- Saves found passwords to a file (`passwords.txt`).

## How to Use

1. Run the script.
2. Enter the hash you want to crack when prompted.
3. Optionally, enter a salt.
4. Wait for the script to finish the bruteforce attempt.
5. If successful, the password is displayed, and the result is saved in `passwords.txt`.

## Usage

```bash
python bruteforce.py
