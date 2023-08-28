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