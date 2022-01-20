from CaminhoDeDados import MemoriaDeInstrucoes


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha)
        return linhas


if __name__ == "__main__":
    caminho_arquivo = "C:\\Users\\ALEMILSON\\OneDrive\\Imagens\\PROVA2EST\\testeLeitura.txt"

    linhas_arquivo = Arquivo.read(caminho_arquivo)

    for linha in linhas_arquivo:
        MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(linha)
