FROM python
RUN pip install dash
RUN pip install pandas
ADD gapminder_unfiltered.py .
HEALTHCHECK --interval=1s CMD curl --fail http://localhost:8050/health || exit 1
ENTRYPOINT [ "python", "gapminder_unfiltered.py" ]
EXPOSE 8050
