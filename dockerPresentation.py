import streamlit as st

dockerImage = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-world.net%2Fwp-content%2Fuploads%2F2021%2F02%2FDocker-Symbol.png&f=1&nofb=1&ipt=5a14afd1e119e1ac15314fcdfdbb1773fa696a5236965cb353f443f7e97f5c97&ipo=images"

st.set_page_config(
    page_title='Docker Presentation',
    layout='wide',
    page_icon=dockerImage
)

st.caption('Team Marquet')
st.image(dockerImage, width=400)

st.title('Docker')
st.caption('What is it? What does it do? How does it work?')

# Yes, you can just put a string here and streamlit recognizes it as markdown. It's that easy.
"""
### Docker is *not* a virtual machine.
It's also not quite emulation software. It's kind of it's own niche which it fills nicely.
Which is why it's used by over 20 million developers in more than 7 million applications.

You can think of it as a lightweight virtual machine for a specific process.

The point of it is to solve the "well it works on *my* machine" problem.
"""

with st.expander('Preparation'):
    """
    # Installation
    You've all installed software before, you can figure it out.
    Just follow the instalation instructions for your platform.

    - [Windows](https://docs.docker.com/desktop/install/windows-install/#install-docker-desktop-on-windows)
    - [Mac](https://docs.docker.com/desktop/install/mac-install/#install-and-run-docker-desktop-on-mac)
    - [Ubuntu](https://docs.docker.com/desktop/install/ubuntu/)
    - [Debian](https://docs.docker.com/desktop/install/debian/)
    - [Fedora](https://docs.docker.com/desktop/install/fedora/)

    ### Other
    General instructions and supported platforms [here](https://docs.docker.com/engine/install/)

    # Setup
    This will install the all-spark-notebook for our presentation in class next week. You'll have to
    install it if you want to follow along. It'll take about 2 GB on your computer.

    ### Desktop
    If you're using docker desktop, open it and search for `jupyter/all-spark-notebook`. Then click
    on the only result and click "pull".

    ### CLI
    If you're using the command line (if you're using Windows, make sure docker is added to PATH),
    just run
    ```bash
    docker pull jupyter/all-spark-notebook
    ```
    We'll get to more details next week.
    """

