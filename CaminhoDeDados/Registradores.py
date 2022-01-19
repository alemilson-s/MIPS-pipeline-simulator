class zero:
    """
    Classe representando o registrador $zero
    """

    bits: list = []  # Lista utilizada para representar os 32 bits do registrador $zero
    id = '00000'

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $zero com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        return cls.id

print("jj")



class s0:
    bits: list = []  # Lista utilizada para representar os 32 bits do registrador
    id = '010000'

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $s0 com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        """
        Método para alterar os valores do intervalo fechado de bit_inicial a bit_final
        :param bit_inicial: Representa a posição inicial do bit ao qual iremos percorrer
        :param bit_final: Representa a posição final do bit ao qual iremos percorrer
        :param sequencia_de_bits: Valores ao qual serão inseridos na lista de bits
        :return: Função sem retorno
        """

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)

        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        """
        Método para retornar os valores do intervalo fechado de bit_inicial a bit_final
        :param bit_inicial: Representa a posição inicial do bit ao qual iremos percorrer
        :param bit_final: Representa a posição final do bit ao qual iremos percorrer
        :return: bits contido no intervalo fechado -> [bit_inicial, bit_final]
        """
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        """
        Método para alterar os 32 bits da lista(bits) representando os bits do registrador
        :param bits: String ou lista representando 32 bits
        :return: Não há retorno
        """
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits
        elif len(bits) == 32:
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        """
        Método para retornar os 32 bits contido no registrador
        :return: bits(lista que representa os 32 bits do registrador)
        """
        return cls.bits

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        return cls.id


print("asasas")