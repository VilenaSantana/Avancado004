from fpdf import FPDF

# Criando o conteúdo do PDF
titulo = "Cursos Gratuitos de Tecnologia – Softex Recife/PE"
conteudo = """
A Softex Pernambuco está com diversas oportunidades incríveis de cursos gratuitos na área de tecnologia! Confira:

Formação Acelerada em Programação (FAP)
Capacitação em Front-end e Back-end, com aulas online e presenciais.
- Linguagens como JavaScript, HTML, CSS, React JS e Node.js.
- Aulas em Recife, Caruaru, Garanhuns e Petrolina.
Inscreva-se: https://clovesrocha.github.io/softex

Cursos de Inteligência Artificial
Parceria com a Microsoft! Com certificado e totalmente online.
- Inclui IA Generativa, Fundamentos do Azure, e muito mais.
Acesse: https://softex.br/escola-do-trabalhador-4-0-e-microsoft-oferecem-cursos-gratuitos-em-inteligencia-artificial

Tech Kids
Oficinas para crianças com robótica e criação digital. Gratuito e divertido!
Veja a programação: https://softexpe.org.br/agenda

Mais informações: (81) 3224-4251
Site oficial: https://softexpe.org.br

Não perca essa chance de entrar no mundo da tecnologia!
"""

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, titulo)

pdf.set_font("Arial", '', 12)
pdf.ln(5)
pdf.multi_cell(0, 10, conteudo)

# Salvando o PDF
pdf.output("Cursos_Gratuitos_Softex_Recife.pdf")
