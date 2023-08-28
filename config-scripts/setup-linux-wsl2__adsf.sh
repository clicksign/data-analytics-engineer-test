echo 'Upgrading dependencies ...'
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autoclean

sudo apt install curl wget openssh-server openssh-client git tar silversearcher-ag unzip -y
sudo apt-get update; sudo apt-get install --no-install-recommends -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
sudo apt-get install -y gcc make zlib1g-dev libreadline-dev libreadline8 sqlite3 libsqlite3-dev libbz2-dev python-tk python3-tk tk-dev
sudo apt install sqlite3
sudo apt install unrar
    
echo 'Installing asdf ...'
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2
echo '. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo '. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc
source ~/.bashrc