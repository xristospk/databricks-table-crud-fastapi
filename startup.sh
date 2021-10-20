apt-get update 
apt-get install libsasl2-dev
gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app --bind=0.0.0.0:8000