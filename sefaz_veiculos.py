
class VeiculoSefaz:
    def __init__(self,data_venda,livro,folha,renavam,placa, espelho,nome_comprador, cpf_comprador,cep_comprador,endereco_comprador, numero_end_comprador, bairro_end_comprador, uf_end_comp,municipio_end_comprador,complemento_end_comprador):
        self.data_venda = data_venda
        self.livro = livro
        self.folha=folha
        self.renavam = renavam
        self.placa = placa
        self.espelho = espelho
        self.nome_comprador = nome_comprador
        self.cpf_comprador = cpf_comprador
        self.cep_comprador = cep_comprador
        self.endereco_comprador = endereco_comprador
        self.numero_end_comprador = numero_end_comprador
        self.bairro_end_comprador = bairro_end_comprador
        self.complemento_end_comprador = complemento_end_comprador
        self.uf_end_comprador = uf_end_comp
        self.municipio_end_comprador = municipio_end_comprador
        self.cnpj_cartorio = '49.898.349/0001-81'
        self.cpf_responsavel = '015.398.548-84'
        self.nome_arquivo_p7s = None
        self.extensao = '.pdf.p7s'
        self.conteudo_arquivo_p7s = None
        self.tamanhoArquivoP7s = None
        self.tipo_documento_comprador = None  
    
    def get_tipo_documento_comprador(self):
        return 'CPF'     
    def get_tamanho_arquivo(self):
        return f'{self.tamanhoArquivoP7s} Kbytes' 
    
    def get_arquivo_p7s(self):
        return f'l{self.livro}f{self.folha}t000001{self.extensao}'
   
    def get_conteudo_arquivo_p7s(self):
        return f'MIMjdkfdskfjsdkfddisofuidueioruieurioeureiuriueireioureiourioeireuirueouroieuorklshkdfjkdjkdskf'  
            
    def exibir_informacoes(self):
        print(f'''<?xml version="1.0" encoding="UTF-8"?>
                <veiculos xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.fazenda.sp.gov.br/cartorios/ValidacaoTransferencia.xsd">
                <veiculo>
                        <renavam>{self.renavam}</renavam>
                        <placa>{self.placa}</placa>
                        <nroEspelho>{self.espelho}</nroEspelho>
                        <dataVenda>{self.data_venda}</dataVenda>
                        <cnpjCartorio>{self.cnpj_cartorio}</cnpjCartorio>
                        <cpfResponsavel>{self.cpf_responsavel}</cpfResponsavel>
                        <nomeArquivoP7S>{self.get_arquivo_p7s()}</nomeArquivoP7S>
                        <conteudoArquivoP7S>{self.get_conteudo_arquivo_p7s}</conteudoArquivoP7S>
                        <caminhoArquivoP7S>{f'C://{self.get_arquivo_p7s()}'}</caminhoArquivoP7S>
                        <tamanhoArquivoP7S>{self.get_tamanho_arquivo()}</tamanhoArquivoP7S>
                        <dadosComprador>
                        <tipoDocumento>{self.get_tipo_documento_comprador()}</tipoDocumento>
                        <documento>{self.cpf_comprador}</documento>
                        <descricaoDocumento>{self.nome_comprador}</descricaoDocumento>
                        <endereco>{self.endereco_comprador}</endereco>
                        <numero>{self.numero_end_comprador}</numero>
                        <complemento>{self.complemento_end_comprador}</complemento>
                        <bairro>{self.bairro_end_comprador}</bairro>
                        <cep>{self.cep_comprador}</cep>
                        <uf>{self.uf_end_comprador}</uf>
                        <municipio>{self.municipio_end_comprador}</municipio>
                        </dadosComprador>
                        <dadosReconhecimentoFirmaVendedor>
                        <livro></livro>
                        <folha></folha>
                        <dataReconhecimentoFirma></dataReconhecimentoFirma>
                        </dadosReconhecimentoFirmaVendedor>
                        <dadosReconhecimentoFirmaComprador>
                        <livro>{self.livro}</livro>
                        <folha>{self.folha}</folha>
                        <dataReconhecimentoFirma>{self.data_venda}</dataReconhecimentoFirma>
                        </dadosReconhecimentoFirmaComprador>
                        </veiculo>
                        <veiculo>''')    
        
if __name__ == '__main__':
    veiculo_enviar = VeiculoSefaz('18/09/2024','1418','1','00460248243','ETK6D61','244070563539','ANGELA APARECIA CARDOSO GOMES','25943125841','RUA DIRCEU CHIQUETO','100','CENTRO','SP','ASSIS','CASA','')   
    veiculo_enviar.exibir_informacoes() 
         
    