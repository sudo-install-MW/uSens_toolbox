# June 20 2018

# script to install tensorflow-gpu with required nvidia deep learning libraries


# install python3 pip
sudo apt-get install python3-pip
pip3 install jupyter

# Remove any nvidia drivers if any exists
sudo apt-get purge nvidia*

# Add and the repo for nvidia graphics drivers
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update



sudo apt-get install nvidia-375

# Install the latest cuda-dev kit
sudo apt-get install nvidia-cuda-dev

# Installing libcupti
sudo apt-get install libcupti-dev

#############################################TODO#################################################
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb


wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7_7.1.1.5-1+cuda9.1_amd64.deb


sudo dpkg -i cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
sudo dpkg -i libcudnn7_7.1.1.5-1+cuda9.1_amd64.deb

sudo apt-get update
sudo apt-get install cuda=9.1.85-1
sudo apt-get install libcudnn7-dev

pip3 install tensorflow-gpu==1.7
