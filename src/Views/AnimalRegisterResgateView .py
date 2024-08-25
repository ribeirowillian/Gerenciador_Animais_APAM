import flet as ft


def main(page):
    page.title = "Adicionar Resgate ao Animal"
    atendimento = ft.TextField(
        label="Atendimento",
        value="",
        width=650,
        height=56,
        border_radius=8,
    )
    obs_resgate = ft.TextField(
        hint_text="Observações de Resgate",
        value="",
        width=320,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )
    hist_anam = ft.TextField(
        hint_text="Histórico de ANAMNESE",
        value="",
        width=320,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )
    dest_prot = ft.TextField(
        label="Destinação do Protegido",
        value="",
        width=370,
        height=56,
        border_radius=8,
    )
    inter_e_medi = ft.TextField(
        label="Tratamento, Intervenção e Medicação",
        value="",
        width=320,
        height=56,
        border_radius=8,
    )
    local_resga = ft.TextField(
        label="Local Resgate",
        value="",
        width=430,
        height=56,
        border_radius=8,
    )
    diagnostico = ft.TextField(
        label="Diagnostico - Estado de Saúde",
        value="",
        width=320,
        height=56,
        border_radius=8,
    )
    data_resga = ft.TextField(
        hint_text='Data de Resgate',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=210,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    def change_date(e):
        data_resga.value = date_picker.value.date()
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date
    )
    bnt_data_resga = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_color=ft.colors.WHITE,
        height=50,
        width=50,
        on_click=lambda _: date_picker.pick_date()
    )
    page.overlay.append(date_picker)
    inter_curu = ft.Dropdown(
        width=210,
        options=[
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        hint_text="Intervenção Cirúrgica",
        alignment=ft.alignment.center,
        border_radius=8
    )
    bnt_salvar = ft.ElevatedButton()

    page.add(
        ft.Row([
            ft.Container(height=40)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            atendimento,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            local_resga,
            inter_curu,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            dest_prot,
            data_resga, bnt_data_resga,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            diagnostico,
            inter_e_medi,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=5),
        ft.Row([
            obs_resgate,
            hist_anam,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=20),
        ft.Row([
            ft.Container(width=900),
            bnt_salvar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        width=650
        ),
    )



if __name__ == "__main__":
    ft.app(target=main)
