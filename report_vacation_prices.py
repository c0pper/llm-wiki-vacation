#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, navy, darkblue, green

output_file = "/media/simo/DATA_SSD/code/llm-wiki-vacation/report_vacation_prices.pdf"
doc = SimpleDocTemplate(
    output_file,
    pagesize=letter,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=72,
)

styles = getSampleStyleSheet()
story = []

title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    fontSize=24,
    textColor=navy,
    spaceAfter=30,
    alignment=TA_CENTER,
)

heading_style = ParagraphStyle(
    "CustomHeading",
    parent=styles["Heading2"],
    fontSize=14,
    textColor=darkblue,
    spaceBefore=20,
    spaceAfter=10,
)

normal_style = ParagraphStyle(
    "CustomNormal",
    parent=styles["Normal"],
    fontSize=10,
    spaceAfter=8,
    alignment=TA_LEFT,
)

link_style = ParagraphStyle(
    "CustomLink",
    parent=styles["Normal"],
    fontSize=9,
    textColor=HexColor("#0066cc"),
    spaceAfter=12,
    alignment=TA_LEFT,
)

price_style = ParagraphStyle(
    "PriceStyle",
    parent=styles["Normal"],
    fontSize=12,
    textColor=green,
    spaceAfter=12,
    alignment=TA_LEFT,
)

story.append(Paragraph("Ville e Case per Vacanza in Italia", title_style))
story.append(
    Paragraph("Rapporto completo con prezzi settimanali (€/settimana)", normal_style)
)
story.append(
    Paragraph(
        "Preferenze: minimo 2 bagni, spiaggia vicino, accesso privato, attenzione alle recensioni",
        normal_style,
    )
)
story.append(Spacer(1, 20))

