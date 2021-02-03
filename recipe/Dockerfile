FROM python:3.8.7-slim-buster
# Set our working directory
WORKDIR ./

#ADD
#label-json.py .
#prodigy-1.10.5-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl .

# Copy files
COPY ./ ./my_dir

# pip install python deps
RUN pip install .
RUN pip install ./recipe/prodigy-1.10.5-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl


# main.py will run when container starts up on the device
CMD ["sh","./recipe/launch_recipe.sh"]
