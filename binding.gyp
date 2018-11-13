{
  "targets": [
    {
      "target_name": "modsecurity",
      "sources": [ "modsecurity_wrap.cxx" ],
      "include_dirs": ['usr/local/modsecurity/include/modsecurity',],
      "libraries": ['/usr/local/modsecurity/lib/libmodsecurity.a',
      '/usr/local/modsecurity/lib/libmodsecurity.dylib',
      '/usr/local/modsecurity/lib/libmodsecurity.la',
      '/usr/local/modsecurity/lib/libmodsecurity.3.dylib'
      '/usr/lib/libxml2.dylib',
      '/usr/lib/libcurl.dylib',
      '/usr/local/lib/libpcre.dylib',
      '/usr/local/lib/libyajl.dylib',
      '/usr/local/lib/libGeoIP.dylib',
      '/usr/local/lib/liblmdb.dylib'],
      "cflags" : [ "-std=c++11" ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ]
    }
  ]
}
