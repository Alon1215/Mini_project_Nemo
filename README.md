#  Digital Humanities - Nemo and Israel's archives
The project focuses on analyzing NER (Named Entity recognition) in documents in the Israel's archives.
The enitities are parsed and extracted using "Nemo" - neural modeling for NER.

## Tools
* Nemo:
  1. The paper: https://arxiv.org/abs/2007.15620
  2. Github - https://github.com/OnlpLab/NEMO
  * We modifed the source code of its implementation to enable running it locally and on CPU.
  * Nemo's requiements are detailed in its repository.
  
* OpenRefine
  for data visualization & post process. can use any different application which enables viewing csv files with hebrew characters.
  
* Python
  1. Pandas
  2. Numpy

* Full requirements:
  * bclm 
  * brotlipy==0.7.0
  * certifi==2021.5.30
  * cffi @ file:///C:/ci/cffi_1613247279197/work
  * chardet @ file:///C:/ci/chardet_1607690654534/work
  * conllu==4.4
  * cryptography @ file:///C:/ci/cryptography_1616769344312/work
  * decorator @ file:///home/ktietz/src/ci/decorator_1611930055503/work
  * idna @ file:///home/linux1/recipes/ci/idna_1610986105248/work
  * mkl-fft==1.3.0
  * mkl-random @ file:///C:/ci/mkl_random_1618854156666/work
  * mkl-service==2.3.0
  * networkx @ file:///tmp/build/80754af9/networkx_1617653298338/work
  * numpy==1.21.0
  * olefile==0.46
  * pandas==1.2.5
  * Pillow @ file:///C:/ci/pillow_1617386341487/work
  * pycparser @ file:///tmp/build/80754af9/pycparser_1594388511720/work
  * pyOpenSSL @ file:///tmp/build/80754af9/pyopenssl_1608057966937/work
  * PySocks @ file:///C:/ci/pysocks_1605287845585/work
  * python-dateutil==2.8.1
  * pytz==2021.1
  * requests @ file:///tmp/build/80754af9/requests_1608241421344/work
  * six==1.16.0
  * torch==1.9.0
  * torchaudio==0.9.0
  * torchvision==0.10.0
  * typing-extensions @ file:///tmp/build/80754af9/typing_extensions_1624965014186/work
  * urllib3 @ file:///tmp/build/80754af9/urllib3_1625084269274/work
  * win-inet-pton @ file:///C:/ci/win_inet_pton_1605306167264/work
  * wincertstore==0.2
