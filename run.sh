# gunicorn
echo "gunicorn starting"
gunicorn -b 0.0.0.0:80 -w4 app.wsgi