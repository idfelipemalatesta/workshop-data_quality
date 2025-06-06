import pandera.pandas as pa
from pandera.typing.pandas import Series

class ProdutoSchema(pa.DataFrameModel):
    """
    Define o esquema para a validação de dados de produtos com Pandera.
    
    Este esquema inclui campos básicos para produtos, incluindo um campo de e-mail
    validado por uma expressão regular.

    Attributes:
        id_produto (Series[int]): Identificador do produto, deve estar entre 1 e 20.
        nome (Series[str]): Nome do produto.
        quantidade (Series[int]): Quantidade disponível do produto, deve estar entre 20 e 200.
        preco (Series[float]): Preço do produto, deve estar entre 5.0 e 120.0.
        categoria (Series[str]): Categoria do produto.
        email (Series[str]): E-mail associado ao produto, deve seguir o formato padrão de e-mails.
    """
    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=05.0, le=120.0)
    categoria: Series[str]
    #email: Series[str]

    class Config:
        coerce = True
        strict = True


class ProdutoSchema(pa.DataFrameModel):
    id_produto: pa.typing.Series[int] = pa.Field(ge=1, le=13, nullable=False)
    nome: pa.typing.Series[str] = pa.Field(nullable=False)
    quantidade: pa.typing.Series[int] = pa.Field(ge=-200, le=200, nullable=False)
    preco: pa.typing.Series[float] = pa.Field(ge=-10, le=120, nullable=False)
    categoria: pa.typing.Series[str] = pa.Field(nullable=False)

    class Config:
        coerce = True
        strict = False



class ProdutoSchemaKPI(ProdutoSchema):
    """
    Representa um esquema da classe Produto com indicadores-chave de desempenho (KPIs).

    Attributes:
        valor_total_estoque (Series[float]): Valor total do estoque, garantindo que seja maior ou igual a zero.
        categoria_normalizada (Series[str]): Categoria do produto normalizada para padronização de análise.
        disponibilidade (Series[bool]): Indica se o produto está disponível em estoque.
    """
    valor_total_estoque: Series[float] = pa.Field(ge=0)
    categoria_normalizada: Series[str]
    disponibilidade: Series[bool]  