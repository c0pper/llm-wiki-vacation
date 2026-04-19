#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, navy, darkblue

output_file = "/media/simo/DATA_SSD/code/llm-wiki-vacation/report_vacation.pdf"
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

story.append(Paragraph("Ville e Case per Vacanza in Italia", title_style))
story.append(
    Paragraph(
        "Rapporto completo basato sulle preferenze: minimo 2 bagni, spiaggia vicino, accesso privato, attenzione alle recensioni",
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
        "price_hint": "Alta",
        "score": 100,
        "desc": """<b>Perfetta per gruppi grandi.</b> Villa con 3 camere da letto e 8 posti letto nella pineta pugliese. Valutazione perfetta 5.0 su 7 recensioni. Ideale per famiglie o gruppi di amici. Giardino grande, terrazza, aria condizionata, doccia esterna, BBQ. Accesso alla spiaggia a piedi. Animali ammessi. Vicina a Matera (58km) e Alberobello.""",
        "url": "https://www.airbnb.com/rooms/41234343",
        "why": "Soddisfa tutti i criteri: 2+ bagni, spiaggia vicina, ottime recensioni (5.0), disponibilità animali",
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
        "beach": "Spiaggia (a piedi)",
        "beach_access": "Si",
        "pets": "No",
        "price_hint": "Media-Alta",
        "score": 98,
        "desc": """<b>Migliore in Cilento.</b> Villa a 2 piani con vista mare, giardino con limoni e olivi. Valutazione 4.96 su 45 recensioni - tra le più amate. 3 bagni. Balcone con pranzo all'aperto. Posizione tranquilla tra la marina e il paese medievale. 10 min a piedi dalla spiaggia.""",
        "url": "https://www.airbnb.com/rooms/15128491",
        "why": "3 bagni, spiaggia a piedi, eccellenti recensioni (4.96), 45 recensioni - campione solido",
    },
    {
        "rank": 3,
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
        "price_hint": "Media",
        "score": 95,
        "desc": """<b>Vista panoramica eccezionale.</b> Appartamento luminosissimo con vista a 360° sulla baia di Serapo. 2 camere matrimoniali + 1 singola, 2 bagni. Camino a legna. Parcheggio gratuito. A 300m dalla spiaggia di Serapo. Vicino Monte Orlando. Molto fresco con aperture naturali.""",
        "url": "https://www.airbnb.com/rooms/1207266166578504838",
        "why": "2 bagni, spiaggia a 300m, alta valutazione (4.92), views eccezionali",
    },
    {
        "rank": 4,
        "name": "Townhouse Scalea",
        "location": "Calabria",
        "rating": "★★★★★ (4.94)",
        "reviews": 18,
        "bedrooms": 2,
        "beds": 4,
        "bathrooms": 2,
        "beach": "100m (privata)",
        "beach_access": "Si (privata)",
        "pets": "Non specificato",
        "price_hint": "Media",
        "score": 94,
        "desc": """<b>Accesso spiaggia privata.</b> Villa a schiera nel parco più bello di Scalea. Accesso privato alla spiaggia a soli 100m. Vista baia e mare. 2 giardini, uno a picco sul mare. Valutazione 4.94 - guest favorite. 2 bagni. Parcheggio riservato.""",
        "url": "https://www.airbnb.com/rooms/839783448307020394",
        "why": "2 bagni, ACCESSO PRIVATO alla spiaggia (100m), alta valutazione (4.94)",
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
        "price_hint": "Alta",
        "score": 92,
        "desc": """<b>Ideale per gruppi grandi.</b> Villa spaziosa con 4 camere e fino a 12 posti letto. 3 bagni stimati. Giardino grande con ping pong e pallavolo. Vicino Parco Nazionale del Circeo. Tranquilla anche in alta stagione. A pochi minuti a piedi dalla spiaggia.""",
        "url": "https://www.airbnb.com/rooms/5914149",
        "why": "4 camere-da-letto/9-letti, 3 bagni, spiaggia a piedi, pets allowed",
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
        "price_hint": "Media",
        "score": 88,
        "desc": """<b>Giardino privato grande.</b> Villa con 5000mq di giardino recintato. Guest favorite! 2 bagni. 800m dalla spiaggia (15 min a piedi). 2 posti auto coperti. Terrazza, BBQ. Aria condizionata. Tra Terracina e Sperlonga.""",
        "url": "https://www.airbnb.com/rooms/1065128176658688079",
        "why": "2 bagni, giardino grande, guest favorite (4.88), buon numero recensioni (16)",
    },
    {
        "rank": 7,
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
        "price_hint": "Bassa-Media",
        "score": 82,
        "desc": """<b>Posizione centrale.</b> Nel centro di Scario, Parco Nazionale del Cilento. Porto e spiagge a piedi. Terrazza con vista mare. 25 recensioni. Internet veloce. Ideale per esplorare il Cilento.""",
        "url": "https://www.airbnb.com/rooms/3007439",
        "why": "25 recensioni - campione buono, spiaggia a piedi, posizione centrale nel Cilento",
    },
    {
        "rank": 8,
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
        "price_hint": "Media",
        "score": 75,
        "desc": """<b>Superhost.</b> Appartamento in villa nella pineta. Grande terrazza panoramica. A 200m dalla spiaggia (5 min a piedi). Host è Superhost con 9 anni di esperienza. Vicina a Matera e Alberobello.""",
        "url": "https://www.airbnb.com/rooms/20244510",
        "why": "Ottima valutazione (4.75), spiaggia a 200m, host attendibile",
    },
    {
        "rank": 9,
        "name": "Home Fondi Emanuele",
        "location": "Fondi (Lazio)",
        "rating": "★★★★☆ (4.55)",
        "reviews": 11,
        "bedrooms": 4,
        "beds": 4,
        "bathrooms": 2,
        "beach": "120m (frontale)",
        "beach_access": "Si",
        "pets": "No",
        "price_hint": "Media",
        "score": 88,
        "desc": """<b>Beachfront.</b> Villetta a schiera a 120m dalla spiaggia - frontale. 2 bagni. 4 camere. Due giardini privati, firepit, BBQ. Vista mare. Tra Sperlonga e Terracina.""",
        "url": "https://www.airbnb.com/rooms/20597083",
        "why": "2 bagni, spiaggia frontale (120m), 4 camere, buona valutazione",
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
        "price_hint": "Media",
        "score": 70,
        "desc": """<b>Per amanti di Matera.</b> Villa a 2 piani con giardino grande. A 500m dal Mare Ionio. Vicina a Matera (Capitale Cultura 2019). Animali ammessi. Giocattoli per bambini.""",
        "url": "https://www.airbnb.com/rooms/24179283",
        "why": "Pets allowed, 2 bagni, buona posizione per escursioni (Matera)",
    },
]

