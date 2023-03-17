from pydantic import BaseModel


class BaseGame(BaseModel):
    uuid: str

    class Config:
        orm_mode = True


class GameShortDescription(BaseGame):
    short_description: str

    class Config:
        schema_extra = {
            "example": {
                "uuid": "b0939ea7-d6bc-4d58-bfe1-6c5cc3c01953",
                "short_description": """Neque porro quisquam est qui dolorem ipsum quia dolor sit amet,
                consectetur""",
            }
        }


class GameLongDescription(BaseGame):
    long_description: str

    class Config:
        schema_extra = {
            "example": {
                "uuid": "b0939ea7-d6bc-4d58-bfe1-6c5cc3c01953",
                "long_description": """Proin imperdiet bibendum odio, sit amet commodo justo congue at. Nulla vitae
                    nisi vel enim pellentesque congue sed in lectus. Quisque vestibulum velit eget neque aliquet
                    consectetur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer tincidunt tristique
                    leo nec posuere. Aliquam commodo ex quis vehicula aliquam. Fusce a vestibulum risus. Duis ac
                    mauris dapibus, varius tortor eget, vehicula est. Suspendisse ut purus at magna aliquam lacinia. Sed
                    finibus leo lectus, tincidunt condimentum magna bibendum vel. Aenean rhoncus nulla eget posuere
                    pretium. Aenean orci erat, aliquam ac accumsan in, luctus volutpat lacus. Sed sit amet ex eget orci
                    molestie efficitur a vitae nibh. Curabitur ut placerat nisi. Suspendisse efficitur in arcu ac pellentesque.
                    Curabitur congue interdum est."""
            }
        }


class Game(BaseModel):
    title: str
    shortDescription: str
    longDescription: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Far Cry 5",
                "shortDescription": """Bem-vindo a Hope County, Montana, terra dos livres
                  e valentes, mas também o lar de um culto apocalíptico fanático, conhecido 
                  como O Projeto em Eden's Gate, que está ameaçando a liberdade da comunidade. 
                  Enfrente os líderes do culto, Joseph Seed, e os Arautos, e acenda o fogo 
                  da resistência, que irá liberar a comunidade sitiada""",
                "longDescription":
                """Far Cry 5 é um jogo eletrônico de tiro em primeira pessoa de ação-aventura
                  ambientado em um mundo aberto. Foi desenvolvido pela Ubisoft Montreal 
                  e publicado pela Ubisoft para Microsoft Windows, PlayStation 4 e Xbox 
                  One em 27 de março de 2018 e foi lançado no 3 de Novembro para o 
                  Google Stadia, junto com o Far Cry: New Dawn.É o décimo titulo da 
                  serie Far Cry e o quinto jogo principal. Em Far Cry 5 o jogador 
                  assume o papel de um delegado de xerife que foi enviado ao condado 
                  fictício de Hope County, em Montana, para prender Joseph 
                  Seed(chamado de "O Pai" por seus seguidores, os "Edenetes"). Seed é
                    um pregador radical que acredita que foi escolhido por Deus para 
                    proteger o povo de Hope County de um "colapso inevitável". Ele é o 
                    criador e líder da seita cristã "Projeto do Portão do Éden", um culto 
                    apocalíptico religioso e militar. Far Cry 5 foi bem recebido pela 
                    crítica após o seu lançamento, apesar de ter sido objeto de controvérsia 
                    depois de ter sido anunciado ao lado de um período de intensos conflitos 
                    políticos. Os críticos elogiaram o design do mundo aberto, o seu visual 
                    e trilha sonora, mas dirigiram críticas para sua história e alguns dos 
                    personagens. O jogo teve um bom desempenho comercial e se tornou o 
                    título mais vendido da franquia, arrecadando mais de 310 milhões de 
                    dólares em sua primeira semana de vendas. Vários pacotes de conteúdo 
                    para download(DLC) foram lançados. Um título de spin-off e continuação 
                    da narrativa, Far Cry: New Dawn, foi lançado em fevereiro de 2019.""",
            }
        }
