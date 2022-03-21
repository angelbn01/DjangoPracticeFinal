FROM python
RUN mkdir /app
WORKDIR /app
ADD website/requirements.txt /app/
RUN pip install -r requirements.txt
ADD website /app/
RUN python manage.py collectstatic