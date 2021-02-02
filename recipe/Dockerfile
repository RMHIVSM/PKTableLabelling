FROM python:3.8
#.7-slim-buster
# Set our working directory
WORKDIR ./

ADD
label-json.py .
#prodigy-1.10.5-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl .

# Copy files
COPY . ./

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install ./prodigy-1.10.5-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl
RUN pip install .

# main.py will run when container starts up on the device
#CMD ["sh","launch_recipe.sh"]
CMD ["python","./label-json.py"]
