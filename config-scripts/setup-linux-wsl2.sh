echo 'Upgrading dependencies ...'
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autoclean

sudo apt install sqlite3
sudo apt install unrar
    
echo 'Installing asdf ...'
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2
echo '. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo '. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc
source ~/.bashrc
sleep 5
source ~/.bashrc

echo 'Installing Python ...'
asdf plugin-add python
asdf install python 3.11.4
asdf global python 3.11.4

echo 'Installing Poetry ...'
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
asdf install poetry 1.6.1
echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bashrc

echo 'Updating the project ...'
git pull
cd ..

if [ ! -f pyproject.toml ]; then
    echo 'Creating pyproject.toml ...'
    poetry init
fi

echo 'Installing dependencies and pre-commit ...'
poetry install
poetry run pre-commit install