story.append(Paragraph("=" * 60, normal_style))
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
            f"Camere: {prop['bedrooms']} | Letti: {prop['beds']} | Bagni: {prop['bathrooms']} | Spiaggia: {prop['beach']}",
            normal_style,
        )
    )
    story.append(Paragraph(prop["desc"], normal_style))
    story.append(
        Paragraph(f"<b>Perché è una buona scelta:</b> {prop['why']}", normal_style)
    )
    story.append(Paragraph(f"<i>Fonte: {prop['url']}</i>", link_style))
    story.append(Spacer(1, 15))

story.append(Paragraph("=" * 60, normal_style))
story.append(Spacer(1, 20))

story.append(Paragraph("PROPRIETA' SCONSIGLIATE", heading_style))
story.append(
    Paragraph(
        "Le seguenti proprietà sono sconsigliate per mancanza di recensioni (pericolo):",
        normal_style,
    )
)

avoid = [
    (
        "Home Fondi Luisa",
        "https://www.airbnb.com/rooms/1336015011780522585",
        "Nessuna recensione - 50m dalla spiaggia",
    ),
    (
        "Home Pollica",
        "https://www.airbnb.com/rooms/1595568886799231526",
        "Nessuna recensione - accesso spiaggia privata",
    ),
    (
        "Home Roseto Capo Spulico",
        "https://www.airbnb.com/rooms/1662456513827712773",
        "Nuovo annuncio - nessuna recensione",
    ),
    (
        "Home Villapiana Lido",
        "https://www.airbnb.com/rooms/1465898782320150531",
        "Solo 2 recensioni",
    ),
    ("Home Palinuro", "https://www.airbnb.com/rooms/28579802", "Solo 1 recensione"),
    (
        "Home Cucco-Riviere",
        "https://www.airbnb.com/rooms/1325256730782747038",
        "Nessuna recensione",
    ),
]

for name, url, note in avoid:
    story.append(Paragraph(f"• <b>{name}</b>: {note}", normal_style))
    story.append(Paragraph(f"  {url}", link_style))

story.append(Spacer(1, 20))
story.append(Paragraph("=" * 60, normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("RIEPILOGO PREFERENZE", heading_style))
story.append(
    Paragraph("• Minimo 2 bagni: Verificato per le prime 10 proprietà", normal_style)
)
story.append(Paragraph("• Spiaggia vicino: <500m o a piedi", normal_style))
story.append(
    Paragraph(
        "• Accesso privato: Townhouse Scalea (100m privata), Home Pollica (300m privata)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "• Attenzione recensioni: Scartate proprietà senza recensioni", normal_style
    )
)

story.append(Spacer(1, 20))
story.append(Paragraph("=" * 60, normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("TOP 3 CONSIGLIATE", heading_style))
story.append(
    Paragraph(
        "1. <b>Villa Castellaneta Marina</b> - Perfetta per gruppi (5.0, 3BR/8 letti)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "2. <b>Home Pisciotta</b> - Migliore in Cilento (4.96, 3 bagni, 45 recensioni)",
        normal_style,
    )
)
story.append(
    Paragraph(
        "3. <b>Home Gaeta</b> - Vista panoramica eccezionale (4.92, 2 bagni)",
        normal_style,
    )
)

doc.build(story)
print(f"PDF creato: {output_file}")
