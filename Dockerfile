FROM continuumio/anaconda3:4.4.0
COPY scripts /usr/local/rf_project
EXPOSE 5000
WORKDIR /usr/local/rf_project
RUN pip install flask && flasgger && pip install -r requirements.txt
CMD python app.py