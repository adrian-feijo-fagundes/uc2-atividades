import tkinter as tk

import customtkinter as ctk

NOME = "Aldric"
NIVEL = 8
DANO_BASE = 10
ARMADURA_BASE = 20
VIDA_MAX = 100
CUSTO_ESPACOS = 50

MADEIRA = "#3a2314"
PAINEL = "#4b2f1b"
BORDA = "#8c6a3c"
OURO = "#f0c96a"
SLOT = "#2b1a0f"
SLOT_BORDA = "#6e5030"
SLOT_HOVER = "#3d2616"
TEXTO = "#f3e3c0"
TEXTO_MUDO = "#8a7a5e"
PALCO = "#0d3342"
ESCURO = "#1a1208"

SKINS = ["#e8e4d0", "#3d6ea8", "#a83d3d", "#3da869", "#7a3da8"]


def item(nome, tipo, dano=0, armadura=0, cor="#c9ced8", sigla="?", cura=0):
    return {
        "nome": nome,
        "tipo": tipo,
        "dano": dano,
        "armadura": armadura,
        "cor": cor,
        "sigla": sigla,
        "cura": cura,
    }


ITENS = {
    "espada_ferro": item("Espada de ferro", "arma", dano=12, cor="#d7dbe6", sigla="Es"),
    "espada_longa": item("Espada longa", "arma", dano=25, cor="#9fd3ff", sigla="EL"),
    "escudo": item("Escudo de madeira", "escudo", armadura=40, cor="#c98a43", sigla="Ec"),
    "elmo": item("Elmo de aço", "cabeca", armadura=25, cor="#b8bcc8", sigla="El"),
    "ombreiras": item("Ombreiras", "ombro", armadura=20, cor="#a9b0c4", sigla="Om"),
    "peitoral": item("Peitoral de aço", "peito", armadura=60, cor="#c4c8d4", sigla="Pe"),
    "luvas": item("Luvas de couro", "maos", armadura=12, cor="#b98a5a", sigla="Lv"),
    "botas": item("Botas reforçadas", "pes", armadura=15, cor="#a9744a", sigla="Bo"),
    "colar": item("Colar de prata", "pescoco", dano=3, armadura=4, cor="#dfe3ea", sigla="Co"),
    "capa": item("Capa de viagem", "capa", armadura=8, cor="#b5524a", sigla="Ca"),
    "anel_rubi": item("Anel de rubi", "anel", dano=5, cor="#e86a6a", sigla="Ar"),
    "anel_ouro": item("Anel de ouro", "anel", armadura=6, cor="#f0c96a", sigla="Ao"),
    "amuleto": item("Amuleto de jade", "amuleto", dano=2, armadura=10, cor="#7ad9c6", sigla="Am"),
    "pocao": item("Poção de vida", "consumivel", cor="#e86a8a", sigla="Po", cura=30),
    "cenoura": item("Cenoura", "consumivel", cor="#f0a04b", sigla="Ce", cura=5),
    "erva": item("Erva curativa", "consumivel", cor="#8fcf6a", sigla="Er", cura=10),
    "moedas": item("Moedas de ouro", "misc", cor="#f4d35e", sigla="Ou"),
}

