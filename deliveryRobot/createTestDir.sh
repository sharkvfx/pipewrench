
# create test directories based on 
# project, episode, sequence, shot, version
#./project/episode/sequence/shot/Comp/publish/version

PROJECT=`cat /dev/urandom | env LC_CTYPE=C tr -dc 'A-Z'|head -c 3`
EPISODE=`cat /dev/urandom | env LC_CTYPE=C tr -dc '0-9A-Z'|head -c 3`
SEQUENCE=`cat /dev/urandom | env LC_CTYPE=C tr -dc '0-9'|head -c 3`
VERSION=`echo -n 0;cat /dev/urandom | env LC_CTYPE=C tr -dc '0-9'|head -c 1`
SHOT=`cat /dev/urandom | env LC_CTYPE=C tr -dc '0-9'|head -c 3;echo 0`
SHOTLONG=$EPISODE-$SEQUENCE-$SHOT

DIR="./test/$PROJECT/$EPISODE/$SEQUENCE/$SHOTLONG/Comp/publish/renders/$SHOTLONG_Comp_$VERSION/"

echo "making $DIR"
mkdir -p $DIR
