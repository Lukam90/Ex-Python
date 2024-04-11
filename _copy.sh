date=`date +"%H.%M"`
name="Python"

target="$HOME/Téléchargements/Copies/CP-$name-$date"

if [ ! -d $target ]; then
    cp -r . $target
fi

echo "Copie $name - $date"