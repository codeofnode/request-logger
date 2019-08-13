if [ ! -f python-server.py ]; then
  git clone https://gist.github.com/8e9757180506f25e46d9.git
  mv 8e9757180506f25e46d9/rest.py python-server.py
  rm -rf 8e9757180506f25e46d9
fi
