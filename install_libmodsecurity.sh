#!/bin/sh
brew update
brew install ruby autoconf automake libtool pkg-config openssl lmdb ssdeep yajl geoip pcre
curl -R -O http://www.lua.org/ftp/lua-5.3.0.tar.gz
tar zxf lua-5.3.0.tar.gz
cd lua-5.3.0
make macosx test MYCFLAGS="-arch x86_64 -arch i386"
cd ../ && rm -rf lua-5.3.0
git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity
cd ModSecurity
git checkout v3/master
git submodule init
git submodule update
./configure
sudo make install
cd ../

