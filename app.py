
 !pip install gradio
# ============================================================
# 🐾 SORTEADOR DE NOMES DE PETS
# Google Colab + Python + Gradio
# ============================================================

# 1️⃣ INSTALAR O GRADIO
# O Gradio é a biblioteca que cria nossa interface visual.
!pip install -q gradio


# ============================================================
# 2️⃣ IMPORTAR AS BIBLIOTECAS
# ============================================================

import gradio as gr
import random


# ============================================================
# 3️⃣ BANCO DE NOMES
# ============================================================

# Cada categoria possui uma lista de nomes.

nomes = {

    "🐶 Cachorro": {

        "💕 Fofo": {
            "♂️ Macho": ["Bento", "Theo", "Toby", "Pipoca", "Nino", "Chico"],
            "♀️ Fêmea": ["Luna", "Mel", "Amora", "Nina", "Pérola", "Mimi"]
        },

        "💪 Forte": {
            "♂️ Macho": ["Thor", "Zeus", "Rex", "Apolo", "Bruce", "Rocky"],
            "♀️ Fêmea": ["Athena", "Hera", "Jade", "Ravena", "Íris", "Diana"]
        },

        "👤 Humano": {
            "♂️ Macho": ["Miguel", "Arthur", "Lucas", "Pedro", "Gabriel", "Heitor"],
            "♀️ Fêmea": ["Helena", "Alice", "Laura", "Clara", "Sofia", "Manuela"]
        }
    },


    "🐱 Gato": {

        "💕 Fofo": {
            "♂️ Macho": ["Milo", "Tom", "Nino", "Pudim", "Tico", "Biscoito"],
            "♀️ Fêmea": ["Mia", "Luna", "Mel", "Nala", "Lili", "Amora"]
        },

        "💪 Forte": {
            "♂️ Macho": ["Thor", "Zeus", "Simba", "Ragnar", "Atlas", "Hércules"],
            "♀️ Fêmea": ["Athena", "Freya", "Hera", "Jade", "Xena", "Gaia"]
        },

        "👤 Humano": {
            "♂️ Macho": ["João", "Carlos", "Miguel", "Lucas", "Rafael", "Daniel"],
            "♀️ Fêmea": ["Ana", "Julia", "Laura", "Clara", "Marina", "Beatriz"]
        }
    },


    "🐰 Coelho": {

        "💕 Fofo": {
            "♂️ Macho": ["Floquinho", "Pompom", "Tutu", "Nino", "Pipoca", "Bidu"],
            "♀️ Fêmea": ["Lili", "Mimi", "Mel", "Pérola", "Nuvem", "Belinha"]
        },

        "💪 Forte": {
            "♂️ Macho": ["Thor", "Max", "Rocky", "Bolt", "Trovão", "Hunter"],
            "♀️ Fêmea": ["Jade", "Ravena", "Gaia", "Diana", "Athena", "Hera"]
        },

        "👤 Humano": {
            "♂️ Macho": ["Theo", "Lucas", "Pedro", "João", "Arthur", "Davi"],
            "♀️ Fêmea": ["Alice", "Laura", "Sofia", "Clara", "Helena", "Julia"]
        }
    },


    "🐹 Hamster": {

        "💕 Fofo": {
            "♂️ Macho": ["Pipoca", "Pudim", "Biscoito", "Tico", "Toby", "Cookie"],
            "♀️ Fêmea": ["Mel", "Mimi", "Luna", "Nina", "Lili", "Amora"]
        },

        "💪 Forte": {
            "♂️ Macho": ["Thor", "Rex", "Bolt", "Max", "Rocky", "Zeus"],
            "♀️ Fêmea": ["Jade", "Xena", "Gaia", "Hera", "Freya", "Diana"]
        },

        "👤 Humano": {
            "♂️ Macho": ["Lucas", "Theo", "Miguel", "Davi", "Arthur", "João"],
            "♀️ Fêmea": ["Alice", "Laura", "Julia", "Sofia", "Clara", "Ana"]
        }
    },


    "🐦 Pássaro": {

        "💕 Fofo": {
            "♂️ Macho": ["Pipoca", "Tico", "Tutu", "Nino", "Piu", "Bento"],
            "♀️ Fêmea": ["Lili", "Mel", "Mimi", "Luna", "Nina", "Amora"]
        },

        "💪 Forte": {
            "♂️ Macho": ["Thor", "Zeus", "Apolo", "Rex", "Bolt", "Hunter"],
            "♀️ Fêmea": ["Athena", "Gaia", "Jade", "Íris", "Diana", "Freya"]
        },

        "👤 Humano": {
            "♂️ Macho": ["Pedro", "Lucas", "Miguel", "Arthur", "Davi", "Gabriel"],
            "♀️ Fêmea": ["Ana", "Clara", "Julia", "Laura", "Sofia", "Helena"]
        }
    }
}


