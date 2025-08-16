MODDIR=$(python read-private-paths.py factp moddir)
rm -dr $MODDIR
mkdir -p $MODDIR/locale
python ./convert-to-ucsur.py
cp ./locale/cs/info.json ./ucsur-converted/cs/
cp -r ./ucsur-converted/* $MODDIR/locale
cp -r ./info.json ./data.lua ./fonts $MODDIR 
