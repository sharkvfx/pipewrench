
# create test directories based on 
# project, episode, sequence, shot, version
#./project/episode/sequence/shot/Comp/publish/version

PROJECT=`cat /dev/random | env LC_CTYPE=C tr -dc 'A-Z'|head -c 3`
EPISODE=`cat /dev/random | env LC_CTYPE=C tr -dc '0-9A-Z'|head -c 3`
SEQUENCE=`cat /dev/random | env LC_CTYPE=C tr -dc '0-9'|head -c 3`
VERSION=`cat /dev/random | env LC_CTYPE=C tr -dc '0-9'|head -c 2;echo 0`

DIR="./test/$PROJECT/$EPISODE/$SEQUENCE/$SHOT/Comp/publish/$PROJECT-$EPISODE-$SEQUENCE-$SHOT_Comp_$VERSION/"

echo "making $DIR"
mkdir -p $DIR
