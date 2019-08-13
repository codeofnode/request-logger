killall python
rm -f python.log
python python-server.py &
#FLASK_APP=flask-server.py python -m flask run &
sleep 1
tail -f python.log &
#curl -H 'X-App-Tid:blah blah' -s --output /dev/null http://localhost:5000
curl -H 'X-App-Tid:blah blah' -s --output /dev/null http://localhost:8080
wait
