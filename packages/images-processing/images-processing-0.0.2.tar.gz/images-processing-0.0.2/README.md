# Projeto _ Descomplicando a criação de pacotes de processamento de imagens em Python

<h1>
    <img src="https://i.ibb.co/4fxm5bL/Descomplicando-a-cria-o-de-pacotes-de-processamento-de-imagens-em-Python.jpg" border="0">
</h1>

Neste projeto sera criado o primeiro pacote de processamento de imagens em Python e disponibilizá-lo no repositório Pypi. 
 <br>
Assim  poderá ser reutilizado facilmente e compartilhá-lo com outras pessoas. 
<br>

### O pacote "image-processing-test" é usado para::

Módulo "Processing":<br>
- Correspondência de histograma<br>
- Similaridade estrutural<br>
- Redimensionar imagem<br>
<br>
Módulo "Utils":<br>
- Leia a imagem<br>
- Salvar imagem<br>
- Plotar imagem<br>
- Plotar Resultado do grafico<br>
- Plotar histograma<br>

### Comandos de Instalação 

py -m pip install --upgrade pip<br>
py -m pip install --user twine<br>
py -m pip install --user setuptools<br>

py -m pip install --upgrade pip setuptools wheel

### Comandos para criar Distribuições

Para evitar erro : <b>error: invalid command 'bdist_wheel'</b>
<br>
Rodei antes : 
<br>
pip install wheel
<br>
Depois 
<br>
python setup.py sdist bdist_wheel 
<br>

<br>

Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - build
  - dist
  - images_processing.egg-info.
  

### Comandos para Publicar no Test Pypi

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*




## Me siga nas redes sociais

https://linktr.ee/ygtecnologia 
<br>
<br> 
Investir em conhecimento rende sempre os melhores juros. Benjamim Franklin
<br>
<br> 
Oração ! Foco ! Ação ! Yeshua Hamashia