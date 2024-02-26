#Pagina inicial contendo:
    #Titulo do site
    #Botão de entrar no site
    
#Dentro do botão de entrar no site:
    #popap contendo:
        #cauxa de texto para inserir o nome do usuario
        #botão "entrar chat"

#depois de clicar no "entrar chat" deve remover:
    #remover popup
    #remover botao_inicial
    
#Depois adicionar:

    #a area do chat
    #barra para digitar a mensagem
    #botão para enviar a mensagem
    #que usuario entrou no chat
    #aparecer no chat o nome do usuario que enviou a mensagem e a mensagem
    
    
    

import flet as ft

def main(pagina):
    
    
    Titulo = ft.Text("HashZap", size= 23)
    chat =ft.Column()
    nome_usuario = ft.TextField(label="Digite seu nome")
    caixa_texto = ft.TextField(label="Digite sua mensagem")
   
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        
    def entrar_chat(evento):
        pagina.remove(Botao_inicial)
        popup.open = False
        pagina.add(chat)
        linha_mensagem = ft.Row([caixa_texto, botao_enviar_mensagem])
        chat.controls.append(ft.Text(f"{nome_usuario.value} entrou no chat", color= ft.colors.ORANGE_500))
        pagina.add(linha_mensagem)
        
        pagina.update()
        
    def enviar_mensagem(evento):
        
        texto_caixa_texto = f"{ nome_usuario.value} : {caixa_texto.value}"
        pagina.pubsub.send_all( texto_caixa_texto)
       
        caixa_texto.value = ""
        pagina.update()
        

    botao_enviar_mensagem = ft.ElevatedButton("enviar", on_click= enviar_mensagem)
    
    
    
    
    popup = ft.AlertDialog(
        open= False,
        modal = True,
        title = ft.Text("Bem vindo ao HashZap"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click= entrar_chat)]
    )
    
    def entrar_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
        
    
    Botao_inicial = ft.ElevatedButton("iniciar chat", on_click= entrar_popup)
    
    pagina.add(Titulo)
    pagina.add(Botao_inicial)
    
    
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
    