with st.expander('Running the all-spark-notebook container'):
    """
    0. Pre-steps:
    If you're using Windows, don't forget to add the executable to PATH.

    If you're on linux, don't forget to start the Docker deamon using:
    ```bash
    sudo systemctl start docker
    ```
    1. Create a docker network
    We're showing you how to do this for tutorial purpouses only. A docker network
    is typically for connecting multiple containers together, or for connecting containers
    to non-docker workloads.
    ```bash
    docker network create n451
    ```
    2. Git clone `byuibigdata/docker_guide`

    ```bash
    git clone https://github.com/byuibigdata/docker_guide.git
    cd docker_guide
    ```

    3. Now we'll create the docker container. In order to create it we will run the following
    terminal code:

    Mac/Linux:
    ```bash
    docker run -it --name spark \\
    -p 8888:8888 -p 4040:4040 -p 4041:4041 \\
    -v ./data:/home/jovyan/data \\
    -v ./scripts:/home/jovyan/scripts \\
    -v ./scratch:/home/jovyan/scratch \\
    --network n451 \\
    jupyter/all-spark-notebook
    ```
    Windows:
    ```bash
    docker run -it --name spark^
    -p 8888:8888 -p 4040:4040 -p 4041:4041 ^
    -v .\\data:/home/jovyan/data ^
    -v .\\scripts:/home/jovyan/scripts ^
    -v .\\scratch:/home/jovyan/scratch ^
    --network n451 ^
    jupyter/all-spark-notebook
    ```
    ##### **Now lets go through step by step and see what that command is doing:**

    This tells docker to run the container (specified later), name it "spark", and open
    an interactive terminal inside the container.
    ```bash
    docker run -it --name spark \\
    ```
    This tells docker to bind the specified ports inside the container to the local machine.
    So if you do something inside the container on these ports, it will effect your local machine
    as well.
    ```bash
    -p 8888:8888 -p 4040:4040 -p 4041:4041 \\
    ```
    Each of these tells docker "take this file, and make it available inside the
    container at the specified path". This works just like the VOLUME command inside
    a Dockerfile, except this way we don't want to have to edit the Dockerfile directly.
    ```bash
    -v ./data:/home/jovyan/data \\
    -v ./scripts:/home/jovyan/scripts \\
    -v ./scratch:/home/jovyan/scratch \\
    ```
    This connects the image to the docker network we just created in step 1
    ```bash
    --network n451 \\
    ```
    This is the name of the notebook we want to run
    ```bash
    jupyter/all-spark-notebook
    ```

    After you run that command, you should see a bunch of output of Docker setting the container up.

    4. Now we have it running! Everything is all set up for us in a Jupyter server running on port 8888.
    We can now test it in 2 ways:

    In your browser, go to the second URL given in the output. It should look something like `http://127.0.0.1:8888/lab?token=...`
    You can then upload some PySpark code or start a new notebook by clicking on `Python 3 (ipykernel)`.

    Or, if you prefer VSCode (or it's open source cousin VSCodium) and you have the Jupyter Notebook extension,
    you can open a new Jupyter notebook, click on the current kernel (or "select kernel") in the top right,
    click "Select Another Kernel...", click "Existing Jupyter Server...", and copy and paste the
    `http://127.0.0.1:8888/lab?token=...` link mentioned above. This connects that notebook to the PySpark
    Jupyter server running in our Docker container.

    Whichever method you choose, try pasting this code in a notebook and running it.
    ```python
    from pyspark.sql import SparkSession

    spark = (SparkSession
        .builder
        .appName("PySpark Example")
        .config("spark.some.config.option", "some-value")
        .getOrCreate()
    )
    spark.version
    ```
    """

with st.expander('Purpose'):
    """
    The use of docker is that it allows you to set up an enviorment (*`container`*) you can run software
    in that is consistent across hardware. So you can send your friend a script you wrote, and you
    don't have to worry about it not running on their machine, because they don't have some package
    installed, or they run Windows instead of Linux, or anything like that.
    """

with st.expander('Containers and Images'):
    st.image('ContainerImage.png')
    """
    #### Images
    Images are like a variable definition. It describes how a container is made.

    #### Containers
    Containers are instantiations of images.
    """

