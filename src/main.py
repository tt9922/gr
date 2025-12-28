import flet as ft

def main(page: ft.Page):
    page.title = "都道府県人口表示アプリ"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 2020年国勢調査の人口データ (単位: 人)
    population_data = {
        "北海道": 5224614,
        "青森県": 1237984,
        "岩手県": 1210534,
        "宮城県": 2301996,
        "秋田県": 959502,
        "山形県": 1068027,
        "福島県": 1833152,
        "茨城県": 2867009,
        "栃木県": 1933146,
        "群馬県": 1939110,
        "埼玉県": 7344765,
        "千葉県": 6284480,
        "東京都": 14047594,
        "神奈川県": 9237337,
        "新潟県": 2201272,
        "富山県": 1034814,
        "石川県": 1132526,
        "福井県": 766863,
        "山梨県": 809974,
        "長野県": 2048011,
        "岐阜県": 1978742,
        "静岡県": 3633202,
        "愛知県": 7542415,
        "三重県": 1770084,
        "滋賀県": 1413610,
        "京都府": 2578087,
        "大阪府": 8837685,
        "兵庫県": 5465002,
        "奈良県": 1324473,
        "和歌山県": 922584,
        "鳥取県": 553406,
        "島根県": 671126,
        "岡山県": 1888432,
        "広島県": 2799702,
        "山口県": 1342059,
        "徳島県": 719559,
        "香川県": 950244,
        "愛媛県": 1334841,
        "高知県": 691527,
        "福岡県": 5135214,
        "佐賀県": 811696,
        "長崎県": 1312317,
        "熊本県": 1738301,
        "大分県": 1123852,
        "宮崎県": 1069576,
        "鹿児島県": 1588256,
        "沖縄県": 1467480
    }

    # 選択された都道府県の人口を表示するテキスト
    result_text = ft.Text(value="都道府県を選択してください", size=20)

    # ドロップダウンの変更イベントハンドラ
    def dropdown_changed(e):
        selected_prefecture = e.control.value
        if selected_prefecture in population_data:
            population = population_data[selected_prefecture]
            result_text.value = f"{selected_prefecture}の人口は {population:,} 人です"
        else:
            result_text.value = "データがありません"
        page.update()

    # ドロップダウンの作成
    prefecture_dropdown = ft.Dropdown(
        width=200,
        label="都道府県",
        hint_text="都道府県を選択",
        options=[ft.dropdown.Option(pref) for pref in population_data.keys()],
        on_change=dropdown_changed,
    )

    page.add(
        ft.Column(
            [
                ft.Text("都道府県人口チェッカー", size=30, weight=ft.FontWeight.BOLD),
                prefecture_dropdown,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
