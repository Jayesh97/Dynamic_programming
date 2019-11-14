a=$1
b=$2
n=$3
m=$4
   
for (( i=0; i<n; i++ )) 
do
    fn=$((a + b)) 
    a=$b 
    b=$fn 
done
echo $fn
# End of for loop 