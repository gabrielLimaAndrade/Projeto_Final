{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador = webdriver.Chrome()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Primeira Pagina de Produtos\n",
    "navegador.get('https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/entity---celular/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Smartphone Samsung Galaxy A15 6,5\" 128GB Azul Claro 4G 4GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Teste na primeira pagina\n",
    "Produto = '#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child(1) > a > div.sc-gQSkpc.jTodsw > h2'\n",
    "navegador.find_element(By.CSS_SELECTOR, Produto).text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ou R$ 898,20'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Teste Preço primeira pagina\n",
    "preco = ('#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child(1) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p')\n",
    "navegador.find_element(By.CSS_SELECTOR, preco).text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Smartphone Samsung Galaxy A15 6,5\" 128GB Azul Claro 4G 4GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip\n",
      "Smartphone Samsung Galaxy A05s 6,7\" 128GB Preto 6GB RAM Câm. Tripla 50MP + Selfie 8MP Bateria 5000mAh Dual Chip\n",
      "Smartphone Samsung Galaxy A15 6,5\" 256GB Azul Escuro 5G 8GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip\n",
      "Smartphone Motorola Moto G24 128GB Grafite 4GB + 4GB RAM Boost 6,6\" Câm. Dupla + Selfie 8MP Dual Chip\n",
      "Smartphone Motorola Moto G34 128GB Azul 5G 4GB + 4GB RAM Boost 6,5\" Câm. Dupla + Selfie 16MP Dual Chip\n",
      "Apple iPhone 13 128GB Estelar Tela 6,1” 12MP\n",
      "Samsung Galaxy S23 FE 5G Smartphone Android 128GB Verde\n",
      "Smartphone Samsung Galaxy A35 128GB Azul Escuro 5G 6GB RAM 6,6\" Câm. Tripla + Selfie 13MP Dual Chip\n",
      "Smartphone Samsung Galaxy A55 256GB Azul Escuro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 32MP Dual Chip\n",
      "Smartphone Samsung Galaxy S23 256GB Preto 5G 8GB RAM 6,1” Câm Tripla + Selfie 12MP\n",
      "Smartphone Motorola Moto G84 256GB Grafite 5G Snapdragon 695 8GB RAM 6,55\" Câm. Dupla + Selfie 16MP Dual Chip\n",
      "Smartphone Motorola Moto G04s 128GB Grafite 4GB RAM 6,6\" Câm 50MP + Selfie 5MP Dual Chip\n",
      "Smartphone Motorola Moto G54 256GB Azul 5G 8GB RAM 6,5\" Câm. Dupla + Selfie 16MP Dual Chip\n",
      "iPhone 12 Apple 64GB Preto Tela 6,1” 12MP iOS\n",
      "Apple iPhone 14 128GB Estelar 6,1” 12MP iOS 5G\n",
      "Smartphone Samsung Galaxy M55 256GB 5G 8GB RAM Verde Claro 6,7\" Câm. Tripla + Selfie 50MP Dual Chip\n",
      "Smartphone Motorola Moto G24 128GB 4G Tela 6,6 Câmera Dupla 50MP Selfie 8MP Dual Chip Android 14\n",
      "Smartphone Motorola Moto g34 5G - 256GB 16GB Ram Boost AI Camera 50MP NFC\n",
      "Smartphone Motorola Moto g34 5G - 256GB 16GB Ram Boost AI Camera 50MP NFC\n"
     ]
    }
   ],
   "source": [
    "#Adicionando da primeira pagina de produtos numa lista\n",
    "lista_produtos = []\n",
    "for n in range(1,20):\n",
    "    print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text)\n",
    "    dado_produtos = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text\n",
    "    lista_produtos.append(dado_produtos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ou R$ 898,20\n",
      "ou R$ 719,10\n",
      "ou R$ 1.104,15\n",
      "ou R$ 809,10\n",
      "ou R$ 872,10\n",
      "ou R$ 3.499,00\n",
      "ou R$ 2.519,10\n",
      "ou R$ 1.574,10\n",
      "ou R$ 2.339,10\n",
      "ou R$ 2.998,80\n",
      "ou R$ 1.529,10\n",
      "ou R$ 719,10\n",
      "ou R$ 1.259,10\n",
      "ou R$ 2.699,10\n",
      "ou R$ 4.099,00\n",
      "ou R$ 1.754,10\n",
      "ou R$ 700,74\n",
      "ou R$ 1.034,10\n",
      "ou R$ 1.034,10\n"
     ]
    }
   ],
   "source": [
    "#Adicionando da primeira pagina de preço numa lista\n",
    "lista_precos = [] \n",
    "for p in range(1,20):\n",
    "        print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text)\n",
    "        dado_preco = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text\n",
    "        lista_precos.append(dado_preco)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Acessando a Segunda pagina de produtos\n",
    "navegador.get('https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/entity---celular/?page=2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Smartphone Samsung Galaxy A25 6,5\" 256GB Azul 5G 8GB RAM Câm Tripla 50MP + Selfie 13MP Bateria 5000mAh Dual Chip'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#testando pagina 2 de produtos\n",
    "Produto = '#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child(1) > a > div.sc-gQSkpc.jTodsw > h2'\n",
    "navegador.find_element(By.CSS_SELECTOR, Produto).text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ou R$ 1.529,10'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Teste Preço 2 pagina\n",
    "preco = ('#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child(1) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p')\n",
    "navegador.find_element(By.CSS_SELECTOR, preco).text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Smartphone Samsung Galaxy A25 6,5\" 256GB Azul 5G 8GB RAM Câm Tripla 50MP + Selfie 13MP Bateria 5000mAh Dual Chip\n",
      "Smartphone Samsung Galaxy A55 128GB Azul Claro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 32MP Dual Chip\n",
      "Smartphone Motorola Edge 50 Pro 5G - 256GB 24GB Ram Boost 50MP Ultra-Pixel AI Camera IP68 NFC\n",
      "Smartphone Samsung Galaxy S23 Ultra 256GB Preto 5G 12GB RAM 6,8” Câm. Quádrupla + Selfie 12MP\n",
      "Smartphone Motorola Moto G04s 128GB Tela 6,6 Câmera 50MP Selfie 5MP Dual Chip Android 14\n",
      "Samsung Galaxy S23 FE 5G Smartphone Android 128GB\n",
      "Smartphone Motorola Moto G54 5G 256GB + 8 GB RAM Azul Câmera 50 MP OIS + 2 MP Frontal 16MP Tela 6,5 IPS Bateria 5000 mAh\n",
      "Smartphone Motorola Moto g04s - 128GB 8 GB Ram Boost AI Camera 16MP sensor FPS lateral\n",
      "Celular Idoso teclas grande Lenoxx Flip Cx 908 Dual Chip\n",
      "Apple iPhone 15 128GB Azul 6,1\" 48MP iOS 5G\n",
      "Smartphone Motorola Edge 40 Neo 5G 256GB 16GB RAM Boost Câmera Traseira Dupla 50MP + 13MP Selfie 32MP Tela 6.55\" Black Beauty\n",
      "Smartphone Motorola Moto g24 - 128GB 8GB Ram Boost AI Camera 50MP Night Vision\n",
      "Smartphone Samsung Galaxy A35 256GB Azul Escuro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 13MP Dual Chip\n",
      "Smartphone Motorola Moto G84 5G 256GB 16GB RAM Boost CâmeraTraseira Dupla 50MP + 8MP Selfie 16MP Tela 6.55\" Grafite\n",
      "Smartphone Motorola Moto g24 Power - 128GB 8GB Ram Boost AI Camera 50MP 6000 mAh\n",
      "Celular Samsung Galaxy A55 5G, Câmera Tripla até 50MP, Tela 6.6\", 256GB\n",
      "Smartphone Motorola Moto G24 4G 128GB 4GB RAM Tela 6,6\" Câmera Dupla 50MP + 2MP Frontal 8MP Grafite\n",
      "Smartphone Motorola Moto G84 5G 256GB 16GB RAM Boost CâmeraTraseira Dupla 50MP + 8MP Selfie 16MP Tela 6.55\" Azul-Vegan Leather\n",
      "Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb Preto\n"
     ]
    }
   ],
   "source": [
    "#Adicionando pagina 2 na tabela\n",
    "for n in range(1,20):\n",
    "    print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text)\n",
    "    dado_produtos = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text\n",
    "    lista_produtos.append(dado_produtos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ou R$ 1.529,10\n",
      "ou R$ 2.051,10\n",
      "ou R$ 2.708,10\n",
      "ou R$ 4.859,10\n",
      "ou R$ 660,71\n",
      "ou R$ 3.193,20\n",
      "ou R$ 1.190,00\n",
      "ou R$ 674,10\n",
      "R$ 127,90\n",
      "ou R$ 4.699,00\n",
      "ou R$ 1.637,53\n",
      "ou R$ 719,10\n",
      "ou R$ 1.799,10\n",
      "ou R$ 1.289,45\n",
      "ou R$ 740,12\n",
      "ou R$ 1.898,10\n",
      "ou R$ 699,00\n",
      "ou R$ 1.289,45\n",
      "ou R$ 1.370,71\n"
     ]
    }
   ],
   "source": [
    "#Adicionando da primeira pagina de preço numa lista\n",
    "for p in range(1,20):\n",
    "        print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text)\n",
    "        dado_preco = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text\n",
    "        lista_precos.append(dado_preco)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.get('https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/entity---celular/?page=3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Smartphone Motorola Moto G34 128GB 5G Tela 6,5 Câmera Dupla 50MP Selfie 16MP Dual Chip Android 14\n",
      "Apple iPhone 14 256GB Meia-noite 6,1” 12MP\n",
      "Celular ObaSmart Conecta verde 4G 32GB fácil de usar Obabox - OB027\n",
      "Celular Samsung Galaxy A35 5G, Câmera Tripla até 50MP, Tela 6.6\", 256GB\n",
      "Smartphone Motorola Moto G54 5G 256GB + 8 GB RAM Verde Camera 50 MP OIS + 2 MP Frontal 16MP Tela 6,5 IPS Bateria 5000 mAh\n",
      "Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb\n",
      "Smartphone Samsung Galaxy A55 256GB Azul Escuro\n",
      "Smartphone Samsung Galaxy A06 128GB 4GB RAM Azul Escuro 6,7\" Câm. Dupla + Selfie 8MP\n",
      "Smartphone Celular Xiaomi Redmi 13c 8gb 256gb\n",
      "Samsung Galaxy S23 FE 5G 128GB + Smartwatch\n",
      "Smartphone Samsung Galaxy S23 Ultra 256GB\n",
      "Smartphone Motorola Edge 40 Neo 5G Peach Fuzz 256 GB,Ram 8 GB Câmera 50 MP OIS + 13 MP, Selfie 32 MP Android 13\n",
      "Smartphone Motorola Moto g24 - 128GB 8GB Ram Boost AI Camera 50MP Night Vision\n",
      "Smartphone Xiaomi Redmi Note 13 8GB+256GB ( Preto ) 4G\n",
      "Smartphone Xiaomi Redmi 14C Global 128GB 4GB RAM Dual SIM Tela 6.88\" - Black - Preto\n",
      "Smartphone Motorola Edge 50 Pro 5G - 256GB 24GB Ram Boost 50MP Ultra-Pixel AI Camera IP68 NFC\n",
      "Smartphone Celular Xiaomi Redmi 13c 8gb 256gb\n",
      "Smartphone Xiaomi Pocophone C65 4G 256GB / 8GB ram (Versao Global) Black Preto\n",
      "Smartphone Samsung Galaxy S24 6,2\" Galaxy AI 128GB Violeta 5G 8GB RAM Câm. Tripla 50MP + Selfie 12MP Bateria 4000mAh Dual Chip\n"
     ]
    }
   ],
   "source": [
    "for n in range(1,20):\n",
    "    print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text)\n",
    "    dado_produtos = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({n}) > a > div.sc-gQSkpc.jTodsw > h2').text\n",
    "    lista_produtos.append(dado_produtos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ou R$ 860,97\n",
      "ou R$ 4.799,00\n",
      "ou R$ 413,92\n",
      "ou R$ 1.583,10\n",
      "ou R$ 1.190,00\n",
      "ou R$ 1.449,90\n",
      "ou R$ 2.473,20\n",
      "ou R$ 809,10\n",
      "ou R$ 1.223,51\n",
      "ou R$ 3.238,20\n",
      "ou R$ 5.983,20\n",
      "ou R$ 1.755,25\n",
      "ou R$ 719,10\n",
      "ou R$ 1.343,19\n",
      "ou R$ 919,86\n",
      "ou R$ 2.708,10\n",
      "ou R$ 1.287,08\n",
      "ou R$ 1.130,00\n",
      "ou R$ 4.319,10\n"
     ]
    }
   ],
   "source": [
    "for p in range(1,20):\n",
    "        print(navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text)\n",
    "        dado_preco = navegador.find_element(By.CSS_SELECTOR, f'#__next > div > main > section:nth-child(5) > div.sc-gxoAxl.khektj > div > ul > li:nth-child({p}) > a > div.sc-gQSkpc.jTodsw > div.sc-iGgWBj.eWtIHQ.sc-jdUcAg.egLKnN > div > div > p').text\n",
    "        lista_precos.append(dado_preco)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Smartphone Samsung Galaxy A15 6,5\" 128GB Azul Claro 4G 4GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip',\n",
       " 'Smartphone Samsung Galaxy A05s 6,7\" 128GB Preto 6GB RAM Câm. Tripla 50MP + Selfie 8MP Bateria 5000mAh Dual Chip',\n",
       " 'Smartphone Samsung Galaxy A15 6,5\" 256GB Azul Escuro 5G 8GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip',\n",
       " 'Smartphone Motorola Moto G24 128GB Grafite 4GB + 4GB RAM Boost 6,6\" Câm. Dupla + Selfie 8MP Dual Chip',\n",
       " 'Smartphone Motorola Moto G34 128GB Azul 5G 4GB + 4GB RAM Boost 6,5\" Câm. Dupla + Selfie 16MP Dual Chip',\n",
       " 'Apple iPhone 13 128GB Estelar Tela 6,1” 12MP',\n",
       " 'Samsung Galaxy S23 FE 5G Smartphone Android 128GB Verde',\n",
       " 'Smartphone Samsung Galaxy A35 128GB Azul Escuro 5G 6GB RAM 6,6\" Câm. Tripla + Selfie 13MP Dual Chip',\n",
       " 'Smartphone Samsung Galaxy A55 256GB Azul Escuro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 32MP Dual Chip',\n",
       " 'Smartphone Samsung Galaxy S23 256GB Preto 5G 8GB RAM 6,1” Câm Tripla + Selfie 12MP',\n",
       " 'Smartphone Motorola Moto G84 256GB Grafite 5G Snapdragon 695 8GB RAM 6,55\" Câm. Dupla + Selfie 16MP Dual Chip',\n",
       " 'Smartphone Motorola Moto G04s 128GB Grafite 4GB RAM 6,6\" Câm 50MP + Selfie 5MP Dual Chip',\n",
       " 'Smartphone Motorola Moto G54 256GB Azul 5G 8GB RAM 6,5\" Câm. Dupla + Selfie 16MP Dual Chip',\n",
       " 'iPhone 12 Apple 64GB Preto Tela 6,1” 12MP iOS',\n",
       " 'Apple iPhone 14 128GB Estelar 6,1” 12MP iOS 5G',\n",
       " 'Smartphone Samsung Galaxy M55 256GB 5G 8GB RAM Verde Claro 6,7\" Câm. Tripla + Selfie 50MP Dual Chip',\n",
       " 'Smartphone Motorola Moto G24 128GB 4G Tela 6,6 Câmera Dupla 50MP Selfie 8MP Dual Chip Android 14',\n",
       " 'Smartphone Motorola Moto g34 5G - 256GB 16GB Ram Boost AI Camera 50MP NFC',\n",
       " 'Smartphone Motorola Moto g34 5G - 256GB 16GB Ram Boost AI Camera 50MP NFC',\n",
       " 'Smartphone Samsung Galaxy A25 6,5\" 256GB Azul 5G 8GB RAM Câm Tripla 50MP + Selfie 13MP Bateria 5000mAh Dual Chip',\n",
       " 'Smartphone Samsung Galaxy A55 128GB Azul Claro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 32MP Dual Chip',\n",
       " 'Smartphone Motorola Edge 50 Pro 5G - 256GB 24GB Ram Boost 50MP Ultra-Pixel AI Camera IP68 NFC',\n",
       " 'Smartphone Samsung Galaxy S23 Ultra 256GB Preto 5G 12GB RAM 6,8” Câm. Quádrupla + Selfie 12MP',\n",
       " 'Smartphone Motorola Moto G04s 128GB Tela 6,6 Câmera 50MP Selfie 5MP Dual Chip Android 14',\n",
       " 'Samsung Galaxy S23 FE 5G Smartphone Android 128GB',\n",
       " 'Smartphone Motorola Moto G54 5G 256GB + 8 GB RAM Azul Câmera 50 MP OIS + 2 MP Frontal 16MP Tela 6,5 IPS Bateria 5000 mAh',\n",
       " 'Smartphone Motorola Moto g04s - 128GB 8 GB Ram Boost AI Camera 16MP sensor FPS lateral',\n",
       " 'Celular Idoso teclas grande Lenoxx Flip Cx 908 Dual Chip',\n",
       " 'Apple iPhone 15 128GB Azul 6,1\" 48MP iOS 5G',\n",
       " 'Smartphone Motorola Edge 40 Neo 5G 256GB 16GB RAM Boost Câmera Traseira Dupla 50MP + 13MP Selfie 32MP Tela 6.55\" Black Beauty',\n",
       " 'Smartphone Motorola Moto g24 - 128GB 8GB Ram Boost AI Camera 50MP Night Vision',\n",
       " 'Smartphone Samsung Galaxy A35 256GB Azul Escuro 5G 8GB RAM 6,6\" Câm. Tripla + Selfie 13MP Dual Chip',\n",
       " 'Smartphone Motorola Moto G84 5G 256GB 16GB RAM Boost CâmeraTraseira Dupla 50MP + 8MP Selfie 16MP Tela 6.55\" Grafite',\n",
       " 'Smartphone Motorola Moto g24 Power - 128GB 8GB Ram Boost AI Camera 50MP 6000 mAh',\n",
       " 'Celular Samsung Galaxy A55 5G, Câmera Tripla até 50MP, Tela 6.6\", 256GB',\n",
       " 'Smartphone Motorola Moto G24 4G 128GB 4GB RAM Tela 6,6\" Câmera Dupla 50MP + 2MP Frontal 8MP Grafite',\n",
       " 'Smartphone Motorola Moto G84 5G 256GB 16GB RAM Boost CâmeraTraseira Dupla 50MP + 8MP Selfie 16MP Tela 6.55\" Azul-Vegan Leather',\n",
       " 'Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb Preto',\n",
       " 'Smartphone Motorola Moto G34 128GB 5G Tela 6,5 Câmera Dupla 50MP Selfie 16MP Dual Chip Android 14',\n",
       " 'Apple iPhone 14 256GB Meia-noite 6,1” 12MP',\n",
       " 'Celular ObaSmart Conecta verde 4G 32GB fácil de usar Obabox - OB027',\n",
       " 'Celular Samsung Galaxy A35 5G, Câmera Tripla até 50MP, Tela 6.6\", 256GB',\n",
       " 'Smartphone Motorola Moto G54 5G 256GB + 8 GB RAM Verde Camera 50 MP OIS + 2 MP Frontal 16MP Tela 6,5 IPS Bateria 5000 mAh',\n",
       " 'Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb',\n",
       " 'Smartphone Samsung Galaxy A55 256GB Azul Escuro',\n",
       " 'Smartphone Samsung Galaxy A06 128GB 4GB RAM Azul Escuro 6,7\" Câm. Dupla + Selfie 8MP',\n",
       " 'Smartphone Celular Xiaomi Redmi 13c 8gb 256gb',\n",
       " 'Samsung Galaxy S23 FE 5G 128GB + Smartwatch',\n",
       " 'Smartphone Samsung Galaxy S23 Ultra 256GB',\n",
       " 'Smartphone Motorola Edge 40 Neo 5G Peach Fuzz 256 GB,Ram 8 GB Câmera 50 MP OIS + 13 MP, Selfie 32 MP Android 13',\n",
       " 'Smartphone Motorola Moto g24 - 128GB 8GB Ram Boost AI Camera 50MP Night Vision',\n",
       " 'Smartphone Xiaomi Redmi Note 13 8GB+256GB ( Preto ) 4G',\n",
       " 'Smartphone Xiaomi Redmi 14C Global 128GB 4GB RAM Dual SIM Tela 6.88\" - Black - Preto',\n",
       " 'Smartphone Motorola Edge 50 Pro 5G - 256GB 24GB Ram Boost 50MP Ultra-Pixel AI Camera IP68 NFC',\n",
       " 'Smartphone Celular Xiaomi Redmi 13c 8gb 256gb',\n",
       " 'Smartphone Xiaomi Pocophone C65 4G 256GB / 8GB ram (Versao Global) Black Preto',\n",
       " 'Smartphone Samsung Galaxy S24 6,2\" Galaxy AI 128GB Violeta 5G 8GB RAM Câm. Tripla 50MP + Selfie 12MP Bateria 4000mAh Dual Chip']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lista_produtos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['ou R$ 898,20',\n",
       " 'ou R$ 719,10',\n",
       " 'ou R$ 1.104,15',\n",
       " 'ou R$ 809,10',\n",
       " 'ou R$ 872,10',\n",
       " 'ou R$ 3.499,00',\n",
       " 'ou R$ 2.519,10',\n",
       " 'ou R$ 1.574,10',\n",
       " 'ou R$ 2.339,10',\n",
       " 'ou R$ 2.998,80',\n",
       " 'ou R$ 1.529,10',\n",
       " 'ou R$ 719,10',\n",
       " 'ou R$ 1.259,10',\n",
       " 'ou R$ 2.699,10',\n",
       " 'ou R$ 4.099,00',\n",
       " 'ou R$ 1.754,10',\n",
       " 'ou R$ 700,74',\n",
       " 'ou R$ 1.034,10',\n",
       " 'ou R$ 1.034,10',\n",
       " 'ou R$ 1.529,10',\n",
       " 'ou R$ 2.051,10',\n",
       " 'ou R$ 2.708,10',\n",
       " 'ou R$ 4.859,10',\n",
       " 'ou R$ 660,71',\n",
       " 'ou R$ 3.193,20',\n",
       " 'ou R$ 1.190,00',\n",
       " 'ou R$ 674,10',\n",
       " 'R$ 127,90',\n",
       " 'ou R$ 4.699,00',\n",
       " 'ou R$ 1.637,53',\n",
       " 'ou R$ 719,10',\n",
       " 'ou R$ 1.799,10',\n",
       " 'ou R$ 1.289,45',\n",
       " 'ou R$ 740,12',\n",
       " 'ou R$ 1.898,10',\n",
       " 'ou R$ 699,00',\n",
       " 'ou R$ 1.289,45',\n",
       " 'ou R$ 1.370,71',\n",
       " 'ou R$ 860,97',\n",
       " 'ou R$ 4.799,00',\n",
       " 'ou R$ 413,92',\n",
       " 'ou R$ 1.583,10',\n",
       " 'ou R$ 1.190,00',\n",
       " 'ou R$ 1.449,90',\n",
       " 'ou R$ 2.473,20',\n",
       " 'ou R$ 809,10',\n",
       " 'ou R$ 1.223,51',\n",
       " 'ou R$ 3.238,20',\n",
       " 'ou R$ 5.983,20',\n",
       " 'ou R$ 1.755,25',\n",
       " 'ou R$ 719,10',\n",
       " 'ou R$ 1.343,19',\n",
       " 'ou R$ 919,86',\n",
       " 'ou R$ 2.708,10',\n",
       " 'ou R$ 1.287,08',\n",
       " 'ou R$ 1.130,00',\n",
       " 'ou R$ 4.319,10']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lista_precos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "Tabela1 = pd.DataFrame(lista_produtos, columns = ['Produtos'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "Tabela2 = pd.DataFrame(lista_precos, columns = ['Preços'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "db = pd.concat([Tabela1, Tabela2], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "db['Preços']=db.Preços.str.replace('ou', ' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Produtos</th>\n",
       "      <th>Preços</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Smartphone Samsung Galaxy A15 6,5\" 128GB Azul ...</td>\n",
       "      <td>R$ 898,20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Smartphone Samsung Galaxy A05s 6,7\" 128GB Pret...</td>\n",
       "      <td>R$ 719,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Smartphone Samsung Galaxy A15 6,5\" 256GB Azul ...</td>\n",
       "      <td>R$ 1.104,15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Smartphone Motorola Moto G24 128GB Grafite 4GB...</td>\n",
       "      <td>R$ 809,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Smartphone Motorola Moto G34 128GB Azul 5G 4GB...</td>\n",
       "      <td>R$ 872,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Apple iPhone 13 128GB Estelar Tela 6,1” 12MP</td>\n",
       "      <td>R$ 3.499,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Samsung Galaxy S23 FE 5G Smartphone Android 12...</td>\n",
       "      <td>R$ 2.519,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Smartphone Samsung Galaxy A35 128GB Azul Escur...</td>\n",
       "      <td>R$ 1.574,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Smartphone Samsung Galaxy A55 256GB Azul Escur...</td>\n",
       "      <td>R$ 2.339,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Smartphone Samsung Galaxy S23 256GB Preto 5G 8...</td>\n",
       "      <td>R$ 2.998,80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Smartphone Motorola Moto G84 256GB Grafite 5G ...</td>\n",
       "      <td>R$ 1.529,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Smartphone Motorola Moto G04s 128GB Grafite 4G...</td>\n",
       "      <td>R$ 719,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Smartphone Motorola Moto G54 256GB Azul 5G 8GB...</td>\n",
       "      <td>R$ 1.259,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>iPhone 12 Apple 64GB Preto Tela 6,1” 12MP iOS</td>\n",
       "      <td>R$ 2.699,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Apple iPhone 14 128GB Estelar 6,1” 12MP iOS 5G</td>\n",
       "      <td>R$ 4.099,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Smartphone Samsung Galaxy M55 256GB 5G 8GB RAM...</td>\n",
       "      <td>R$ 1.754,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Smartphone Motorola Moto G24 128GB 4G Tela 6,6...</td>\n",
       "      <td>R$ 700,74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Smartphone Motorola Moto g34 5G - 256GB 16GB R...</td>\n",
       "      <td>R$ 1.034,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Smartphone Motorola Moto g34 5G - 256GB 16GB R...</td>\n",
       "      <td>R$ 1.034,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Smartphone Samsung Galaxy A25 6,5\" 256GB Azul ...</td>\n",
       "      <td>R$ 1.529,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Smartphone Samsung Galaxy A55 128GB Azul Claro...</td>\n",
       "      <td>R$ 2.051,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Smartphone Motorola Edge 50 Pro 5G - 256GB 24G...</td>\n",
       "      <td>R$ 2.708,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Smartphone Samsung Galaxy S23 Ultra 256GB Pret...</td>\n",
       "      <td>R$ 4.859,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Smartphone Motorola Moto G04s 128GB Tela 6,6 C...</td>\n",
       "      <td>R$ 660,71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Samsung Galaxy S23 FE 5G Smartphone Android 128GB</td>\n",
       "      <td>R$ 3.193,20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Smartphone Motorola Moto G54 5G 256GB + 8 GB R...</td>\n",
       "      <td>R$ 1.190,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Smartphone Motorola Moto g04s - 128GB 8 GB Ram...</td>\n",
       "      <td>R$ 674,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Celular Idoso teclas grande Lenoxx Flip Cx 908...</td>\n",
       "      <td>R$ 127,90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Apple iPhone 15 128GB Azul 6,1\" 48MP iOS 5G</td>\n",
       "      <td>R$ 4.699,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Smartphone Motorola Edge 40 Neo 5G 256GB 16GB ...</td>\n",
       "      <td>R$ 1.637,53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Smartphone Motorola Moto g24 - 128GB 8GB Ram B...</td>\n",
       "      <td>R$ 719,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Smartphone Samsung Galaxy A35 256GB Azul Escur...</td>\n",
       "      <td>R$ 1.799,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Smartphone Motorola Moto G84 5G 256GB 16GB RAM...</td>\n",
       "      <td>R$ 1.289,45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>Smartphone Motorola Moto g24 Power - 128GB 8GB...</td>\n",
       "      <td>R$ 740,12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>Celular Samsung Galaxy A55 5G, Câmera Tripla a...</td>\n",
       "      <td>R$ 1.898,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Smartphone Motorola Moto G24 4G 128GB 4GB RAM ...</td>\n",
       "      <td>R$ 699,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>Smartphone Motorola Moto G84 5G 256GB 16GB RAM...</td>\n",
       "      <td>R$ 1.289,45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb ...</td>\n",
       "      <td>R$ 1.370,71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Smartphone Motorola Moto G34 128GB 5G Tela 6,5...</td>\n",
       "      <td>R$ 860,97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>Apple iPhone 14 256GB Meia-noite 6,1” 12MP</td>\n",
       "      <td>R$ 4.799,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Celular ObaSmart Conecta verde 4G 32GB fácil d...</td>\n",
       "      <td>R$ 413,92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>Celular Samsung Galaxy A35 5G, Câmera Tripla a...</td>\n",
       "      <td>R$ 1.583,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>Smartphone Motorola Moto G54 5G 256GB + 8 GB R...</td>\n",
       "      <td>R$ 1.190,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb</td>\n",
       "      <td>R$ 1.449,90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>Smartphone Samsung Galaxy A55 256GB Azul Escuro</td>\n",
       "      <td>R$ 2.473,20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Smartphone Samsung Galaxy A06 128GB 4GB RAM Az...</td>\n",
       "      <td>R$ 809,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Smartphone Celular Xiaomi Redmi 13c 8gb 256gb</td>\n",
       "      <td>R$ 1.223,51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Samsung Galaxy S23 FE 5G 128GB + Smartwatch</td>\n",
       "      <td>R$ 3.238,20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Smartphone Samsung Galaxy S23 Ultra 256GB</td>\n",
       "      <td>R$ 5.983,20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Smartphone Motorola Edge 40 Neo 5G Peach Fuzz ...</td>\n",
       "      <td>R$ 1.755,25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>Smartphone Motorola Moto g24 - 128GB 8GB Ram B...</td>\n",
       "      <td>R$ 719,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>Smartphone Xiaomi Redmi Note 13 8GB+256GB ( Pr...</td>\n",
       "      <td>R$ 1.343,19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>Smartphone Xiaomi Redmi 14C Global 128GB 4GB R...</td>\n",
       "      <td>R$ 919,86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>Smartphone Motorola Edge 50 Pro 5G - 256GB 24G...</td>\n",
       "      <td>R$ 2.708,10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>Smartphone Celular Xiaomi Redmi 13c 8gb 256gb</td>\n",
       "      <td>R$ 1.287,08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>55</th>\n",
       "      <td>Smartphone Xiaomi Pocophone C65 4G 256GB / 8GB...</td>\n",
       "      <td>R$ 1.130,00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>56</th>\n",
       "      <td>Smartphone Samsung Galaxy S24 6,2\" Galaxy AI 1...</td>\n",
       "      <td>R$ 4.319,10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Produtos         Preços\n",
       "0   Smartphone Samsung Galaxy A15 6,5\" 128GB Azul ...      R$ 898,20\n",
       "1   Smartphone Samsung Galaxy A05s 6,7\" 128GB Pret...      R$ 719,10\n",
       "2   Smartphone Samsung Galaxy A15 6,5\" 256GB Azul ...    R$ 1.104,15\n",
       "3   Smartphone Motorola Moto G24 128GB Grafite 4GB...      R$ 809,10\n",
       "4   Smartphone Motorola Moto G34 128GB Azul 5G 4GB...      R$ 872,10\n",
       "5        Apple iPhone 13 128GB Estelar Tela 6,1” 12MP    R$ 3.499,00\n",
       "6   Samsung Galaxy S23 FE 5G Smartphone Android 12...    R$ 2.519,10\n",
       "7   Smartphone Samsung Galaxy A35 128GB Azul Escur...    R$ 1.574,10\n",
       "8   Smartphone Samsung Galaxy A55 256GB Azul Escur...    R$ 2.339,10\n",
       "9   Smartphone Samsung Galaxy S23 256GB Preto 5G 8...    R$ 2.998,80\n",
       "10  Smartphone Motorola Moto G84 256GB Grafite 5G ...    R$ 1.529,10\n",
       "11  Smartphone Motorola Moto G04s 128GB Grafite 4G...      R$ 719,10\n",
       "12  Smartphone Motorola Moto G54 256GB Azul 5G 8GB...    R$ 1.259,10\n",
       "13      iPhone 12 Apple 64GB Preto Tela 6,1” 12MP iOS    R$ 2.699,10\n",
       "14     Apple iPhone 14 128GB Estelar 6,1” 12MP iOS 5G    R$ 4.099,00\n",
       "15  Smartphone Samsung Galaxy M55 256GB 5G 8GB RAM...    R$ 1.754,10\n",
       "16  Smartphone Motorola Moto G24 128GB 4G Tela 6,6...      R$ 700,74\n",
       "17  Smartphone Motorola Moto g34 5G - 256GB 16GB R...    R$ 1.034,10\n",
       "18  Smartphone Motorola Moto g34 5G - 256GB 16GB R...    R$ 1.034,10\n",
       "19  Smartphone Samsung Galaxy A25 6,5\" 256GB Azul ...    R$ 1.529,10\n",
       "20  Smartphone Samsung Galaxy A55 128GB Azul Claro...    R$ 2.051,10\n",
       "21  Smartphone Motorola Edge 50 Pro 5G - 256GB 24G...    R$ 2.708,10\n",
       "22  Smartphone Samsung Galaxy S23 Ultra 256GB Pret...    R$ 4.859,10\n",
       "23  Smartphone Motorola Moto G04s 128GB Tela 6,6 C...      R$ 660,71\n",
       "24  Samsung Galaxy S23 FE 5G Smartphone Android 128GB    R$ 3.193,20\n",
       "25  Smartphone Motorola Moto G54 5G 256GB + 8 GB R...    R$ 1.190,00\n",
       "26  Smartphone Motorola Moto g04s - 128GB 8 GB Ram...      R$ 674,10\n",
       "27  Celular Idoso teclas grande Lenoxx Flip Cx 908...      R$ 127,90\n",
       "28        Apple iPhone 15 128GB Azul 6,1\" 48MP iOS 5G    R$ 4.699,00\n",
       "29  Smartphone Motorola Edge 40 Neo 5G 256GB 16GB ...    R$ 1.637,53\n",
       "30  Smartphone Motorola Moto g24 - 128GB 8GB Ram B...      R$ 719,10\n",
       "31  Smartphone Samsung Galaxy A35 256GB Azul Escur...    R$ 1.799,10\n",
       "32  Smartphone Motorola Moto G84 5G 256GB 16GB RAM...    R$ 1.289,45\n",
       "33  Smartphone Motorola Moto g24 Power - 128GB 8GB...      R$ 740,12\n",
       "34  Celular Samsung Galaxy A55 5G, Câmera Tripla a...    R$ 1.898,10\n",
       "35  Smartphone Motorola Moto G24 4G 128GB 4GB RAM ...      R$ 699,00\n",
       "36  Smartphone Motorola Moto G84 5G 256GB 16GB RAM...    R$ 1.289,45\n",
       "37  Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb ...    R$ 1.370,71\n",
       "38  Smartphone Motorola Moto G34 128GB 5G Tela 6,5...      R$ 860,97\n",
       "39         Apple iPhone 14 256GB Meia-noite 6,1” 12MP    R$ 4.799,00\n",
       "40  Celular ObaSmart Conecta verde 4G 32GB fácil d...      R$ 413,92\n",
       "41  Celular Samsung Galaxy A35 5G, Câmera Tripla a...    R$ 1.583,10\n",
       "42  Smartphone Motorola Moto G54 5G 256GB + 8 GB R...    R$ 1.190,00\n",
       "43      Smartphone Xiaomi Redmi Note 13 8gb Ram 256gb    R$ 1.449,90\n",
       "44    Smartphone Samsung Galaxy A55 256GB Azul Escuro    R$ 2.473,20\n",
       "45  Smartphone Samsung Galaxy A06 128GB 4GB RAM Az...      R$ 809,10\n",
       "46      Smartphone Celular Xiaomi Redmi 13c 8gb 256gb    R$ 1.223,51\n",
       "47        Samsung Galaxy S23 FE 5G 128GB + Smartwatch    R$ 3.238,20\n",
       "48          Smartphone Samsung Galaxy S23 Ultra 256GB    R$ 5.983,20\n",
       "49  Smartphone Motorola Edge 40 Neo 5G Peach Fuzz ...    R$ 1.755,25\n",
       "50  Smartphone Motorola Moto g24 - 128GB 8GB Ram B...      R$ 719,10\n",
       "51  Smartphone Xiaomi Redmi Note 13 8GB+256GB ( Pr...    R$ 1.343,19\n",
       "52  Smartphone Xiaomi Redmi 14C Global 128GB 4GB R...      R$ 919,86\n",
       "53  Smartphone Motorola Edge 50 Pro 5G - 256GB 24G...    R$ 2.708,10\n",
       "54      Smartphone Celular Xiaomi Redmi 13c 8gb 256gb    R$ 1.287,08\n",
       "55  Smartphone Xiaomi Pocophone C65 4G 256GB / 8GB...    R$ 1.130,00\n",
       "56  Smartphone Samsung Galaxy S24 6,2\" Galaxy AI 1...    R$ 4.319,10"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "db.to_csv('../0_Bases_Originais/Magazine.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
