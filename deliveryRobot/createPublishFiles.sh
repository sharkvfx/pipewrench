if [ $# -ne 3 ]
then
    echo "Usage: `basename $0` path startframe endframe"
    exit 
fi


PATH=$1
START=$2
END=$3
padtowidth=3
echo creating files in $PATH

for i in $(eval echo {$START..$END})
do num=`printf "%0*d\n" $padtowidth $i`
echo $PATH/testfile.$num.jpg
/usr/bin/touch $PATH/testfile.$num.jpg
done

