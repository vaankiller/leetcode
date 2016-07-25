#!/bin/sh

COL=$(cat file.txt | head -n 1 | wc -w)
LINE=$(cat file.txt | wc -l)

#echo $COL
#echo $LINE
cat file.txt | awk -v line=$LINE \
	'BEGIN{ for(i=1;i<=2;i++) 
			{
				printf $i; 
			}
		}'


		awk '  
		{

			for(i=1;i<=NF;i++){

				if(NR==1){

					s[i]=$i;  
				}else{

				s[i]=s[i]" "$i;  
			}  
		}  
	}    
	END{

	for(i=1;s[i]!="";i++)  
		print s[i];  
	}  
	' file.txt'