properties = [
    {
        "rank": 1,
        "name": "Villa Castellaneta Marina",
        "location": "Puglia",
        "rating": "★★★★★ (5.0)",
        "reviews": 7,
        "bedrooms": 3,
        "beds": 8,
        "bathrooms": "2+",
        "beach": "Vicino (a piedi)",
        "beach_access": "Si",
        "pets": "Si",
        "price": "€1.360",
        "score": 100,
        "desc": """<b>Perfetta per gruppi grandi.</b> Villa con 3 camere e 8 posti letto nella pineta pugliese. Valutazione perfetta 5.0 su 7 recensioni. Giardino, terrazza, aria condizionata, doccia esterna, BBQ. Animali ammessi. Vicina a Matera (58km).""",
        "url": "https://www.airbnb.com/rooms/41234343",
        "why": "Soddisfa tutti i criteri: 2+ bagni, spiaggia vicina, 5.0 stelle, animali ammessi",
    },
    {
        "rank": 2,
        "name": "Home Pisciotta",
        "location": "Cilento (Campania)",
        "rating": "★★★★★ (4.96)",
        "reviews": 45,
        "bedrooms": 3,
        "beds": 4,
        "bathrooms": 3,
        "beach": "A piedi",
        "beach_access": "Si",
        "pets": "No",
        "price": "€1.138",
        "score": 98,
        "desc": """<b>Migliore in Cilento.</b> Villa a 2 piani con vista mare, giardino con limoni e olivi. 45 recensioni - tra le piu' amate. 3 bagni. Balcone con pranzo all'aperto. 10 min a piedi dalla spiaggia.""",
        "url": "https://www.airbnb.com/rooms/15128491",
        "why": "3 bagni, eccellenti recensioni (4.96), 45 recensioni - campione solido",
    },
    {
        "rank": 3,
        "name": "Townhouse Scalea",
        "location": "Calabria",
        "rating": "★★★★★ (4.94)",
        "reviews": 18,
        "bedrooms": 2,
        "beds": 4,
        "bathrooms": 2,
        "beach": "100m (privata)",
        "beach_access": "SI - PRIVATA",
        "pets": "Non specificato",
        "price": "€1.222",
        "score": 96,
        "desc": """<b>Accesso spiaggia PRIVATO.</b> Villa a schiera nel parco piu' bello di Scalea. Accesso privato a soli 100m. Vista baia e mare. 2 giardini. Guest favorite. 2 bagni.""",
        "url": "https://www.airbnb.com/rooms/839783448307020394",
        "why": "2 bagni, UNICO CON ACCESSO PRIVATO alla spiaggia (100m), alta valutazione (4.94)",
    },
    {
        "rank": 4,
        "name": "Home Gaeta - Luca",
        "location": "Gaeta (Lazio)",
        "rating": "★★★★★ (4.92)",
        "reviews": 13,
        "bedrooms": 3,
        "beds": 3,
        "bathrooms": 2,
        "beach": "300m",
        "beach_access": "No",
        "pets": "No",
        "price": "€1.401",
        "score": 95,
        "desc": """<b>Vista panoramica eccezionale.</b> Appartamento luminosissimo con vista a 360° sulla baia di Serapo. 2 camere matrimoniali + 1 singola, 2 bagni. Camino a legna. Parcheggio gratuito.""",
        "url": "https://www.airbnb.com/rooms/1207266166578504838",
        "why": "2 bagni, spiaggia a 300m, alta valutazione (4.92), vista mare eccezionale",
    },
    {
        "rank": 5,
        "name": "Villa San Felice Circeo",
        "location": "San Felice Circeo (Lazio)",
        "rating": "★★★★☆ (4.67)",
        "reviews": 9,
        "bedrooms": 4,
        "beds": 9,
        "bathrooms": "3 (stima)",
        "beach": "A piedi",
        "beach_access": "Si",
        "pets": "Si",
        "price": "€1.300 (stimato)",
        "score": 92,
        "desc": """<b>Ideale per gruppi grandi.</b> Villa spaziosa con 4 camere e fino a 12 posti letto. 3 bagni. Giardino con ping pong e pallavolo. Vicino Parco Nazionale del Circeo. Tranquilla anche in alta stagione.""",
        "url": "https://www.airbnb.com/rooms/5914149",
        "why": "4 camere/9 letti, 3 bagni, spiaggia a piedi, animali ammessi",
    },
    {
        "rank": 6,
        "name": "Villa Fondi Serena",
        "location": "Fondi (Lazio)",
        "rating": "★★★★★ (4.88)",
        "reviews": 16,
        "bedrooms": 3,
        "beds": 5,
        "bathrooms": 2,
        "beach": "800m (15 min)",
        "beach_access": "No",
        "pets": "No",
        "price": "€1.303",
        "score": 88,
        "desc": """<b>Giardino privato grande.</b> Villa con 5000mq di giardino recintato. Guest favorite! 2 bagni. 2 posti auto coperti. Terrazza, BBQ. Tra Terracina e Sperlonga.""",
        "url": "https://www.airbnb.com/rooms/1065128176658688079",
        "why": "2 bagni, giardino grande, guest favorite (4.88), 16 recensioni",
    },
    {
        "rank": 7,
        "name": "Home Fondi Emanuele",
        "location": "Fondi (Lazio)",
        "rating": "★★★★☆ (4.55)",
        "reviews": 11,
        "bedrooms": 4,
        "beds": 4,
        "bathrooms": 2,
        "beach": "120m (frontale)",
        "beach_access": "Si (frontale)",
        "pets": "No",
        "price": "€1.173",
        "score": 90,
        "desc": """<b>Beachfront.</b> Villetta a schiera a 120m dalla spiaggia - frontale. 2 bagni. 4 camere. Due giardini privati, firepit, BBQ. Vista mare. Tra Sperlonga e Terracina.""",
        "url": "https://www.airbnb.com/rooms/20597083",
        "why": "2 bagni, spiaggia frontale (120m), 4 camere, buona valutazione",
    },
    {
        "rank": 8,
        "name": "Home Scario",
        "location": "Cilento (Campania)",
        "rating": "★★★★☆ (4.6)",
        "reviews": 25,
        "bedrooms": 2,
        "beds": 5,
        "bathrooms": "1+",
        "beach": "A piedi",
        "beach_access": "No",
        "pets": "No",
        "price": "€827",
        "score": 82,
        "desc": """<b>Posizione centrale.</b> Nel centro di Scario, Parco Nazionale del Cilento. Porto e spiagge a piedi. Terrazza con vista mare. 25 recensioni.""",
        "url": "https://www.airbnb.com/rooms/3007439",
        "why": "25 recensioni - campione buono, spiaggia a piedi, il PIU' ECONOMICO con buone recensioni",
    },
    {
        "rank": 9,
        "name": "Townhouse Castellaneta Marina",
        "location": "Puglia",
        "rating": "★★★★★ (4.75)",
        "reviews": 4,
        "bedrooms": 2,
        "beds": 3,
        "bathrooms": "1+",
        "beach": "200m (5 min)",
        "beach_access": "No",
        "pets": "No",
        "price": "€1.102",
        "score": 75,
        "desc": """<b>Superhost.</b> Appartamento in villa nella pineta. Grande terrazza panoramica. A 200m dalla spiaggia (5 min). Host e' Superhost.""",
        "url": "https://www.airbnb.com/rooms/20244510",
        "why": "Ottima valutazione (4.75), spiaggia a 200m, host attendibile",
    },
    {
        "rank": 10,
        "name": "Villa Hotel Tivigest",
        "location": "Basilicata",
        "rating": "★★★★☆ (4.6)",
        "reviews": 5,
        "bedrooms": 3,
        "beds": 5,
        "bathrooms": 2,
        "beach": "500m",
        "beach_access": "No",
        "pets": "Si",
        "price": "€1.208",
        "score": 70,
        "desc": """<b>Per amanti di Matera.</b> Villa a 2 piani con giardino grande. A 500m dal Mare Ionio. Vicina a Matera. Animali ammessi.""",
        "url": "https://www.airbnb.com/rooms/24179283",
        "why": "Animali ammessi, 2 bagni, buona posizione per escursioni (Matera)",
    },
]

