from CaminhoDeDados import MemoriaDeInstrucoes
from UnidadeDeControle import UnidadeDeControle
from CaminhoDeDados import ALU
from CaminhoDeDados import BancoDeRegistradores


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n", ""))
        return linhas


if __name__ == "__main__":
    # caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"
    # caminho_arquivoAle = '/home/alemilson/Downloads/a.txt'
    #
    # linhas_arquivo = Arquivo.read(caminho_arquivoAle)
    #
    # for linha in linhas_arquivo:
    #     MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(linha)
    #     print(linha)
    # BancoDeRegistradores.s1.set("00000000000000000000000000011111")
    # BancoDeRegistradores.s2.set("00000000000000000000000100000110")
    # i = "00000010001100101000000100101010"
    # UnidadeDeControle.Control.setInstruction(list(i[::-1]))
    # UnidadeDeControle.Control.run()
    # UnidadeDeControle.HazardDetectionUnit.run()
    # UnidadeDeControle.FowardingUnit.run()
    # ALU.Alu.setData_1(BancoDeRegistradores.s1.get())
    # ALU.Alu.setData_2(BancoDeRegistradores.s2.get())
    # UnidadeDeControle.ALUControl.run()
    # ALU.Alu.setALUControl_input()
    # ALU.Alu.run()
    # print(ALU.Alu.getALUOutput())
    pass