ESQUERDA = [
    ("cabeca", "Cabeça"),
    ("ombro", "Ombros"),
    ("peito", "Peito"),
    ("maos", "Mãos"),
    ("pes", "Pés"),
]
DIREITA = [
    ("pescoco", "Pescoço"),
    ("capa", "Capa"),
    ("anel1", "Anel"),
    ("anel2", "Anel"),
    ("amuleto", "Amuleto"),
]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Cavaleiro {NOME}")
        self.geometry("880x640")
        self.resizable(False, False)
        self.configure(fg_color=MADEIRA)

        self.equip = {k: None for k, _ in ESQUERDA + DIREITA}
        self.equip["arma"] = "espada_ferro"
        self.equip["escudo"] = "escudo"
        self.equip["peito"] = "peitoral"

        self.bag = [
            ["espada_longa", 1],
            ["elmo", 1],
            ["ombreiras", 1],
            ["luvas", 1],
            ["botas", 1],
            ["capa", 1],
            ["colar", 1],
            ["anel_rubi", 1],
            ["anel_ouro", 1],
            ["amuleto", 1],
            ["pocao", 3],
            ["cenoura", 11],
            ["erva", 4],
            ["moedas", 120],
        ]
        self.bag += [None] * (40 - len(self.bag))

        self.vida = 60
        self.skin = 0
        self.msg = "Clique em um item da mochila para equipar ou usar."
        self.botoes_slot = {}
        self.botoes_bag = []

        self.montar()
        self.atualizar()

    def montar(self):
        cab = ctk.CTkFrame(self, fg_color=PAINEL, border_color=BORDA, border_width=2, corner_radius=10)
        cab.pack(fill="x", padx=14, pady=(14, 8))
        ctk.CTkLabel(
            cab,
            text=f"Cavaleiro {NOME} - Nível {NIVEL}",
            font=("Georgia", 26, "bold"),
            text_color=OURO,
        ).pack(pady=(8, 2))
        linha = ctk.CTkFrame(cab, fg_color="transparent")
        linha.pack(pady=(0, 10))
        self.lbl_vida = ctk.CTkLabel(linha, text="", font=("Arial", 13), text_color=TEXTO)
        self.lbl_vida.pack(side="left", padx=(0, 10))
        self.barra = ctk.CTkProgressBar(linha, width=280, height=12, progress_color="#c0392b", fg_color=SLOT)
        self.barra.pack(side="left")

        self.status = ctk.CTkLabel(self, text=self.msg, font=("Arial", 13), text_color=TEXTO, anchor="w")
        self.status.pack(side="bottom", fill="x", padx=20, pady=(4, 10))

        corpo = ctk.CTkFrame(self, fg_color="transparent")
        corpo.pack(fill="both", expand=True, padx=14)

        esq = ctk.CTkFrame(corpo, fg_color=PAINEL, border_color=BORDA, border_width=2, corner_radius=10)
        esq.pack(side="left", fill="y")
        dire = ctk.CTkFrame(corpo, fg_color=PAINEL, border_color=BORDA, border_width=2, corner_radius=10)
        dire.pack(side="left", fill="both", expand=True, padx=(10, 0))

        for i, (chave, rotulo) in enumerate(ESQUERDA):
            self.criar_slot(esq, chave, rotulo).grid(row=i, column=0, padx=(10, 4), pady=4)
        for i, (chave, rotulo) in enumerate(DIREITA):
            self.criar_slot(esq, chave, rotulo).grid(row=i, column=2, padx=(4, 10), pady=4)

        self.tela = tk.Canvas(esq, width=230, height=300, bg=PALCO, highlightthickness=2, highlightbackground=SLOT_BORDA)
        self.tela.grid(row=0, column=1, rowspan=5, padx=4, pady=(10, 4))

        est = ctk.CTkFrame(esq, fg_color="transparent")
        est.grid(row=5, column=1, pady=(2, 0))
        self.lbl_dano = self.criar_stat(est, "DANO", 0)
        self.lbl_arm = self.criar_stat(est, "ARMADURA", 1)

        self.criar_slot(esq, "arma", "Arma", tam=68).grid(row=6, column=0, padx=(10, 4), pady=(2, 10))
        self.criar_slot(esq, "escudo", "Escudo", tam=68).grid(row=6, column=2, padx=(4, 10), pady=(2, 10))

        botoes = ctk.CTkFrame(esq, fg_color="transparent")
        botoes.grid(row=6, column=1, pady=(2, 10))
        ctk.CTkButton(botoes, text="Skins", width=100, fg_color="#1f6f8b", hover_color="#2a8aa8", command=self.trocar_skin).pack(side="left", padx=4)
        ctk.CTkButton(botoes, text="Atributos", width=100, fg_color="#1f6f8b", hover_color="#2a8aa8", command=self.abrir_atributos).pack(side="left", padx=4)

        ctk.CTkLabel(dire, text="Mochila", font=("Georgia", 20, "bold"), text_color=OURO).pack(pady=(10, 4))
        self.grade = ctk.CTkScrollableFrame(dire, width=270, height=380, fg_color=MADEIRA, corner_radius=8)
        self.grade.pack(fill="both", expand=True, padx=10)
        ctk.CTkButton(
            dire,
            text=f"Adicionar 5 espaços: {CUSTO_ESPACOS} moedas",
            fg_color="#6b4e2e",
            hover_color="#85623a",
            text_color=TEXTO,
            command=self.adicionar_espacos,
        ).pack(pady=10, padx=10, fill="x")
        self.montar_bag()

    def criar_stat(self, pai, rotulo, col):
        ctk.CTkLabel(pai, text=rotulo, font=("Georgia", 13, "bold"), text_color="#e8d6a8").grid(row=0, column=col, padx=18)
        lbl = ctk.CTkLabel(pai, text="0", font=("Georgia", 26, "bold"), text_color=OURO)
        lbl.grid(row=1, column=col)
        return lbl

    def criar_slot(self, pai, chave, rotulo, tam=56):
        btn = ctk.CTkButton(
            pai,
            width=tam,
            height=tam,
            text="",
            corner_radius=8,
            border_width=2,
            border_color=SLOT_BORDA,
            fg_color=SLOT,
            hover_color=SLOT_HOVER,
            font=("Arial", 10),
            command=lambda: self.clicar_slot(chave),
        )
        btn.bind("<Enter>", lambda e: self.dica_slot(chave), add="+")
        btn.bind("<Leave>", lambda e: self.dica(self.msg), add="+")
        self.botoes_slot[chave] = (btn, rotulo)
        return btn

    def montar_bag(self):
        for w in self.grade.winfo_children():
            w.destroy()
        self.botoes_bag = []
        for i in range(len(self.bag)):
            b = ctk.CTkButton(
                self.grade,
                width=48,
                height=48,
                text="",
                corner_radius=6,
                border_width=2,
                border_color=SLOT_BORDA,
                fg_color=SLOT,
                hover_color=SLOT_HOVER,
                font=("Arial", 11, "bold"),
                command=lambda i=i: self.clicar_bag(i),
            )
            b.grid(row=i // 5, column=i % 5, padx=3, pady=3)
            b.bind("<Enter>", lambda e, i=i: self.dica_bag(i), add="+")
            b.bind("<Leave>", lambda e: self.dica(self.msg), add="+")
            self.botoes_bag.append(b)

    def dano(self):
        return DANO_BASE + sum(ITENS[v]["dano"] for v in self.equip.values() if v)

    def armadura(self):
        return ARMADURA_BASE + sum(ITENS[v]["armadura"] for v in self.equip.values() if v)

    def descricao(self, id_):
        d = ITENS[id_]
        partes = []
        if d["dano"]:
            partes.append(f"Dano +{d['dano']}")
        if d["armadura"]:
            partes.append(f"Armadura +{d['armadura']}")
        if d["cura"]:
            partes.append(f"Cura {d['cura']}")
        return f"{d['nome']} - " + (", ".join(partes) if partes else "item de troca")

    def avisar(self, texto):
        self.msg = texto
        self.status.configure(text=texto)

    def dica(self, texto):
        self.status.configure(text=texto)

    def dica_slot(self, chave):
        id_ = self.equip[chave]
        if id_:
            self.dica(self.descricao(id_) + " (clique para guardar)")
        else:
            self.dica(f"Espaço vazio: {self.botoes_slot[chave][1]}")

    def dica_bag(self, i):
        entrada = self.bag[i]
        if entrada:
            self.dica(self.descricao(entrada[0]))

    def destino(self, tipo):
        if tipo == "anel":
            if not self.equip["anel1"]:
                return "anel1"
            if not self.equip["anel2"]:
                return "anel2"
            return "anel1"
        return tipo

    def clicar_bag(self, i):
        entrada = self.bag[i]
        if not entrada:
            return
        id_, _ = entrada
        d = ITENS[id_]
        if d["tipo"] == "consumivel":
            if self.vida >= VIDA_MAX:
                self.avisar("Sua vida já está cheia.")
                return
            self.vida = min(VIDA_MAX, self.vida + d["cura"])
            entrada[1] -= 1
            if entrada[1] <= 0:
                self.bag[i] = None
            self.avisar(f"Você usou {d['nome']}: +{d['cura']} de vida.")
        elif d["tipo"] == "misc":
            self.avisar(f"{d['nome']}: servem para ampliar a mochila.")
        else:
            slot = self.destino(d["tipo"])
            antigo = self.equip[slot]
            self.equip[slot] = id_
            self.bag[i] = [antigo, 1] if antigo else None
            self.avisar(f"{d['nome']} equipado.")
        self.atualizar()

    def clicar_slot(self, chave):
        id_ = self.equip[chave]
        if not id_:
            return
        livre = next((i for i, v in enumerate(self.bag) if v is None), None)
        if livre is None:
            self.avisar("Mochila cheia. Libere espaço ou adicione mais.")
            return
        self.bag[livre] = [id_, 1]
        self.equip[chave] = None
        self.avisar(f"{ITENS[id_]['nome']} guardado na mochila.")
        self.atualizar()

    def adicionar_espacos(self):
        idx = next((i for i, v in enumerate(self.bag) if v and v[0] == "moedas"), None)
        if idx is None or self.bag[idx][1] < CUSTO_ESPACOS:
            self.avisar(f"Você precisa de {CUSTO_ESPACOS} moedas para ampliar a mochila.")
            return
        self.bag[idx][1] -= CUSTO_ESPACOS
        if self.bag[idx][1] <= 0:
            self.bag[idx] = None
        self.bag += [None] * 5
        self.montar_bag()
        self.avisar("Mochila ampliada em 5 espaços.")
        self.atualizar()

    def trocar_skin(self):
        self.skin = (self.skin + 1) % len(SKINS)
        self.avisar("Skin alterada.")
        self.desenhar()

    def abrir_atributos(self):
        jan = ctk.CTkToplevel(self)
        jan.title("Atributos")
        jan.geometry("320x300")
        jan.configure(fg_color=MADEIRA)
        jan.transient(self)
        jan.after(150, jan.focus)
        linhas = [
            ("Nível", NIVEL),
            ("Vida", f"{self.vida}/{VIDA_MAX}"),
            ("Dano base", DANO_BASE),
            ("Bônus de dano", f"+{self.dano() - DANO_BASE}"),
            ("Dano total", self.dano()),
            ("Armadura base", ARMADURA_BASE),
            ("Bônus de armadura", f"+{self.armadura() - ARMADURA_BASE}"),
            ("Armadura total", self.armadura()),
        ]
        jan.grid_columnconfigure(0, weight=1)
        jan.grid_columnconfigure(1, weight=1)
        for r, (nome, valor) in enumerate(linhas):
            destaque = nome.endswith("total")
            cor = OURO if destaque else TEXTO
            fonte = ("Georgia", 16, "bold") if destaque else ("Arial", 14)
            ctk.CTkLabel(jan, text=nome, font=fonte, text_color=cor, anchor="w").grid(row=r, column=0, padx=(24, 8), pady=6, sticky="w")
            ctk.CTkLabel(jan, text=str(valor), font=fonte, text_color=cor, anchor="e").grid(row=r, column=1, padx=(8, 24), pady=6, sticky="e")

    def desenhar(self):
        c = self.tela
        c.delete("all")
        contorno = "#2a1a0f"
        c.create_oval(25, 245, 205, 292, fill="#0a2a37", outline="")
        c.create_rectangle(86, 222, 110, 262, fill="#5b3a1e", outline=contorno)
        c.create_rectangle(120, 222, 144, 262, fill="#5b3a1e", outline=contorno)
        c.create_rectangle(88, 180, 108, 226, fill="#7d8190", outline=contorno)
        c.create_rectangle(122, 180, 142, 226, fill="#7d8190", outline=contorno)
        c.create_rectangle(80, 112, 150, 196, fill=SKINS[self.skin], outline=contorno, width=2)
        c.create_line(80, 172, 150, 172, fill="#6b4e2e", width=4)
        if self.equip["peito"]:
            c.create_rectangle(88, 118, 142, 168, fill="#c4c8d4", outline=contorno, width=2)
            c.create_line(115, 118, 115, 168, fill="#8f95a6", width=2)
        c.create_rectangle(68, 126, 84, 190, fill="#9aa0b0", outline=contorno)
        c.create_rectangle(146, 126, 162, 190, fill="#9aa0b0", outline=contorno)
        c.create_oval(62, 106, 96, 138, fill="#b8bcc8", outline=contorno)
        c.create_oval(134, 106, 168, 138, fill="#b8bcc8", outline=contorno)
        c.create_oval(97, 66, 133, 108, fill="#d9a679", outline=contorno)
        c.create_oval(105, 84, 110, 89, fill=contorno, outline="")
        c.create_oval(120, 84, 125, 89, fill=contorno, outline="")
        if self.equip["cabeca"]:
            c.create_arc(94, 60, 136, 104, start=0, extent=180, style="chord", fill="#c4c8d4", outline=contorno, width=2)
            c.create_rectangle(113, 76, 117, 100, fill="#c4c8d4", outline="")
        else:
            c.create_arc(95, 62, 135, 100, start=0, extent=180, style="chord", fill="#5a3b20", outline="")
        if self.equip["escudo"]:
            c.create_oval(127, 122, 203, 198, fill="#7a4a22", outline="#aeb4c4", width=4)
            c.create_line(165, 122, 165, 198, fill="#aeb4c4", width=4)
            c.create_line(127, 160, 203, 160, fill="#aeb4c4", width=4)
        if self.equip["arma"]:
            c.create_line(64, 160, 63, 178, fill="#6b4e2e", width=7)
            c.create_line(52, 182, 78, 178, fill=OURO, width=5)
            c.create_line(65, 182, 52, 264, fill="#d7dbe6", width=7)

    def atualizar(self):
        for chave, (btn, rotulo) in self.botoes_slot.items():
            id_ = self.equip[chave]
            if id_:
                d = ITENS[id_]
                btn.configure(
                    text=d["sigla"],
                    fg_color=d["cor"],
                    hover_color=d["cor"],
                    text_color=ESCURO,
                    border_color=OURO,
                    font=("Arial", 16, "bold"),
                )
            else:
                btn.configure(
                    text=rotulo,
                    fg_color=SLOT,
                    hover_color=SLOT_HOVER,
                    text_color=TEXTO_MUDO,
                    border_color=SLOT_BORDA,
                    font=("Arial", 10),
                )
        for i, btn in enumerate(self.botoes_bag):
            entrada = self.bag[i]
            if entrada:
                d = ITENS[entrada[0]]
                texto = d["sigla"] + (f"\n×{entrada[1]}" if entrada[1] > 1 else "")
                btn.configure(text=texto, fg_color=d["cor"], hover_color=d["cor"], text_color=ESCURO)
            else:
                btn.configure(text="", fg_color=SLOT, hover_color=SLOT_HOVER)
        self.lbl_dano.configure(text=str(self.dano()))
        self.lbl_arm.configure(text=str(self.armadura()))
        self.lbl_vida.configure(text=f"Vida {self.vida}/{VIDA_MAX}")
        self.barra.set(self.vida / VIDA_MAX)
        self.desenhar()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    App().mainloop()