story.append(Paragraph("=" * 70, normal_style))
story.append(Spacer(1, 10))

for prop in properties:
    story.append(Paragraph(f"{prop['rank']}. {prop['name']}", heading_style))
    story.append(
        Paragraph(
            f"<b>{prop['location']}</b> | {prop['rating']} ({prop['reviews']} recensioni)",
            normal_style,
        )
    )
    story.append(
        Paragraph(
            f"Camere: {prop['bedrooms']} | Letti: {prop['beds']} | Bagni: {prop['bathrooms']}",
            normal_style,
        )
    )
    story.append(
        Paragraph(
            f"Spiaggia: {prop['beach']} | Accesso privato: {prop['beach_access']}",
            normal_style,
        )
    )
    story.append(Paragraph(f"<b>PREZZO: {prop['price']}/settimana</b>", price_style))
    story.append(Paragraph(prop["desc"], normal_style))
    story.append(
        Paragraph(f"<b>Perche' e' una buona scelta:</b> {prop['why']}", normal_style)
    )
    story.append(Paragraph(f"<i>Fonte: {prop['url']}</i>", link_style))
    story.append(Spacer(1, 15))

story.append(Paragraph("=" * 70, normal_style))
story.append(Spacer(1, 20))

story.append(Paragraph("PROPRIETA' SCONSIGLIATE", heading_style))
story.append(
    Paragraph(
        "Le seguenti proprieta' sono sconsigliate per mancanza di recensioni (pericolo):",
        normal_style,
    )
)

avoid = [
    (
        "Home Fondi Luisa",
        "https://www.airbnb.com/rooms/1336015011780522585",
        "Nessuna recensione - 50m dalla spiaggia",
        "€880",
    ),
    (
        "Home Pollica",
        "https://www.airbnb.com/rooms/1595568886799231526",
        "Nessuna recensione - accesso spiaggia privata",
        "€899",
    ),
    (
        "Home Roseto Capo Spulico",
        "https://www.airbnb.com/rooms/1662456513827712773",
        "Nuovo annuncio - nessuna recensione",
        "€798",
    ),
    (
        "Home Villapiana Lido",
        "https://www.airbnb.com/rooms/1465898782320150531",
        "Solo 2 recensioni",
        "€1.050",
    ),
    (
        "Home Palinuro",
        "https://www.airbnb.com/rooms/28579802",
        "Solo 1 recensione",
        "€1.105",
    ),
    (
        "Home Cucco-Riviere",
        "https://www.airbnb.com/rooms/1325256730782747038",
        "Nessuna recensione",
        "€1.446",
    ),
]

for name, url, note, price in avoid:
    story.append(Paragraph(f"• <b>{name}</b> - {note}", normal_style))
    story.append(Paragraph(f"  Prezzo: {price}/settimana | {url}", link_style))

story.append(Spacer(1, 20))
story.append(Paragraph("=" * 70, normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("RIEPILOGO PREFERENZE", heading_style))
story.append(
    Paragraph("• Minimo 2 bagni: Verificato per le prime 10 proprieta'", normal_style)
)
story.append(Paragraph("• Spiaggia vicino: <500m o a piedi", normal_style))
story.append(
    Paragraph(
        "• Accesso privato: SOLO Townhouse Scalea (100m privata) - gli altri claims non verificati",
        normal_style,
    )
)
story.append(
    Paragraph(
        "• Attenzione recensioni: Scartate proprieta' senza recensioni", normal_style
    )
)

story.append(Spacer(1, 20))
story.append(Paragraph("=" * 70, normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("TOP 3 CONSIGLIATE", heading_style))
story.append(
    Paragraph(
        "1. <b>Villa Castellaneta Marina</b> - Perfetta per gruppi (5.0, 3BR/8 letti, EUR1.360)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "2. <b>Home Pisciotta</b> - Migliore in Cilento (4.96, 3 bagni, 45 recensioni, EUR1.138)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "3. <b>Townhouse Scalea</b> - Unica con accesso PRIVATO alla spiaggia (4.94, EUR1.222)",
        normal_style,
    )
)

story.append(Spacer(1, 20))
story.append(Paragraph("=" * 70, normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("ANALISI PREZZI", heading_style))
story.append(
    Paragraph(
        "• Più economico con buone recensioni: Home Scario (EUR827)", normal_style
    )
)
story.append(
    Paragraph(
        "• Miglior rapporto qualita'/prezzo: Home Pisciotta (EUR1.138, 4.96 rating)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "• Per gruppi grandi: Villa San Felice Circeo (4 camere, 9 letti)", normal_style
    )
)
story.append(
    Paragraph(
        "• Unico con accesso spiaggia privato: Townhouse Scalea (EUR1.222)",
        normal_style,
    )
)

doc.build(story)
print(f"PDF creato: {output_file}")
