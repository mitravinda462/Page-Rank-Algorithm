#!/bin/sh
CONVERGE=1
COUNT=0
rm v*

cat web-Google.txt | /home/mitravinda/Desktop/Mitra/BD/asst2/mapper.py | sort -k1,1 | reducer.py './v' > adjlist #has adjacency list


while [ "$CONVERGE" -ne 0 ]
do
	cat adjlist | mapper1.py './v' | sort -k1,1 | reducer1.py > v1
	CONVERGE=$(python3 check_conv.py >&1)
	COUNT=`expr $COUNT + 1`
	echo "iteration: $COUNT"
done
