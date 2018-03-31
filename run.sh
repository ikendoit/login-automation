#!/bin/bash

if [ ! -e AutoData.txt ]; then 
    echo "d2l user pass
mylangara user pass
******************

films: super natural season 12 http://www.phimmoi.net/phim/sieu-nhien-phan-12-4277/

films: flash season 3 http://www.phimmoi.net/phim/nguoi-hung-tia-chop-phan-3-4269/

films: boruto http://www.phimmoi.net/phim/boruto-naruto-next-generations-4997/

films: attack on the titan season 2 http://www.phimmoi.net/phim/dai-chien-titan-phan-2-5119/

films: one piece http://www.phimmoi.net/phim/dao-hai-tac-i4-665/" > ./AutoData.txt
fi

dependi=(selenium chromedriver requests bs4)

for f in ${dependi[@]}; do 
    pip show $f > /dev/null
    if [ $? != "0" ]; then 
        sudo pip install $f
    fi
done

which python3 > /dev/null

if [ $? == "0" ]; then 
    if [ `grep "d2l " AutoData.txt | wc -m` -lt 18 -o `grep "mylangara " AutoData.txt | wc -m` -lt 25 > /dev/null ]; then 
        read -p "enter your username for d2l: " userd2l
        read -p "enter your password for d2l: " -s passd2l
        echo 
        read -p "enter your username for mylangara: " usermyl
        read -p "enter your username for mylangara: " -s passmyl
        sed -i "s/d2l user pass/d2l $userd2l $passd2l/g" AutoData.txt
        sed -i "s/mylangara user pass/mylangara $usermyl $passmyl/g" AutoData.txt
    fi
else 
    sudo apt-get install python3
	sudo apt-get install python3-pip
fi

python3 autoweb.py