# ============================================================
# 4️⃣ FUNÇÃO QUE FAZ O SORTEIO
# ============================================================

def gerar_nome(pet, tipo_nome, sexo):

    # Procura os nomes correspondentes às escolhas.
    lista = nomes[pet][tipo_nome][sexo]

    # Escolhe aleatoriamente um nome.
    nome = random.choice(lista)

    # Mensagem que aparecerá para o usuário.
    return f"""
    <div class="resultado">
        <div class="pata">🐾</div>
        <div class="titulo-resultado">✨ O nome do seu pet é ✨</div>
        <div class="nome">{nome}</div>
        <div class="pata">🐾</div>
    </div>
    """


# ============================================================
# 5️⃣ CSS — PARTE VISUAL
# ============================================================

css = """

/* Fundo geral */
body {
    background: linear-gradient(
        135deg,
        #ffe1ec 0%,
        #ffffff 45%,
        #dcecff 100%
    );
}

/* Área principal */
.gradio-container {
    max-width: 900px !important;
    margin: auto !important;
    background: linear-gradient(
        135deg,
        #fff0f6,
        #eef6ff
    );
    border-radius: 30px;
    padding: 30px !important;
}

/* Título */
.titulo-principal {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #d63384;
    margin-bottom: 5px;
}

/* Subtítulo */
.subtitulo {
    text-align: center;
    color: #5271a5;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Caixa das opções */
.caixa {
    background: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 5px 20px rgba(100,100,150,0.12);
}

/* Botão */
.gerar {
    background: linear-gradient(
        90deg,
        #e83e8c,
        #4d9de0
    ) !important;

    color: white !important;
    font-size: 22px !important;
    font-weight: bold !important;
    border-radius: 18px !important;
    border: none !important;
    padding: 15px !important;
}

/* Resultado */
.resultado {
    text-align: center;
    background: linear-gradient(
        135deg,
        #fff5fa,
        #eef7ff
    );
    border: 3px solid #f3a6c8;
    border-radius: 25px;
    padding: 30px;
    margin-top: 15px;
}

/* Nome */
.nome {
    font-size: 50px;
    font-weight: bold;
    color: #4d75b9;
    margin: 15px;
}

/* Texto do resultado */
.titulo-resultado {
    font-size: 22px;
    color: #d63384;
    font-weight: bold;
}

/* Patinhas */
.pata {
    font-size: 35px;
    margin: 5px;
}


/* PATINHAS DECORATIVAS */

.gradio-container::before {
    content: "🐾       🐾          🐾       🐾";
    display: block;
    text-align: center;
    font-size: 28px;
    opacity: 0.45;
    margin-bottom: 10px;
}

.gradio-container::after {
    content: "🐾    🐾        🐾       🐾    🐾";
    display: block;
    text-align: center;
    font-size: 28px;
    opacity: 0.35;
    margin-top: 20px;
}


/* Rodapé */
.rodape {
    text-align: center;
    color: #777;
    font-size: 14px;
    margin-top: 20px;
}

"""


# ============================================================
# 6️⃣ CRIAR A INTERFACE
# ============================================================

with gr.Blocks(
    css=css,
    title="🐾 Sorteador de Nomes de Pets"
) as app:

    # Título
    gr.HTML("""
        <div class="titulo-principal">
            🐾 Sorteador de Nomes de Pets 🐾
        </div>

        <div class="subtitulo">
            Encontre o nome perfeito para seu novo companheiro! 💕
        </div>
    """)


    # Caixa com as opções
    with gr.Column(elem_classes="caixa"):

        pet = gr.Dropdown(
            choices=list(nomes.keys()),
            label="🐾 Qual é o seu pet?",
            value="🐶 Cachorro"
        )


        tipo_nome = gr.Dropdown(
            choices=[
                "💕 Fofo",
                "💪 Forte",
                "👤 Humano"
            ],
            label="✨ Qual tipo de nome você quer?",
            value="💕 Fofo"
        )


        sexo = gr.Radio(
            choices=[
                "♂️ Macho",
                "♀️ Fêmea"
            ],
            label="💗 Seu pet é...",
            value="♂️ Macho"
        )


        botao = gr.Button(
            "🎲 GERAR NOME",
            elem_classes="gerar"
        )


    # Resultado
    resultado = gr.HTML(
        value="""
        <div class="resultado">
            <div class="pata">🐾</div>
            <div class="titulo-resultado">
                Seu nome aparecerá aqui!
            </div>
            <div class="pata">🐾</div>
        </div>
        """
    )


    # Rodapé
    gr.HTML("""
        <div class="rodape">
            Feito com 🐾, Python e Gradio
        </div>
    """)


    # Quando clicar no botão, executa gerar_nome()
    botao.click(
        fn=gerar_nome,
        inputs=[pet, tipo_nome, sexo],
        outputs=resultado
    )


# ============================================================
# 7️⃣ ABRIR A INTERFACE
# ============================================================

app.launch(share=True)
