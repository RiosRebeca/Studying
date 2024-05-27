#!/bin/bash

if [ "$1" == "" ]
then
        echo "CHAVE DO VLAB3.1";
        echo "MODO DE USO: $0 ip_do_alvo";
        echo "Esse script é específico para esse vlab";
        echo "IP: 37.59.174.235 ";
else
        portas=("13" "37" "30000" "3000" "1337");
        for chave in "${portas[@]}"; do
            echo "Knocking port $chave";
            sudo hping3 -S -p "$chave"  -c 1 "$1" > /dev/null 2> /dev/null;
        done
        curl -v -o malwarename 37.59.174.235:1337 > /dev/null 2> /dev/null;
        if [ -f "malwarename" ]
        then
                cat malwarename;
        else
                echo "AAAAAHHHH QUE ÓDIOOOOOOO!!!! S/2  >O< T-T";
        fi

portas2=("2424" "2525")
for chave2 in "${portas2[@]}";
do
echo "Knocking port $chave2"
sudo hping3 -S -p "$chave2" -c 1 "$1" > /dev/null 2> /dev/null;
done
echo "Fim S2."
fi      
