import flet as ft


def main(page: ft.Page):

#========Função para trocar a cor do tema==========#
    def change_theme(e):
        page.theme_mode=(
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
            )
        page.update()

#=======Função para trocar o tema=============#
    barra=ft.Column()
    def progressebar(e):
        barra.controls.append(ft.ProgressBar(width=3000, color="Blue"))
        page.update()
    
            

#===========Função para About===================#
    def about(e):
        Autor1=ft.CircleAvatar(foreground_image_url="java.png",
                               tooltip="Mateus Ivano", width=50, height=50)
        page.add(Autor1)
        

 
#=========Criando a appBar==========================#
    page.appbar= ft.AppBar(leading=ft.Icon(ft.icons.COMPUTER),
                           leading_width=45,
                           bgcolor=ft.colors.PURPLE_500,
                           title= ft.Text("Digital MAK"),
                           toolbar_height=70,
                           center_title=True,
                           actions=[
                                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                                    ft.IconButton(ft.icons.INFO_OUTLINE),
                                    ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Log in", icon=ft.icons.LOGIN),
                                    ft.PopupMenuItem(text="Log out",icon=ft.icons.LOGOUT_OUTLINED, on_click=progressebar),
                                    ft.PopupMenuItem(text="feedback", icon=ft.icons.FEEDBACK),
                                ],
                               ),
                           ],)
#===========Criando a barra de navegação========================#

    rail=ft.NavigationRail(
        selected_index=0,
        bgcolor=ft.colors.WHITE,
        label_type=ft.NavigationRailLabelType.SELECTED,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_MAX_OUTLINED, label="Home" 
            ),
            ft.NavigationDestination(
                icon=ft.icons.NEWSPAPER,
                selected_icon=ft.icons.NEWSPAPER_OUTLINED,
                label="Information",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS,
                selected_icon=ft.icons.SETTINGS_OUTLINED,
                label="settings",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CONTACT_MAIL,
                selected_icon=ft.icons.CONTACT_MAIL_OUTLINED,
                label="About"
            )
        ],
        
    )
  
  
    page.add(
        ft.Row([
            rail,
            ft.VerticalDivider(width=1),
            barra,
            ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),],
            expand=True,),)
    
ft.app(main,view="web_browser")