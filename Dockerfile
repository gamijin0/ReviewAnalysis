FROM python:3-onbuild
CMD ["pip","install","-r","./requirements.txt"]
CMD ["python","./run.py"]