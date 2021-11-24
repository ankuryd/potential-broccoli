start=`date +%s`

if [ $# -eq 0 ]
  then
    echo "No arguments passed. Please pass pdf file name as argument."
fi

[ ! -d ./env ] && echo -e "Environment Check: Failure\nSetting up env" && ( ( virtualenv env && echo "Virtual env set up: Success" ) || ( echo "Please install virtualenv" && exit ) )
echo "Environment Check: Success"

echo "Sourcing virtual environment"
source env/bin/activate
( [ -f ./requirements.txt ] && echo "Installing required modules" && pip install -r requirements.txt > /dev/null ) || ( echo "File requirements.txt not found" && exit )

echo "Running PDF cleaning script" && python script.py $1 || exit
echo "Your pdf is now cleaned!"

end=`date +%s`

runtime=$((end-start))

echo "Runtime: $runtime seconds"
