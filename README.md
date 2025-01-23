# Rag-v1

This is a project i made while learning how to make a RAG system.

The you access the playlist i watched from [here](https://www.youtube.com/watch?v=Vv6e2Rb1Q6w&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj)

## Requirements
- Python 3.8 or later

### Python installation using Miniconda

1 - Download and install miniconda from [this](https://docs.anaconda.com/miniconda/install/) page.

2 - Create a new environment using the following command:

``` bash
$ conda create -n mini-rag-app
```

3 - Activiate the environment using the following command :

``` bash
$ conda activate mini-rag-app
```

### To install the required packages simply run this command:
```bash
$ pip install -r requirments.txt
```

### Setup the environment variables
```bash
$ cp .env.example .env
```
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

### Run the fastapi server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## (Optional)

### Setup your command line for better readability using this command:
``` bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
