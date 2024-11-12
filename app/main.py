import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.models.usuario_models import Usuario
from app.repositories.usuario_repositories import UsuarioRepository
from app.services.usuario_services import UsuarioService
from app.config.database import Session 

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService (repository)

    #Solicitando dados para o usuario 
    def cadastrar_usuario():
            print("\nAdicionando usuário.")
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")         
            senha = input("Digite sua senha: ")
    

            service.criar_usuario(nome=nome, email=email, senha=senha)


    def consultar_usuario():
            email_usuario = input("Digite o email do cliente: ")

            usuario = session.query(Usuario).filter_by(email = email_usuario).first()

            if usuario:
                print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

            else:
                print(f"Usuario não encontrado.")

    def atualizar_cadastro():
            email_usuario = input(f"Digite o email do usuário: ")
            usuario = session.query(Usuario).filter_by(email = email_usuario).first()
            if usuario:
                usuario.nome = input(f"Digite o nome: ")
                usuario.email = input(f"Digite o email: ")
                usuario.senha = input(f"Digite a senha: ")
                session.commit()

            else:
                print(f"Cliente não encontrado")

    def excluir_cadastro():
            email_usuario = input(f"Digite o email do usuário: ")
            usuario = session.query(Usuario).filter_by(email = email_usuario).first()
            if usuario:
                session.delete(usuario)
                session.commit()
                print(f"Usuário {usuario.nome} deletado com sucesso!")
            else:
                print(f"Cliente não encontrado")

    def listar_usuarios():
        listar_usuario = service.listar_todos_usuario()
        for usuario in listar_usuario:
                print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
        
    while True:
            print(f"\n== Tabela de serviços disponiveis ==")
            print(f"1- Cadastrar usuário")
            print(f"2- Consultar cadastro")
            print(f"3- Atualizar usuário")
            print(f"4- Excluir usuário")
            print(f"5- Listar usuários")
            print(f"0- Sair")
            opcao = int(input("Digite o número correspondente à opção desejada: "))
            match opcao: 
                case 1:
                    cadastrar_usuario()
            

                case 2:
                    consultar_usuario()


                case 3:
                    atualizar_cadastro()
                
                case 4:
                    excluir_cadastro()

                case 5:
                    listar_usuarios()
                case 0:
                    print(f"Encerrando o sistema")
                    break
                case _:
                    print(f"Tente novamente")

if __name__ == "__main__":
    main()