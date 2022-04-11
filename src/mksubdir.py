import pathlib
import os


class MkSubDir:

    def __init__(self, arg1: str, arg2: str):
        self._diretorios = []
        if arg2 is None:
            self._pasta_nova = arg1
            self._pasta_base = pathlib.Path(__file__).parent.resolve()
        else:
            self._pasta_nova = arg2
            self._pasta_base = arg1
        if not self._pasta_nova.startswith("/") or not self._pasta_nova.startswith("\\"):
            self._pasta_nova = "/" + self._pasta_nova
        for diretorio in os.scandir(self._pasta_base):
            if diretorio.is_dir():
                self._diretorios.append(diretorio.path)

    def execute(self):
        total = len(self._diretorios)
        comando = input(f"Deseja criar a pasta {self._pasta_nova} em {total} diretorios de {self._pasta_base}? ")
        if comando.lower() != "s":
            return
        for diretorio in self._diretorios:
            pasta = diretorio + self._pasta_nova
            try:
                os.makedirs(pasta)
            except Exception as ex:
                print(f"Não foi possível criar {pasta}: {str(ex)}")
