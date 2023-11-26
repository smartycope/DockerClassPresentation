import streamlit as st

st.caption('Team Marquet')
st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-world.net%2Fwp-content%2Fuploads%2F2021%2F02%2FDocker-Symbol.png&f=1&nofb=1&ipt=5a14afd1e119e1ac15314fcdfdbb1773fa696a5236965cb353f443f7e97f5c97&ipo=images', width=400)

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
    """
    st.code('docker pull jupyter/all-spark-notebook')
    """
    We'll get to more details next week.
    """

with st.expander('Creating the Docker Container for Class Demonstration'):

    """

    1. Create a docker network 

    ```bash
    docker network create n451
    ```

    2. Git clone 
    
    ```bash
    git clone https://github.com/byuibigdata/docker_guide.git
    ```

    3. Now we'll create the docker container. In order to create it we will run this terminal code below.
    I personally had to put it all on one line. We'll also have to change the path
    (`C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\data`) which you will need to change.

    __Command Line: Mac__

    ```bash
    docker run --name spark -it \\
    -p 8888:8888 -p 4040:4040 -p 4041:4041 \\
    -v /Users/hathawayj/git/BYUI451/docker_guide/data:/home/jovyan/data \\
    -v /Users/hathawayj/git/BYUI451/docker_guide/scripts:/home/jovyan/scripts \\
    -v /Users/hathawayj/git/BYUI451/docker_guide/scratch:/home/jovyan/scratch \\
    --network n451 \\
    jupyter/all-spark-notebook
    ```

    __Command Line: Windows__

    ```bash
    docker run --name spark -it ^
    -p 8888:8888 -p 4040:4040 -p 4041:4041 ^
    -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\data:/home/jovyan/data ^
    -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\scripts:/home/jovyan/scripts ^
    -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\scratch:/home/jovyan/scratch ^
    --network n451 ^
    jupyter/all-spark-notebook
    ```
    
    __Here is what my code looked like__

    ```bash
    docker run --name spark -it -p 8888:8888 -p 4040:4040 -p 4041:4041 -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\data:/home/jovyan/data -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\scripts:/home/jovyan/scripts -v C:\\Users\\spence\\Desktop\\classes\\DS_460\\docker_guide\\scratch:/home/jovyan/scratch --network n451 jupyter/all-spark-notebook
    ```

    4. On your browser, go to `localhost:8888`
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
    In docker, you have several parts.
    #### Images
    Images are like a variable definition. Think of it like a C++ header file, or ...something else
    not relating to C++

    You define images by
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

with st.expander('Examples'):
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