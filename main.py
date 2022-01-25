from CaminhoDeDados import MemoriaDeInstrucoes


# token repositório: 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

class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n", ""))
        return linhas


if __name__ == "__main__":
    caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"

    linhas_arquivo = Arquivo.read(caminho_arquivo)

    for linha in linhas_arquivo:
        MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(linha)
        print(linha)
