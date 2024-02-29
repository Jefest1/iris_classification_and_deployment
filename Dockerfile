FROM continuumio/anaconda3:4.4.0
COPY scripts /usr/local/rf_project
EXPOSE 5000
WORKDIR /usr/local/rf_project
RUN pip install flask && pip install flasgger && pip install -r requirements.txt && pip install joblib
CMD python app.py