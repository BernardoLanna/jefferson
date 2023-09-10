#!/bin/bash

read -p “Insira o link para o streamer: “ host

echo $host > /home/jefferson/Desktop/host.txt
mkdir /home/jefferson/script

cat > /home/jefferson/script/mplayer.sh <<EOF
