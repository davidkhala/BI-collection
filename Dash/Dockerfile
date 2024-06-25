FROM python
RUN pip install dash
RUN pip install pandas
ADD app.py .
ENTRYPOINT [ "python", "app.py" ]
EXPOSE 8050
# TODO not accessible