# Cope has this section
with st.expander('Dockerfile'):
    """
    A Docker image is specified by a file called `Dockerfile`. Once you "compose"
    (instantiate) an image, it becomes a runnable container.

    The Dockerfile contains a list of commands to modify a base container.
    Here, we'll show you the basic commands used in Dockerfiles, with examples.
    """

    st.caption('These don\'t *have* to be uppercase, but they always are by convention')

    # Docs are here: https://docs.docker.com/engine/reference/builder/#from
    """
    - [FROM](https://docs.docker.com/engine/reference/builder/#from) `[--platform=<platform>] <image> [AS <name>]`
        - Always the very first line in a file (with a couple of advanced exceptions you don't
        need to worry about), it specifies the base image from the docker website
        - `FROM ubuntu:22.04`
            - sets the base image to Ubuntu Linux, version 22.04
    - [RUN](https://docs.docker.com/engine/reference/builder/#run) `<command> <param1> <param2>` OR [RUN](https://docs.docker.com/engine/reference/builder/#run) `["executable", "param1", "param2"]`
        - Runs a command from inside the container to set things up. By defualt,
        it uses bash in a Linux image, or powershell in a Windows image.
        - It can also take some additional arguments, like --mount, for mounting
        drives, and --network for some networking commands
        - `RUN apt-get install python3`
            - Installs Python3 inside the container
        - `RUN ["c:\\windows\\system32\\tasklist.exe"]`
            - Runs the specified executable inside the container
    - [ADD](https://docs.docker.com/engine/reference/builder/#add) `[--checksum=<checksum>] <src>... <dest>`
    - [COPY](https://docs.docker.com/engine/reference/builder/#copy) `[--checksum=<checksum>] <src>... <dest>`
        - These essentially do the same thing. They copy files, directories,
        or URLs from <src> (on the local machine) to <dest> (in the container).
        They also support standard regex file matching.
        - The only difference is that `ADD` automatically unzips compressed files,
        and fetches URLs, while `COPY` copies them directly, and doesn't fetch URLs.
        - `COPY hom* /home/working/`
            - Copies all files in the current directory on the local machine
            starting with "hom" to the `/home/working/` directory in the container
        - `ADD https://github.com/moby/buildkit.git#v0.10.1 /buildkit`
            - Copies the repo from the github URL to the `/buildkit/` directory
            in the container
    - [CMD](https://docs.docker.com/engine/reference/builder/#cmd) `<command> <param1> <param2>` OR [CMD](https://docs.docker.com/engine/reference/builder/#cmd) `["executable","param1","param2"]`
    - [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) `<command> <param1> <param2>` OR [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) `["executable","param1","param2"]`
        - These essentially do the same thing. They allow you to set a command or
        executable to be run inside the container when the container is told to
        run (using the `docker run` command). Every image must have at least
        one of these specified.
        - The only difference is that `CMD`
        is meant to provide default arguements to the executable, and `ENTRYPOINT`
        is meant to specify the executable itself. However, both can do both (I'm
        reasonably certain)
        - `CMD uname -a`
            - Displays the kernel info when the image is run
    - [LABEL](https://docs.docker.com/engine/reference/builder/#label) `<key>=<value> <key>=<value>`
        - Specifies metadata for the image, like version or description.
        - `LABEL version="1.0"`
            - Sets the image version to 1.0
    - [EXPOSE](https://docs.docker.com/engine/reference/builder/#expose) `<port>[/<protocol>]`
        - Exposes a port on the local machine to the container
        - `EXPOSE 80/udp`
            - Exposes UDP port 80 to the container
    - [ARG](https://docs.docker.com/engine/reference/builder/#arg) `<name>[=<default value>]`
        - Defines a variable the user can define at build time using the `--build-arg <varname>=<value>`
        - `ARG buildno=1`
            - Sets the variable in the script named `buildno` to 1 if not specified

    There's a few more more complicated commands I'll skim over:
    - [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir) `WORKDIR /path/to/workdir`
        - Specifies the current working directory like the cd command
    - [VOLUME](https://docs.docker.com/engine/reference/builder/#volume) `["/data"]`
        - Specifies a mount point and marks it as holding externally mounted volumes
    - [STOPSIGNAL](https://docs.docker.com/engine/reference/builder/#stopsignal) `signal`
        - Specifies what needs to be run before the container shuts down
    - [USER](https://docs.docker.com/engine/reference/builder/#user) `<user>[:<group>]`
        - Specifies the user which runs following commands
    - [ONBUILD](https://docs.docker.com/engine/reference/builder/#onbuild) `*INSTRUCTION*`
        - Used for doing things when the image is used as a base image for another image
    - [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) `[OPTIONS] CMD command` OR [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) `NONE`
        - Runs a command to check that the container is working properly (or disables
        health check from the inherited image)
    - [SHELL](https://docs.docker.com/engine/reference/builder/#shell) `["executable", "parameters"]`
        - Specifies which shell executable is used for following commands
    """

with st.expander('Example'):
    st.code('''
    FROM ubuntu:22.04
    # creates a layer from the ubuntu:22.04 Docker image.
    COPY . /app
    # adds files from your Docker client's current directory to /app
    RUN make /app
    # builds your application with the make command
    CMD python /app/app.py
    # specifies what command to run within the container.
    ''', language='docker')
