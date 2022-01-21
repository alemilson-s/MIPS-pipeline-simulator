from CaminhoDeDados import MemoriaDeInstrucoes


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n",""))
        return linhas


if __name__ == "__main__":
    caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"

    linhas_arquivo = Arquivo.read(caminho_arquivo)

    for linha in linhas_arquivo:
        MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(linha)
        print(linha)
