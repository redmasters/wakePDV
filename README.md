# Script para ligar PDVs


### Requisitos:
- Python3
- pip

### Instalação:

Clone o repositório:
- ``git clone https://github.com/redmasters/wakePDV.git`` 
- ``cd wakePDV``
- ``pip install -r requirements.txt``

### Uso:
- Na BIOS dos computadores, ative o recurso Wake On Lan, WOL;
- Edite o arquivo 'macs.py' com a lista de macs dos computadores que precisam ser ligados;
- Execute com ``python wakePDV.py`` ;
- É preciso está na mesma redes dos computadores alvo;

Roda no android com um terminal instalado. [Termux](https://termux.com/) no caso, funciona perfeitamente.