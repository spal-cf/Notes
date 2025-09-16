### Simple SSL web server
openssl s_server -accept 443 -cert cert.pem -key key.pem -WWW

  ### ngrok

python3 -m http.server 8000
ngrok http --domain=domain.ngrok.app 8000
https://domain.ngrok.app
